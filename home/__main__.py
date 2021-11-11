#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import importlib
import asyncio
import logging.config
import sys

import home

from apscheduler.schedulers.asyncio import AsyncIOScheduler

sys.path.append("..")

if __name__ == "__main__":
    (options, _) = home.options.parser().parse_args()
    if options.configuration_file:
        options = home.configs.parse(vars(options), options.configuration_file)

    knx_logging_level = "INFO"
    if options.knx_usbhid or options.knxnet_ip:
        if options.knx_usbhid:
            knx_logging_level = options.knx_usbhid_logging_level
        else:
            knx_logging_level = options.knxnet_ip_logging_level
    configuration = home.logger.default_logging_configuration(
        options.logging_dir,
        logging_level=options.logging_level,
        knx_logging_level=knx_logging_level,
        lifx_logging_level=options.lifx_logging_level,
        sonos_logging_level=options.sonos_logging_level,
        somfy_sdn_logging_level=options.somfy_sdn_logging_level,
        home_assistant_logging_level=options.home_assistant_logging_level,
    )
    logging.config.dictConfig(configuration)

    loop = asyncio.get_event_loop()

    if options.knx_usbhid or options.knxnet_ip:
        import knx_plugin
    if options.lifx:
        import lifx_plugin
    if options.sonos:
        import soco_plugin
    if options.somfy_sdn:
        import somfy_sdn_plugin
    if options.home_assistant:
        import home_assistant_plugin

    if options.blockly_file:
        with open("/tmp/workspace.py", "r") as fd:
            code = importlib.abc.InspectLoader.source_to_code(fd.read())
            exec(code)
    else:
        my_home = home.builder.my_home.Yaml(options.project_dir)
    redis_gateway = home.redis.Gateway(
        options.redis_host,
        options.redis_port,
        home.redis.gateway.serialization.Encoder,
        home.redis.gateway.serialization.Decoder().run,
        my_home.appliances,
        my_home.performers,
        home.redis.gateway.client.storage.Connection,
        home.redis.gateway.client.pubsub.Connection,
        options.my_node_name,
        options.other_nodes_names,
    )
    process = home.Process(my_home, redis_gateway)
    if options.knx_usbhid or options.knxnet_ip:
        if options.knx_usbhid:
            gateway = knx_plugin.gateway.usbhid.Gateway(
                knx_plugin.client.usbhid.Client,
                options.knx_usbhid_daemon_host,
                int(options.knx_usbhid_daemon_port),
            )
        else:
            gateway = knx_plugin.gateway.knxnet_ip.Gateway(
                knx_plugin.client.knxnet_ip.Client,
                options.knxnet_ip_server_host,
                int(options.knxnet_ip_server_port),
                options.knxnet_ip_client_host,
                int(options.knxnet_ip_client_port),
                options.knxnet_ip_nat_client_host,
                int(options.knxnet_ip_nat_client_port),
            )
        gateway.associate_commands(my_home.commands_by(knx_plugin.Description.PROTOCOL))
        gateway.associate_triggers(my_home.triggers_by(knx_plugin.Description.PROTOCOL))
        process.add(gateway)
    if options.lifx:
        gateway = lifx_plugin.Gateway(lifx_plugin.Client)
        gateway.associate_commands(
            my_home.commands_by(lifx_plugin.Description.PROTOCOL)
        )
        gateway.associate_triggers(
            my_home.triggers_by(lifx_plugin.Description.PROTOCOL)
        )
        process.add(gateway)
    if options.sonos:
        gateway = soco_plugin.Gateway()
        loop.run_until_complete(
            gateway.associate_commands(
                my_home.commands_by(soco_plugin.Description.PROTOCOL)
            )
        )
        loop.run_until_complete(
            gateway.associate_triggers(
                my_home.triggers_by(soco_plugin.Description.PROTOCOL)
            )
        )
        process.add(gateway)
    if options.somfy_sdn:
        gateway = somfy_sdn_plugin.Gateway(options.somfy_sdn_device)
        loop.run_until_complete(
            gateway.associate_commands(
                my_home.commands_by(somfy_sdn_plugin.Description.PROTOCOL)
            )
        )
        loop.run_until_complete(
            gateway.associate_triggers(
                my_home.triggers_by(somfy_sdn_plugin.Description.PROTOCOL)
            )
        )
        process.add(gateway)
    if options.home_assistant:
        gateway = home_assistant_plugin.Gateway(
            options.home_assistant_token,
            options.home_assistant_host,
            options.home_assistant_port,
        )
        gateway.associate_commands(
            my_home.commands_by(home_assistant_plugin.Description.PROTOCOL)
        )
        gateway.associate_triggers(
            my_home.triggers_by(home_assistant_plugin.Description.PROTOCOL)
        )
        process.add(gateway)

    scheduler = AsyncIOScheduler()
    my_home.schedule(scheduler, process.schedule)
    process.run(scheduler)

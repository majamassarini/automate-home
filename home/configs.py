# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import configparser
from collections import namedtuple


def parse(old_options: dict, file_name: str) -> namedtuple:
    """
    >>> import io
    >>> import tempfile
    >>> configuration = b'''
    ... [project]
    ... blockly_file = /tmp/workspace.py
    ... project_dir = /tmp
    ... logging_dir = /tmp
    ... logging_level = WARNING
    ... redis_host = localhost
    ... redis_port = 6379
    ... my_node_name = brain
    ... other_nodes_names = ws, graphite
    ...
    ... [home_assistant]
    ... host = 172.31.10.236
    ... port = 8123
    ... token = HA_TOKEN
    ... logging_level = WARNING
    ...
    ... [knx_usbhid]
    ... logging_level = WARNING
    ... daemon_host = 172.31.11.251
    ... daemon_port = 5555
    ...
    ... [knxnet_ip]
    ... logging_level = WARNING
    ... server_host = localhost
    ... server_port = 3761
    ... client_host = localhost
    ... client_port = 1736
    ... client_nat_host = localhost
    ... client_nat_port = 1736
    ...
    ... [lifx]
    ... logging_level = WARNING
    ...
    ... [sonos]
    ... logging_level = WARNING
    ...
    ... [somfy_sdn]
    ... logging_level = WARNING
    ... device = /dev/tty.usbmodemfd121
    ...
    ... [webserver]
    ... dir = /tmp
    ... logging_level = WARNING
    ... node_name = ws
    ... other_nodes_names = brain
    ... port = 8181
    ...
    ... [graphite_feeder]
    ... logging_level = WARNING
    ... server_host = localhost
    ... server_port = 8282
    ... data_port = 2003
    ... node_name = ws
    ... other_nodes_names = brain
    ... '''
    >>> def test_parse():
    ...     options = dict()
    ...     with tempfile.NamedTemporaryFile() as fp:
    ...         fp.write(configuration)
    ...         fp.flush()
    ...         options = parse({'project_dir': 'pippo'}, fp.name)
    ...     return options
    >>> test_parse()
    Options(project_dir='/tmp', blockly_file='/tmp/workspace.py', logging_dir='/tmp', logging_level='WARNING', redis_host='localhost', redis_port='6379', my_node_name='brain', other_nodes_names=['ws', ' graphite'], home_assistant=True, home_assistant_host='172.31.10.236', home_assistant_port='8123', home_assistant_token='HA_TOKEN', home_assistant_logging_level='WARNING', knx_usbhid=True, knx_usbhid_logging_level='WARNING', knx_usbhid_daemon_host='172.31.11.251', knx_usbhid_daemon_port='5555', knxnet_ip=True, knxnet_ip_logging_level='WARNING', knxnet_ip_server_host='localhost', knxnet_ip_server_port='3761', knxnet_ip_client_host='localhost', knxnet_ip_client_port='1736', knxnet_ip_client_nat_host='localhost', knxnet_ip_client_nat_port='1736', lifx=True, lifx_logging_level='WARNING', sonos=True, sonos_logging_level='WARNING', somfy_sdn=True, somfy_sdn_logging_level='WARNING', somfy_sdn_device='/dev/tty.usbmodemfd121', webserver=True, webserver_dir='/tmp', webserver_logging_level='WARNING', webserver_node_name='ws', webserver_other_nodes_names=['brain'], webserver_port='8181', graphite_feeder=True, graphite_feeder_logging_level='WARNING', graphite_feeder_server_host='localhost', graphite_feeder_server_port='8282', graphite_feeder_data_port='2003', graphite_feeder_node_name='ws', graphite_feeder_other_nodes_names=['brain'])

    :param old_options: a dictionary to be update
    :param file_name: path to a ini configuration file
    :return: a new updated options dictionary
    """
    PROJECT = "project"
    OTHER_NODES_NAMES = "other_nodes_names"

    config = configparser.ConfigParser()
    config.read(file_name)
    sections = config.sections()
    options = dict(old_options)

    if PROJECT in sections:
        for entry in config[PROJECT]:
            if entry == OTHER_NODES_NAMES:
                options[entry] = config[PROJECT][entry].split(",")
            else:
                options[entry] = config[PROJECT][entry]

    for section in [s for s in sections if s != PROJECT]:
        options[section] = True
        for entry in config[section]:
            if entry == OTHER_NODES_NAMES:
                options["{}_{}".format(section, entry)] = config[section][entry].split(
                    ","
                )
            else:
                options["{}_{}".format(section, entry)] = config[section][entry]

    Options = namedtuple("Options", options)
    return Options(**options)

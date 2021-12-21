# SPDX-License-Identifier: GPL-3.0-only
#
# automate home devices
#
# Copyright (C) 2021  Maja Massarini

import socket

from optparse import OptionParser, OptionGroup

GOOGLE_DNS_SERVER = "8.8.8.8"


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((GOOGLE_DNS_SERVER, 80))
    name = s.getsockname()[0]
    s.close()
    return name


def parser() -> OptionParser:
    """
    >>> args = ['--project-dir', '/tmp',
    ... '--logging-dir', '/tmp',
    ... '--blockly-file', '/tmp/workspace.py',
    ... '--enable-knx-usbhid',
    ... '--knx-usbhid-daemon-host', '172.31.11.251',
    ... '--enable-sonos', 'True',
    ... '--enable-lifx', 'True',
    ... '--enable-somfy-sdn', 'True',
    ... '--enable-home-assistant', 'True',
    ... '--home-assistant-token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI4NWJjZmRkMTE3NWU0YjM5YWMzNWNjMmI5MTRkYjM1NCIsImlhdCI6MTYwMjUwOTQxNiwiZXhwIjoxOTE3ODY5NDE2fQ.LCxbeAzU28rWVrwPdb-qq2ClJdygOJrtloQQF54EXGk',
    ... '--home-assistant-host', '172.31.10.236',
    ... '--logging-level', 'INFO',
    ... '--knx-usbhid-logging-level', 'ERROR',
    ... '--lifx-logging-level', 'ERROR',
    ... '--sonos-logging-level', 'ERROR',
    ... '--home-assistant-logging-level', 'DEBUG']
    >>> (options, args) = parser().parse_args(args)
    >>> options.project_dir
    '/tmp'
    >>> options.knx_usbhid
    True
    >>> options.other_nodes_names
    ['ws', 'graphite']
    >>> options.redis_port
    '6379'

    :return: An enriched OptionParser
    """
    parser = OptionParser()
    parser.add_option(
        "-c",
        "--configuration-file",
        dest="configuration_file",
        help="File where the project configuration directives will be found",
        metavar="CONFIGURATION FILE",
    )
    parser.add_option(
        "-b",
        "--blockly-file",
        dest="blockly_file",
        help="Blockly file configuration",
        metavar="BLOCKLY CONFIGURATION FILE",
    )
    parser.add_option(
        "-d",
        "--project-dir",
        default="/usr/share/automate-home",
        dest="project_dir",
        help="Directory where project files will be found",
        metavar="PROJECT DIR",
    )
    parser.add_option(
        "-l",
        "--logging-dir",
        default="/var/log/automate-home",
        dest="logging_dir",
        help="Log data dir",
        metavar="LOGGING DIR",
    )
    parser.add_option(
        "-v",
        "--logging-level",
        default="WARNING",
        dest="logging_level",
        help="Logging level",
        metavar="LOGGING LEVEL",
    )
    parser.add_option(
        "-r",
        "--redis-host",
        default="127.0.0.1",
        dest="redis_host",
        help="Redis server host",
        metavar="REDIS HOST",
    )
    parser.add_option(
        "-p",
        "--redis-port",
        default="6379",
        dest="redis_port",
        help="Redis server port",
        metavar="REDIS PORT",
    )
    parser.add_option(
        "-m",
        "--my-node-name",
        default="brain",
        dest="my_node_name",
        help="My node name to be used with pub/sub",
        metavar="NODE NAME",
    )
    parser.add_option(
        "-o",
        "--other-nodes-names",
        action="append",
        default=["ws", "graphite"],
        dest="other_nodes_names",
        help="Other nodes to be notified with pub/sub",
        metavar="OTHER NODES NAMES",
    )

    ha_group = OptionGroup(parser, "Home Assistant Options")
    parser.add_option_group(ha_group)

    ha_group.add_option(
        "--enable-home-assistant",
        action="store_true",
        default=False,
        dest="home_assistant",
        help="Enable Home Assistant integration through websocket API",
        metavar="ENABLE HOME ASSISTANT",
    )
    ha_group.add_option(
        "--home-assistant-host",
        default="localhost",
        dest="home_assistant_host",
        help="Home Assistant Web Socket Server Host",
        metavar="HOME ASSISTANT WS HOST",
    )
    ha_group.add_option(
        "--home-assistant-port",
        default="8123",
        dest="home_assistant_port",
        help="Home Assistant Web Socket Server Port",
        metavar="HOME ASSISTANT WS PORT",
    )
    ha_group.add_option(
        "--home-assistant-token",
        default="",
        dest="home_assistant_token",
        help="Home Assistant Long Live Token",
        metavar="HOME ASSISTANT LONG LIVE TOKEN",
    )
    ha_group.add_option(
        "--home-assistant-logging-level",
        default="WARNING",
        dest="home_assistant_logging_level",
        help="Home Assistant Plugin Logging Level",
        metavar="HOME ASSISTANT LOGGING LEVEL",
    )

    knx_usb_hid_group = OptionGroup(parser, "KNX USB Hid Options")
    parser.add_option_group(knx_usb_hid_group)

    knx_usb_hid_group.add_option(
        "--enable-knx-usbhid",
        action="store_true",
        default=False,
        dest="knx_usbhid",
        help="Enable KNX (trough a USB interface)",
        metavar="KNX",
    )
    knx_usb_hid_group.add_option(
        "--knx-usbhid-daemon-host",
        default="localhost",
        dest="knx_usbhid_daemon_host",
        help="KNX USB Hid CEMI Daemon Host",
        metavar="KNX USBHID DAEMON HOST",
    )
    knx_usb_hid_group.add_option(
        "--knx-usbhid-daemon-port",
        default="5555",
        dest="knx_usbhid_daemon_port",
        help="KNX USB Hid CEMI Daemon Port",
        metavar="KNX CEMI DAEMON PORT",
    )
    knx_usb_hid_group.add_option(
        "--knx-usbhid-logging-level",
        default="WARNING",
        dest="knx_usbhid_logging_level",
        help="Knx USB Hid Logging Level",
        metavar="KNX USBHID LOGGING LEVEL",
    )

    knx_netip_group = OptionGroup(parser, "KNXNet/IP options")
    parser.add_option_group(knx_netip_group)

    knx_netip_group.add_option(
        "--enable-knxnet-ip",
        action="store_true",
        default=False,
        dest="knxnet_ip",
        help="Enable KNX (through a KNXNet/IP interface)",
        metavar="KNXNET/IP",
    )
    knx_netip_group.add_option(
        "--knxnet-ip-server-host",
        default="172.31.11.251",
        dest="knxnet_ip_server_host",
        help="KNXNet/IP Server Host",
        metavar="KNXNET/IP SERVER HOST",
    )
    knx_netip_group.add_option(
        "--knxnet-ip-server-port",
        default="3761",
        dest="knxnet_ip_server_port",
        help="KNXNet/IP Server Port",
        metavar="KNXNET/IP SERVER PORT",
    )
    knx_netip_group.add_option(
        "--knxnet-ip-client-host",
        default=get_local_ip(),
        dest="knxnet_ip_client_host",
        help="Where KNXNet/IP Client is Listening for messages (host)",
        metavar="KNXNET/IP CLIENT HOST",
    )
    knx_netip_group.add_option(
        "--knxnet-ip-client-port",
        default="1736",
        dest="knxnet_ip_client_port",
        help="Where KNXNet/IP Client is Listening for messages (port)",
        metavar="KNXNET/IP CLIENT PORT",
    )
    knx_netip_group.add_option(
        "--knxnet-ip-nat-client-host",
        default=get_local_ip(),
        dest="knxnet_ip_nat_client_host",
        help="Where KNXNet/IP Client is Listening for messages (natted ip)",
        metavar="KNXNet/IP NATTED CLIENT HOST",
    )
    knx_netip_group.add_option(
        "--knxnet-ip-nat-client-port",
        default="1736",
        dest="knxnet_ip_nat_client_port",
        help="Where KNXNet/IP Client is Listening for messages (natted port)",
        metavar="KNXNet/IP NATTED CLIENT PORT",
    )
    knx_netip_group.add_option(
        "--knxnet-ip-logging-level",
        default="WARNING",
        dest="knxnet_ip_logging_level",
        help="KNXNet/IP Logging Level",
        metavar="KNXNet/IP LOGGING LEVEL",
    )

    lifx_group = OptionGroup(parser, "Lifx Options")
    parser.add_option_group(lifx_group)
    lifx_group.add_option(
        "--enable-lifx",
        action="store_true",
        default=False,
        dest="lifx",
        help="Enable Lifx",
    )
    lifx_group.add_option(
        "--lifx-logging-level",
        default="WARNING",
        dest="lifx_logging_level",
        help="Lifx Logging Level",
        metavar="LIFX LOGGING LEVEL",
    )

    sonos_group = OptionGroup(parser, "Sonos Options")
    parser.add_option_group(sonos_group)
    sonos_group.add_option(
        "--enable-sonos",
        action="store_true",
        default=False,
        dest="sonos",
        help="Enable Sonos",
    )
    sonos_group.add_option(
        "--sonos-logging-level",
        default="WARNING",
        dest="sonos_logging_level",
        help="Sonos Logging Level",
        metavar="SONOS LOGGING LEVEL",
    )

    somfy_sdn_group = OptionGroup(parser, "Somfy Sdn Options")
    parser.add_option_group(somfy_sdn_group)

    somfy_sdn_group.add_option(
        "--enable-somfy-sdn",
        action="store_true",
        default=False,
        dest="somfy_sdn",
        help="Enable Somfy Sdn",
    )
    somfy_sdn_group.add_option(
        "--somfy-sdn-device",
        default="/dev/tty.usbmodemfd121",
        dest="somfy_sdn_device",
        help="Serial Device for Somfy Sdn",
        metavar="SOMFY SDN SERIAL DEVICE",
    )
    somfy_sdn_group.add_option(
        "--somfy-sdn-logging-level",
        default="WARNING",
        dest="somfy_sdn_logging_level",
        help="Somfy Sdn Logging Level",
        metavar="SOMFY SDN LOGGING LEVEL",
    )

    webserver_group = OptionGroup(parser, "Webserver Options")
    parser.add_option_group(webserver_group)

    webserver_group.add_option(
        "--webserver-dir",
        default="/usr/share/automate-home",
        dest="webserver_dir",
        help="Directory where webserver configuration files will be found",
        metavar="WEBSERVER DIRECTORY",
    )
    webserver_group.add_option(
        "--webserver-port",
        default="8181",
        dest="webserver_port",
        help="port for webserver",
        metavar="WEBSERVER PORT",
    )
    webserver_group.add_option(
        "--webserver-logging-level",
        default="WARNING",
        dest="webserver_logging_level",
        help="Webserver Logging Level",
        metavar="WEBSERVER LOGGING LEVEL",
    )
    webserver_group.add_option(
        "--webserver-node-name",
        default="ws",
        dest="webserver_node_name",
        help="Webserver node name to be used with pub/sub",
        metavar="WEBSERVER NODE NAME",
    )
    webserver_group.add_option(
        "--webserver-other-nodes-names",
        default=["brain"],
        action="append",
        dest="webserver_other_nodes_names",
    )

    graphite_feeder_group = OptionGroup(parser, "Graphite Feeder Options")
    parser.add_option_group(graphite_feeder_group)

    graphite_feeder_group.add_option(
        "--enable-graphite-feeder",
        action="store_true",
        default=False,
        dest="graphite_feeder",
        help="Enable Graphite Feeder",
    )
    graphite_feeder_group.add_option(
        "--graphite-feeder-logging-level",
        default="WARNING",
        dest="graphite_feeder_logging_level",
        help="Graphite Feeder Logging Level",
        metavar="GRAPHITE FEEDER LOGGING LEVEL",
    )
    graphite_feeder_group.add_option(
        "--graphite-host",
        default="localhost",
        dest="graphite_feeder_server_host",
        help="Graphite (host)",
        metavar="GRAPHITE SERVER HOST",
    )
    graphite_feeder_group.add_option(
        "--graphite-port",
        default="8282",
        dest="graphite_feeder_server_port",
        help="Graphite (port)",
        metavar="GRAPHITE SERVER PORT",
    )
    graphite_feeder_group.add_option(
        "--graphite-data-port",
        default="8282",
        dest="graphite_feeder_data_port",
        help="Graphite push data (port)",
        metavar="GRAPHITE SERVER DATA PORT",
    )
    graphite_feeder_group.add_option(
        "--graphite-feeder-node-name",
        default="graphite",
        dest="graphite_feeder_node_name",
        help="Graphite Feeder node name to be used with pub/sub",
        metavar="GRAPHITE FEEDER NODE NAME",
    )
    graphite_feeder_group.add_option(
        "--graphite-feeder-other-nodes-names",
        default=["brain"],
        action="append",
        dest="graphite_feeder_other_nodes_names",
        metavar="GRAPHITE FEEDER OTHER NODES NAMES",
    )

    return parser

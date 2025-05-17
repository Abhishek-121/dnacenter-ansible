#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wired_network_devices_id_config_features_intended_layer2_feature
short_description: Resource module for Wired Network Devices Id Config Features Intended
  Layer2 Feature
description:
  - This module represents an alias of the module wired_network_devices_id_config_features_intended_layer2_feature_v1
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  cdpGlobalConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      cdpGlobalConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality configured for CDP. Config
                  type CDP_GLOBAL is for configuring the global settings for CDP.
                type: str
              holdTime:
                description: Specifies the amount of time a receiving device should
                  hold the information sent by the device before discarding it. Corresponding
                  CLI - cdp holdtime <10-255>.
                type: int
              isAdvertiseV2Enabled:
                description: Configures CDP to send Version-2 advertisements. The
                  default state is enabled. Corresponding CLI - cdp advertise-v2.
                type: bool
              isCdpEnabled:
                description: Enables or disables CDP on the device. Corresponding
                  CLI - cdp run. Default true.
                type: bool
              isLogDuplexMismatchEnabled:
                description: Configures the reporting of duplex mismatches generated
                  by CDP for all Ethernet interfaces on the device. Corresponding
                  CLI - cdp log mismatch. Duplex. Default true.
                type: bool
              timer:
                description: Sets the transmission frequency of CDP updates in seconds.
                  Corresponding CLI - cdp timer <5-254>.
                type: int
            type: list
        type: list
    type: dict
  cdpInterfaceConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      cdpInterfaceConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config
                  type CDP_INTERFACE is for configuring CDP on an interface.
                type: str
              interfaceName:
                description: Interface name. The API /dna/intent/api/v1/interface/network-device/{deviceId}
                  can be used to get the list of interfaces on a device. Example GigabitEthernet1/0/1.
                type: str
              isCdpEnabled:
                description: Enables or disables CDP on the interface. Corresponding
                  CLI - cdp enable. Default true.
                type: bool
              isLogDuplexMismatchEnabled:
                description: Configures the reporting of duplex mismatches generated
                  by CDP for all Ethernet interfaces on the device. Corresponding
                  CLI - cdp log mismatch duplex. Default true.
                type: bool
            type: list
        type: list
    type: dict
  dhcpSnoopingGlobalConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      dhcpSnoopingGlobalConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config
                  type DHCP_SNOOPING_GLOBAL is for configuring the global settings
                  for DHCP snooping.
                type: str
              databaseAgent:
                description: Wired Network Devices Id Config Features Intended Layer2
                  Feature's databaseAgent.
                suboptions:
                  agentUrl:
                    description: Example tftp //192.168.1.100/db_backup Specify the
                      URL for the database agent or the binding file. Corresponding
                      CLI - ip dhcp snooping database .
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config
                      type DHCP_SNOOPING_DATABASE_AGENT is for configuring DHCP snooping
                      database agent settings on a device.
                    type: str
                  timeout:
                    description: Specify the duration, in seconds, after which a configuration
                      process will be automatically terminated. Corresponding CLI
                      - ip dhcp snooping database timeout <0-86400>.
                    type: int
                  writeDelay:
                    description: WriteDelay.
                    type: int
                type: dict
              dhcpSnoopingVlans:
                description: Enable DHCP snooping on VLANs. VLANs can be comma separated
                  and/or a range like '2,4-5,7,10-20'. Corresponding CLI - ip dhcp
                  snooping vlan .
                type: str
              isDhcpSnoopingEnabled:
                description: Enable DHCP snooping globally. Corresponding CLI - ip
                  dhcp snooping.default false.
                type: bool
              isGleaningEnabled:
                description: Enable DHCP gleaning which allows components to register
                  and glean only DHCP version 4 packets. Corresponding CLI - ip dhcp
                  snooping glean.default false.
                type: bool
              proxyBridgeVlans:
                description: Enable bridge mode on VLANs. VLANs can be comma separated
                  and/or a range like '2,4-5,7,10-20'. Corresponding CLI - ip dhcp
                  snooping vlan proxy-bridge.
                type: str
            type: list
        type: list
    type: dict
  dhcpSnoopingInterfaceConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      dhcpSnoopingInterfaceConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config
                  type DHCP_SNOOPING_INTERFACE is for configuring DHCP snooping on
                  an interface.
                type: str
              interfaceName:
                description: Interface name. The API /intent/api/v1/interface/network-device/{deviceId}
                  can be used to get the list of interfaces on a device.example GigabitEthernet1/0/1.
                type: str
              isTrustedInterface:
                description: Enable Trusted Interface. Corresponding CLI - ip dhcp
                  snooping trust.
                type: bool
              messageRateLimit:
                description: Limit the number of DHCP packets a port can send or receive
                  in a second. This is a protective measure to prevent a single device
                  from overwhelming the DHCP server. Increase the rate limit on trunk
                  ports carrying more than one VLAN. By default, rate limit is disabled.
                  The recommended value is <= 100. Set the rate-limit as 0 to disable
                  it. Corresponding CLI - ip dhcp snooping limit rate <1-2048>.
                type: int
            type: list
        type: list
    type: dict
  dot1xGlobalConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      dot1xGlobalConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              authenticationConfigMode:
                description: ReadOnly attribute. Identity-Based Networking Services
                  features are configured in the Cisco common classification policy
                  language (C3PL) display mode. The legacy authentication manager
                  mode is enabled by default. Use this command in EXEC mode to display
                  the current configuration mode. Corresponding CLI - authentication
                  display config-mode. LEGACY - Legacy configuration mode. NEW_STYLE
                  - Identity-Based Networking Services (IBNS) configuration mode.
                type: str
              configType:
                description: Type of network functionality under a feature. Config
                  type DOT1X_GLOBAL is for global 802.1x settings on a device.
                type: str
              isDot1xEnabled:
                description: Globally enable 802.1x authentication on Switch. Corresponding
                  CLI - dot1x system-auth-control. Default false.
                type: bool
            type: list
        type: list
    type: dict
  dot1xInterfaceConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      dot1xInterfaceConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              authenticationOrder:
                description: Wired Network Devices Id Config Features Intended Layer2
                  Feature's authenticationOrder.
                suboptions:
                  configType:
                    description: ConfigType.
                    type: str
                  items:
                    description: Array of Enums. DOT1X, MAB, WEBAUTH.
                    elements: str
                    type: list
                type: dict
              configType:
                description: Type of network functionality under a feature. Config
                  type DOT1X_INTERFACE is for configuring 802.1x on an interface.
                type: str
              interfaceName:
                description: Interface name. The API /intent/api/v1/interface/network-device/{deviceId}
                  can be used to get the list of interfaces on a device.example GigabitEthernet1/0/1.
                type: str
            type: list
        type: list
    type: dict
  feature:
    description: Feature path parameter. Name of the feature to delete.
    type: str
  id:
    description: Id path parameter. Network device ID of the wired device to configure.
    type: str
  igmpSnoopingGlobalConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      igmpSnoopingGlobalConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config
                  type IGMP_SNOOPING_GLOBAL is for configuring global IGMP snooping
                  settings on a device.
                type: str
              igmpSnoopingVlanSettings:
                description: Wired Network Devices Id Config Features Intended Layer2
                  Feature's igmpSnoopingVlanSettings.
                suboptions:
                  configType:
                    description: ConfigType.
                    type: str
                  items:
                    description: Wired Network Devices Id Config Features Intended
                      Layer2 Feature's items.
                    elements: dict
                    suboptions:
                      configType:
                        description: Type of network functionality under a feature.
                          Config type IGMP_SNOOPING_VLAN is for configuring IGMP snooping
                          per VLAN.
                        type: str
                      igmpSnoopingVlanMrouters:
                        description: Wired Network Devices Id Config Features Intended
                          Layer2 Feature's igmpSnoopingVlanMrouters.
                        suboptions:
                          configType:
                            description: Type of IGMP Snooping Mrouter Settings.
                            type: str
                          items:
                            description: Wired Network Devices Id Config Features
                              Intended Layer2 Feature's items.
                            elements: dict
                            suboptions:
                              configType:
                                description: Type of network functionality under a
                                  feature. Config type IGMP_SNOOPING_VLAN_MROUTER
                                  is for configuring IGMP snooping mrouter per VLAN.
                                type: str
                              interfaceName:
                                description: Mrouter interface name. The API /dna/intent/api/v1/interface/network-dev...
                                  can be used to get the list of interfaces on a device.example
                                  GigabitEthernet1/0/2.
                                type: str
                            type: list
                        type: dict
                      isIgmpSnoopingEnabled:
                        description: Enable IGMP Snooping for a VLAN. Corresponding
                          CLI - ip igmp snooping vlan <1-4094>.
                        type: bool
                      isImmediateLeaveEnabled:
                        description: Enable immediate leave processing for IGMPv2.
                          Corresponding CLI - ip igmp snooping vlan <vlan-id> immediate-leave.default
                          false.
                        type: bool
                      isQuerierEnabled:
                        description: Enable IGMP querier for this VLAN. Corresponding
                          CLI - ip igmp snooping vlan <vlan-id> querier.
                        type: bool
                      querierAddress:
                        description: IGMP querier source IP address. Corresponding
                          CLI - ip igmp snooping vlan <vlan-id> querier address <ip-address>.
                        type: str
                      querierQueryInterval:
                        description: Set the IGMP querier query interval (in seconds).
                          Corresponding CLI - ip igmp snooping vlan <vlan-id> querier
                          query-interval <1-18000>.
                        type: int
                      querierVersion:
                        description: The switch supports IGMP version 1, IGMP version
                          2, and IGMP version 3. These versions are interoperable
                          on the switch. For example, if IGMP snooping is enabled
                          and the querier's version is IGMPv2, and the switch receives
                          an IGMPv3 report from a host, then the switch can forward
                          the IGMPv3 report to the multicast router. Corresponding
                          CLI - ip igmp snooping querier version <1-3>. IGMP version
                          1 provides the basic query-response mechanism that allows
                          the multicast device to determine which multicast groups
                          are active and other processes that enable hosts to join
                          and leave a multicast group. IGMP version 2 extends IGMP
                          functionality by providing such features as the IGMP leave
                          process to reduce leave latency, group-specific queries,
                          and an explicit maximum query response time. IGMPv2 also
                          addsthe capability for routers to elect the IGMP querier
                          without depending on the multicast protocol to perform this
                          task. An IGMP version 3 switch supports Basic IGMPv3SnoopingSupport
                          (BISS), which includes support for the snooping features
                          on IGMPv1 and IGMPv2 switches and for IGMPv3 membership
                          report messages. BISS constrains the flooding of multicast
                          traffic when your network includes IGMPv3 hosts. It constrains
                          traffic to approximately the same set of ports as the IGMP
                          snooping feature on IGMPv2 or IGMPv1 hosts. An IGMPv3 switch
                          can receive messages from and forward messages to a device
                          running theSourceSpecific Multicast (SSM) feature.
                        type: str
                      vlanId:
                        description: VLAN ID.
                        type: int
                    type: list
                type: dict
              isIgmpSnoopingEnabled:
                description: Enable global IGMP Snooping. Corresponding CLI - ip igmp
                  snooping.default true.
                type: bool
              isQuerierEnabled:
                description: Enable IGMP Snooping Querier. Corresponding CLI - ip
                  igmp snooping querier.default false.
                type: bool
              querierAddress:
                description: Configure IGMP querier source IP address. Corresponding
                  CLI - ip igmp snooping querier address <ip-address>.
                type: str
              querierQueryInterval:
                description: Set the IGMP querier query interval (in seconds). Corresponding
                  CLI - ip igmp snooping querier query-interval <1-18000>.
                type: int
              querierVersion:
                description: The switch supports IGMP version 1, IGMP version 2, and
                  IGMP version 3. These versions are interoperable on the switch.
                  For example, if IGMP snooping is enabled and the querier's version
                  is IGMPv2, and the switch receives an IGMPv3 report from a host,
                  then the switch can forward the IGMPv3 report to the multicast router.
                  Corresponding CLI - ip igmp snooping querier version <1-3>. IGMP
                  version 1 provides the basic query-response mechanism that allows
                  the multicast device to determine which multicast groups are active
                  and other processes that enable hosts to join and leave a multicast
                  group. IGMP version 2 extends IGMP functionality by providing such
                  features as the IGMP leave process to reduce leave latency, group-specific
                  queries, and an explicit maximum query response time. IGMPv2 also
                  adds the capability for routers to elect the IGMP querier without
                  depending on the multicast protocol to perform this task. An IGMP
                  version 3 switch supports Basic IGMPv3SnoopingSupport (BISS), which
                  includes support for the snooping features on IGMPv1 and IGMPv2
                  switches and for IGMPv3 membership report messages. BISS constrains
                  the flooding of multicast traffic when your network includes IGMPv3
                  hosts. It constrains traffic to approximately the same set of ports
                  as the IGMP snooping feature on IGMPv2 or IGMPv1 hosts. An IGMPv3
                  switch can receive messages from and forward messages to a device
                  running theSourceSpecific Multicast (SSM) feature.
                type: str
            type: list
        type: list
    type: dict
  lldpGlobalConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      lldpGlobalConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality configured for LLDP. Config
                  type LLDP_GLOBAL is for configuring the global settings for LLDP.
                type: str
              holdTime:
                description: Specifies the amount of time a receiving device should
                  hold the information sent by the device before discarding it. Corresponding
                  CLI - lldp holdtime $holdTime <0-32767>.
                type: int
              isLldpEnabled:
                description: Enables or disables LLDP on the device. Corresponding
                  CLI - lldp run. Default true.
                type: bool
              reinitializationDelay:
                description: Specifies the delay time in seconds for LLDP to initialize
                  on any interface. Corresponding CLI - lldp reinit <2-5>.
                type: int
              timer:
                description: Sets the transmission frequency of LLDP updates in seconds.
                  Corresponding CLI - lldp timer <5-32767>.
                type: int
            type: list
        type: list
    type: dict
  lldpInterfaceConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      lldpInterfaceConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              adminStatus:
                description: Configure the interface to transmit and receive LLDP
                  packets, or disable LLDP on the interface. TRANSMIT_ONLY - Configure
                  the interface to transmit LLDP packets only. Corresponding CLI -
                  lldp transmit. RECEIVE_ONLY - Configure the interface to receive
                  LLDP packets only. Corresponding CLI - lldp receive. TRANSMIT_AND_RECEIVE
                  - Configure the interface to both transmit and receive LLDP packets.
                  Corresponding CLI - lldp receive; lldp transmit. DISABLED - Disable
                  LLDP functionality on the device, preventing both transmission and
                  reception of LLDP packets.
                type: str
              configType:
                description: Type of network functionality under a feature. Config
                  type LLDP_INTERFACE is for configuring LLDP on an interface.
                type: str
              interfaceName:
                description: Interface name. The API /intent/api/v1/interface/network-device/{deviceId}
                  can be used to get the list of interfaces on a device. Example GigabitEthernet1/0/1.
                type: str
            type: list
        type: list
    type: dict
  mabInterfaceConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      mabInterfaceConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config
                  type MAB_INTERFACE is for configuring MAB on an interface.
                type: str
              interfaceName:
                description: Interface name. The API /intent/api/v1/interface/network-device/{deviceId}
                  can be used to get the list of interfaces on a device.
                type: str
              isMabEnabled:
                description: Enable MAC-based authentication on a port. Corresponding
                  CLI - mab. Default false.
                type: bool
            type: list
        type: list
    type: dict
  mldSnoopingGlobalConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      mldSnoopingGlobalConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config
                  type MLD_SNOOPING_GLOBAL is for configuring MLD snooping settings
                  on a device.
                type: str
              isMldSnoopingEnabled:
                description: Enable global MLD Snooping. Corresponding CLI - ipv6
                  mld snooping.default false.
                type: bool
              isQuerierEnabled:
                description: Enable MLD Snooping Querier. Corresponding CLI - ipv6
                  mld snooping querier.default false.
                type: bool
              isSuppressListenerMessagesEnabled:
                description: When Listener Message Suppression is enabled, the switch
                  forwards only a single MLD report per multicast router query. Corresponding
                  CLI - ipv6 mld snooping listener-message-suppression.default true.
                type: bool
              mldSnoopingVlanSettings:
                description: Wired Network Devices Id Config Features Intended Layer2
                  Feature's mldSnoopingVlanSettings.
                suboptions:
                  configType:
                    description: Type of MLD Snooping VLAN Settings.
                    type: str
                  items:
                    description: Wired Network Devices Id Config Features Intended
                      Layer2 Feature's items.
                    elements: dict
                    suboptions:
                      configType:
                        description: Type of network functionality under a feature.
                          Config type MLD_SNOOPING_VLAN is for configuring MLD snooping
                          per VLAN.
                        type: str
                      isImmediateLeaveEnabled:
                        description: Enable immediate leave processing for MLDv1.
                          Corresponding CLI - ipv6 mld snooping vlan <vlan-id> immediate-leave.default
                          false.
                        type: bool
                      isMldSnoopingEnabled:
                        description: Enable MLD Snooping for a VLAN. Corresponding
                          CLI - ipv6 mld snooping vlan <1-4094>.
                        type: bool
                      isQuerierEnabled:
                        description: Enable MLD querier for this VLAN. Corresponding
                          CLI - ipv6 mld snooping vlan <vlan-id> querier.
                        type: bool
                      mldSnoopingVlanMrouters:
                        description: Wired Network Devices Id Config Features Intended
                          Layer2 Feature's mldSnoopingVlanMrouters.
                        suboptions:
                          configType:
                            description: Type of MLD Snooping Mrouter Settings.
                            type: str
                          items:
                            description: Wired Network Devices Id Config Features
                              Intended Layer2 Feature's items.
                            elements: dict
                            suboptions:
                              configType:
                                description: Type of network functionality under a
                                  feature. Config type MLD_SNOOPING_VLAN_MROUTER is
                                  for configuring MLD snooping mrouter per VLAN.
                                type: str
                              interfaceName:
                                description: Mrouter interface name. The API /dna/intent/api/v1/interface/network-dev...
                                  can be used to get the list of interfaces on a device.example
                                  GigabitEthernet1/0/2.
                                type: str
                            type: list
                        type: dict
                      querierAddress:
                        description: MLD querier source IP address. Corresponding
                          CLI - ipv6 mld snooping vlan <vlan-id> querier address <source-ipv6-address>.
                        type: str
                      querierQueryInterval:
                        description: Set the MLD querier query interval (in seconds).
                          Corresponding CLI - ipv6 mld snooping vlan <vlan-id> querier
                          query-interval <1-18000>.
                        type: int
                      querierVersion:
                        description: Configure MLD version. Corresponding CLI - ipv6
                          mld snooping vlan <vlan-id> querier version <1-2> VERSION_1
                          - MLDv1 snooping detects MLDv1 control packets and sets
                          up traffic bridging based on IPv6 destination multicast
                          addresses. MLDv1 supports three types of messages - Listener
                          Queries, Multicast Listener Reports, Multicast Listener
                          Done. VERSION_2 - MLDv2 basic snooping (MBSS) uses MLDv2
                          control packets to set up traffic forwarding based on IPv6
                          destination multicast addresses. MLDv2 supports MLDv2 queries
                          and reports, as well as MLDv1 Report and Done messages.
                        type: str
                      vlanId:
                        description: VLAN ID.
                        type: int
                    type: list
                type: dict
              querierAddress:
                description: MLD querier source IP address. Corresponding CLI - ipv6
                  mld snooping querier address <source-ipv6-address>.
                type: str
              querierQueryInterval:
                description: Set the MLD querier query interval (in seconds). Corresponding
                  CLI - ipv6 mld snooping querier query-interval <1-18000>.
                type: int
              querierVersion:
                description: Configure the MLD version. Corresponding CLI - ipv6 mld
                  snooping querier version <1-2> VERSION_1 - MLDv1 snooping detects
                  MLDv1 control packets and sets up traffic bridging based on IPv6
                  destination multicast addresses. MLDv1 supports three types of messages
                  - Listener Queries, Multicast Listener Reports, Multicast Listener
                  Done. VERSION_2 - MLDv2 basic snooping (MBSS) uses MLDv2 control
                  packets to set up traffic forwarding based on IPv6 destination multicast
                  addresses. MLDv2 supports MLDv2 queries and reports, as well as
                  MLDv1 Report and Done messages.
                type: str
            type: list
        type: list
    type: dict
  portChannelConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      portChannelConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality configured for Portchannel.
                type: str
              isAutoEnabled:
                description: Enables the auto-LAG feature on a switch globally. Corresponding
                  CLI - port-channel auto.default false.
                type: bool
              lacpSystemPriority:
                description: Configures the LACP system priority. Corresponding CLI
                  - lacp system-priority <0-65535>.
                type: int
              loadBalancingMethod:
                description: Configures an EtherChannel load-balancing method. Corresponding
                  CLI - port-channel load-balance .
                type: str
              portchannels:
                description: Wired Network Devices Id Config Features Intended Layer2
                  Feature's portchannels.
                suboptions:
                  configType:
                    description: Type of Portchannels.
                    type: str
                  items:
                    description: Wired Network Devices Id Config Features Intended
                      Layer2 Feature's items.
                    elements: dict
                    suboptions:
                      AnyOf:
                        description: Wired Network Devices Id Config Features Intended
                          Layer2 Feature's AnyOf.
                        suboptions:
                          EtherchannelConfig:
                            description: Wired Network Devices Id Config Features
                              Intended Layer2 Feature's EtherchannelConfig.
                            suboptions:
                              configType:
                                description: Type of a Portchannel.
                                type: str
                              memberPorts:
                                description: Wired Network Devices Id Config Features
                                  Intended Layer2 Feature's memberPorts.
                                suboptions:
                                  configType:
                                    description: Type of member ports.
                                    type: str
                                  items:
                                    description: Wired Network Devices Id Config Features
                                      Intended Layer2 Feature's items.
                                    elements: dict
                                    suboptions:
                                      configType:
                                        description: Type of network functionality
                                          configured for Etherchannel member port.default
                                          ETHERCHANNEL_MEMBER_PORT_CONFIG.
                                        type: str
                                      interfaceName:
                                        description: InterfaceName.
                                        type: str
                                      mode:
                                        description: Mode.
                                        type: str
                                    type: list
                                type: dict
                              minLinks:
                                description: Specifies the minimum number of member
                                  ports that must be in the link-up state and bundled
                                  in the EtherChannel for the port channel interface
                                  to transition to the link-up state. Corresponding
                                  CLI - port-channel min-links <2-8>.
                                type: int
                              name:
                                description: Configures the channel group. Corresponding
                                  CLI - interface port-channel <1-128>.
                                type: str
                            type: dict
                          LacpPortchannelConfig:
                            description: Wired Network Devices Id Config Features
                              Intended Layer2 Feature's LacpPortchannelConfig.
                            suboptions:
                              configType:
                                description: Type of a Portchannel.
                                type: str
                              memberPorts:
                                description: Wired Network Devices Id Config Features
                                  Intended Layer2 Feature's memberPorts.
                                suboptions:
                                  configType:
                                    description: Type of member ports.
                                    type: str
                                  items:
                                    description: Wired Network Devices Id Config Features
                                      Intended Layer2 Feature's items.
                                    elements: dict
                                    suboptions:
                                      configType:
                                        description: Type of network functionality
                                          configured for LACP Portchannel member port.
                                        type: str
                                      interfaceName:
                                        description: Interface name. The API /dna/intent/api/v1/interface/network-dev...
                                          can be used to get the list of interfaces
                                          on a device.
                                        type: str
                                      mode:
                                        description: Specify whether a port can send
                                          LACP packets or only receive LACP packets.
                                        type: str
                                      portPriority:
                                        description: Configures the LACP port priority.
                                          Corresponding CLI - lacp port-priority <0-65535>.
                                        type: int
                                      rate:
                                        description: Configures the rate at which
                                          LACP control packets are received by an
                                          LACP-supported interface. Corresponding
                                          CLI - lacp rate fast| normal.
                                        type: int
                                    type: list
                                type: dict
                              minLinks:
                                description: Specifies the minimum number of member
                                  ports that must be in the link-up state and bundled
                                  in the EtherChannel for the port channel interface
                                  to transition to the link-up state. Corresponding
                                  CLI - port-channel min-links <2-8>.
                                type: int
                              name:
                                description: Configures the channel group. Corresponding
                                  CLI - interface port-channel <1-128>.
                                type: str
                            type: dict
                          PagpPortchannelConfig:
                            description: Wired Network Devices Id Config Features
                              Intended Layer2 Feature's PagpPortchannelConfig.
                            suboptions:
                              configType:
                                description: Type of a Portchannel.
                                type: str
                              memberPorts:
                                description: Wired Network Devices Id Config Features
                                  Intended Layer2 Feature's memberPorts.
                                suboptions:
                                  configType:
                                    description: Type of member ports.
                                    type: str
                                  items:
                                    description: Wired Network Devices Id Config Features
                                      Intended Layer2 Feature's items.
                                    elements: dict
                                    suboptions:
                                      configType:
                                        description: Type of network functionality
                                          configured for Etherchannel member port.
                                        type: str
                                      interfaceName:
                                        description: Interface name. The API /dna/intent/api/v1/interface/network-dev...
                                          can be used to get the list of interfaces
                                          on a device.
                                        type: str
                                      learnMethod:
                                        description: Selects the PAgP learning method.
                                          Corresponding CLI - pagp learn-method aggregation
                                          port | physical port.
                                        type: str
                                      mode:
                                        description: Mode.
                                        type: str
                                      portPriority:
                                        description: Assigns a priority so that the
                                          selected port is chosen for packet transmission.
                                          Corresponding CLI - pagp port-priority <0-255>.
                                        type: int
                                    type: list
                                type: dict
                              minLinks:
                                description: Specifies the minimum number of member
                                  ports that must be in the link-up state and bundled
                                  in the EtherChannel for the port channel interface
                                  to transition to the link-up state. Corresponding
                                  CLI - port-channel min-links <2-8>.
                                type: int
                              name:
                                description: Configures the channel group. Corresponding
                                  CLI - interface port-channel <1-128>.
                                type: str
                            type: dict
                        type: dict
                    type: list
                type: dict
            type: list
        type: list
    type: dict
  stpGlobalConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      stpGlobalConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality configured for STP. Config
                  type STP_GLOBAL is for configuring the global settings for STP.
                type: str
              isBackboneFastEnabled:
                description: Enable BackboneFast to detect indirect link failures
                  and to start the STP reconfiguration sooner than it would under
                  normal spanning-tree rules. Corresponding CLI - spanning-tree backbonefast.default
                  false.
                type: bool
              isBpduFilterEnabled:
                description: Configure BPDU filtering. Enabling BPDU filtering on
                  PortFast edge-enabled interfaces keeps those interfaces that are
                  in a PortFast edge-operational state from sending or receiving BPDUs.
                  Corresponding CLI - spanning-tree portfast bpdufilter default.default
                  false.
                type: bool
              isBpduGuardEnabled:
                description: Configure BPDU guard. Enabling BPDU filtering on PortFast
                  edge-enabled interfaces spanning tree shuts down ports that are
                  in a PortFast edge-operational state if any BPDU is received on
                  them. Corresponding CLI - spanning-tree portfast bpduguard default.default
                  false.
                type: bool
              isEtherChannelGuardEnabled:
                description: Enable EtherChannel guard to detect an EtherChannel misconfiguration
                  between the switch and a connected device. A misconfiguration can
                  occur if the switch interfaces are configured in an EtherChannel,
                  but the interfaces on the other device are not. A misconfiguration
                  can also occur if the channel parameters are not the same at both
                  ends of the EtherChannel. Corresponding CLI - spanning-tree etherchannel
                  guard misconfig.default true.
                type: bool
              isExtendedSystemIdEnabled:
                description: Enable the extended-system ID updates the bridge IDs
                  of all active Spanning Tree Protocol (STP) instances, which might
                  change the spanning-tree topology. Corresponding CLI - spanning-tree
                  extend system-id.default true.
                type: bool
              isLoggingEnabled:
                description: Enable STP Logging. Corresponding CLI - spanning-tree
                  logging.default false.
                type: bool
              isLoopGuardEnabled:
                description: Configure loop guard to prevent alternate or root ports
                  from becoming designated ports because of a failure that leads to
                  a unidirectional link. Loop guard prevents alternate and root ports
                  from becoming designated ports, and spanning tree does not send
                  BPDUs on root or alternate ports. Corresponding CLI - spanning-tree
                  loopguard default.default false.
                type: bool
              isUplinkFastEnabled:
                description: Configure UplinkFast which provides fast convergence
                  after a direct link failure and achieves load-balancing between
                  redundant Layer 2 links using uplink groups. Corresponding CLI -
                  spanning-tree uplinkfast.default false.
                type: bool
              portFastMode:
                description: Configure portfast on ports so they are moved directly
                  to STP forwarding state without waiting for the standard forward-time
                  delay. Corresponding CLI - spanning-tree portfast default.
                type: str
              stpInstances:
                description: Wired Network Devices Id Config Features Intended Layer2
                  Feature's stpInstances.
                suboptions:
                  configType:
                    description: Type of STP VLAN instances.
                    type: str
                  items:
                    description: Wired Network Devices Id Config Features Intended
                      Layer2 Feature's items.
                    elements: dict
                    suboptions:
                      configType:
                        description: Type of network functionality under a feature.
                          Config type STP_VLAN is for configuring the per VLAN settings
                          for STP.
                        type: str
                      priority:
                        description: Configure the device priority of a VLAN. Corresponding
                          CLI - spanning-tree vlan <vlan-id> priority <0-61440>. Default
                          32768 multipleOf 4096.
                        type: int
                      timers:
                        description: Wired Network Devices Id Config Features Intended
                          Layer2 Feature's timers.
                        suboptions:
                          configType:
                            description: Type of network functionality under a feature.
                              Config type STP_TIMERS is for configuring the per-VLAN
                              timers for STP.
                            type: str
                          forwardDelay:
                            description: Configures the maximum-aging time of a VLAN.
                              The maximum-aging time is the number of seconds a switch
                              waits without receiving spanning-tree configuration
                              messages before attempting a reconfiguration. Corresponding
                              CLI - spanning-tree vlan <vlan-id> max-age <6-40>.
                            type: int
                          helloInterval:
                            description: Configure the hello time of a VLAN. The hello
                              time is the time interval between configuration messages
                              that are generated and sent by the root switch. These
                              messages mean that the switch is alive. Corresponding
                              CLI - spanning-tree vlan <vlan-id> hello-time <1-10>.
                            type: int
                          isStpEnabled:
                            description: Enable STP on the VLAN. Corresponding CLI
                              - spanning-tree vlan <vlan-id>. Default true.
                            type: bool
                          maxAge:
                            description: Configure the maximum-aging time of a VLAN.
                              The maximum-aging time is the number of seconds a switch
                              waits without receiving spanning-tree configuration
                              messages before attempting a reconfiguration. Corresponding
                              CLI - spanning-tree vlan <vlan-id> max-age <6-40>.default
                              20.
                            type: int
                        type: dict
                      vlanId:
                        description: VLAN ID for which STP is configured.
                        type: int
                    type: list
                type: dict
              stpMode:
                description: Configure the STP mode. Corresponding CLI - spanning-tree
                  mode mst | pvst | rapid-pvst. PVST - Per-VLAN Spanning Tree (PVST)
                  mode is based on the IEEE 802.1D standard and Cisco proprietary
                  extensions. The PVST+ runs on each VLAN on the device up to the
                  maximum supported, ensuring that each has a loop-free path through
                  the network. RSTP - Rapid per-VLAN Spanning Tree Plus (RSTP) mode
                  is the same as PVST+ except that is uses a rapid convergence based
                  on the IEEE 802.1w standard. MST - Multiple Spanning Tree (MST)
                  mode is based on the IEEE 802.1s standard. You can map multiple
                  VLANs to the same spanning-tree instance, which reduces the number
                  of spanning-tree instances that are required to support many VLANs.
                type: str
              transmitHoldCount:
                description: Configure the BPDU burst size by changing the transmit
                  hold count value. Corresponding CLI - spanning-tree transmit hold-count
                  <1-20>.default 6.
                type: int
              uplinkFastMaxUpdateRate:
                description: Configure the STP Uplink Fast Max Update Rate to change
                  the rate at which update packets are sent. Corresponding CLI - spanning-tree
                  uplinkfast max-update-rate <0-32000>.
                type: int
            type: list
        type: list
    type: dict
  stpInterfaceConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      stpInterfaceConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: dict
        suboptions:
          bpduFilter:
            description: Configure BPDU filtering on a port. Enabling BPDU filtering
              on PortFast edge-enabled port keeps the port from sending or receiving
              BPDUs. Corresponding CLI - spanning-tree bpduguard enable | disable.
            type: str
          bpduGuard:
            description: Configures BPDU guard. When BPDU filtering is enabled on
              PortFast edge-enabled port, spanning tree shuts down the port if any
              BPDU is received on it.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type
              STP_INTERFACE is for configuring STP on an interface.
            type: str
          guardMode:
            description: Enable loop guard or root guard on the interface. Corresponding
              CLI - spanning-tree guard loop | none | root. LOOP - Enables loop guard
              on the interface. ROOT - Enables root guard on the interface.
            type: str
          interfaceName:
            description: Interface name. The API /intent/api/v1/interface/network-device/{deviceId}
              can be used to get the list of interfaces on a device.example GigabitEthernet1/0/1.
            type: str
          pathCost:
            description: Configure the cost for an interface. Corresponding CLI -
              spanning-tree cost <1-200000000>.
            type: int
          portFastMode:
            description: Configure the portFast mode for an interface. Corresponding
              CLI - spanning-tree portfast disable | trunk | network | edge | edge
              trunk. DISABLE - Disable portFast for this interface. EDGE - Enable
              edge behavior on a Layer 2 access port connected to an end workstation
              or server. EDGE_TRUNK - Enable edge behavior on a trunk port. Use this
              keyword if the link is a trunk. NETWORK - Configure the port as a network
              port. Ports that are connected to Layer 2 switches and bridges can be
              configured as network ports. If Bridge Assurance is enabled globally,
              it automatically gets enabled on a spanning tree network port. TRUNK
              - Enable portfast on a trunk port.
            type: str
          portVlanCostSettings:
            description: Wired Network Devices Id Config Features Intended Layer2
              Feature's portVlanCostSettings.
            suboptions:
              configType:
                description: Type of STP Cost Settings.
                type: str
              items:
                description: Wired Network Devices Id Config Features Intended Layer2
                  Feature's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config
                      type STP_INTERFACE_VLAN_COST is for configuring per VLAN cost
                      on an interface.
                    type: str
                  cost:
                    description: Configure the cost for the VLANs. Corresponding CLI
                      - spanning-tree vlan cost <1-200000000>.
                    type: int
                  vlans:
                    description: VLANs can be comma separated and/or a range like
                      '2,4-5,7,10-20'.
                    type: str
                type: list
            type: dict
          portVlanPrioritySettings:
            description: Wired Network Devices Id Config Features Intended Layer2
              Feature's portVlanPrioritySettings.
            suboptions:
              configType:
                description: Type of STP Priority Settings.
                type: str
              items:
                description: Wired Network Devices Id Config Features Intended Layer2
                  Feature's items.
                elements: dict
                suboptions:
                  configType:
                    description: ConfigType.
                    type: str
                  priority:
                    description: Configures the port priority for the VLANs. Corresponding
                      CLI - spanning-tree vlan port-priority <0-240>.multipleOf 16.
                    type: int
                  vlans:
                    description: VLANs can be comma separated and/or a range like
                      '2,4-5,7,10-20'.
                    type: str
                type: list
            type: dict
          priority:
            description: Configures port priority for an interface. If a loop occurs,
              spanning tree uses port priority when selecting an interface to put
              into the forwarding state. Assign higher priority values (lower numerical
              values) to interfaces that you want selected first and lower priority
              values (higher numerical values) that you want selected last. If all
              interfaces have the same priority value, spanning tree puts the interface
              with the lowest interface number in the forwarding state and blocks
              the other interfaces. Corresponding CLI - spanning-tree port-priority
              <0-240>.multipleOf 16.
            type: int
        type: list
    type: dict
  switchportInterfaceConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      switchportInterfaceConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              accessVlan:
                description: Set the VLAN for untagged traffic when the interface
                  is in access mode. Corresponding CLI - switchport access vlan <1-4094>.
                type: int
              adminStatus:
                description: Configured the admin state of the interface as either
                  'UP' or 'DOWN'. Corresponding CLI - no shutdown.default UP.
                type: str
              configType:
                description: Type of network functionality under a feature. Config
                  type SWITCHPORT_INTERFACE is for configuring switchport settings
                  on an interface.
                type: str
              description:
                description: Configure the description of the interface. It cannot
                  include non-ASCII characters. Corresponding CLI - description .
                type: str
              interfaceName:
                description: Interface name. The API /intent/api/v1/interface/network-device/{deviceId}
                  can be used to get the list of interfaces on a device.example GigabitEthernet1/0/1.
                type: str
              mode:
                description: Set the administrative mode for the interface. Corresponding
                  CLI - switchport mode access | trunk | dynamic auto | dynamic desirable
                  | dot1q-tunnel .
                type: str
              nativeVlan:
                description: Set the native VLAN for IEEE 802.1Q trunks. Corresponding
                  CLI - switchport trunk native vlan <1-4094>.
                type: int
              trunkAllowedVlans:
                description: Configure the list of VLANs allowed on a trunk interface.
                  Allowed VLANs should be between 1 and 4094. VLANs can be comma separated
                  and/or a range like '2,4-5,7,10-20'. Corresponding CLI - switchport
                  trunk allowed vlan 10, 20, 21-24 | all | none.
                type: str
              voiceVlan:
                description: Enable the access port to carry IP voice traffic from
                  an IP phone. All voice traffic is on the specified VLAN. Corresponding
                  CLI - switchport voice vlan <1-4094>.
                type: int
            type: list
        type: list
    type: dict
  trunkInterfaceConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      trunkInterfaceConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config
                  type TRUNK_INTERFACE is for configuring trunk settings on an interface.
                type: str
              interfaceName:
                description: Interface name. The API /intent/api/v1/interface/network-device/{deviceId}
                  can be used to get the list of interfaces on a device.
                type: str
              isDtpNegotiationEnabled:
                description: Configure whether or not the interface supports negotiation
                  of the trunk encapsulation. The switchport nonegotiate command is
                  issued to prevent DTP (negotiation) packets from being sent out
                  the interface. Corresponding CLI - switchport nonegotiate. Default
                  true.
                type: bool
              isProtected:
                description: A protected port does not forward any traffic (unicast,
                  multicast, or broadcast) to any other port that is also a protected
                  port. Data traffic cannot be forwarded between protected ports at
                  Layer 2; all data traffic passing between protected ports must be
                  forwarded through a Layer 3 device. Forwarding behavior between
                  a protected port and a non-protected port proceeds as usual. Corresponding
                  CLI - switchport protected.default false.
                type: bool
              pruneEligibleVlans:
                description: Configure the prune eligibility list. By default, all
                  VLANs are allowed on a trunk and all VLANs (between 2 and 1001,
                  inclusive) are eligible for pruning if pruning is enabled globally
                  with the vtp pruning command. If a prune eligibility list is configured,
                  then only those VLANs on the list are eligible for pruning. Corresponding
                  CLI - switchport trunk pruning vlan 10, 20, 21-24 | none.
                type: str
            type: list
        type: list
    type: dict
  vlanConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      vlanConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality configured for VLAN. Config
                  type VLAN is for configuring VLANs.
                type: str
              isVlanEnabled:
                description: Enables or disables the VLAN switching. Corresponding
                  CLI - shutdown. Default true.
                type: bool
              name:
                description: Configure the name of the VLAN. VTP version VTPv1 and
                  VTPv2 supports VLAN name of 32 character length, VTP version VTPv3
                  supports up to 128 characters. The recommended name length is 20
                  characters. If no name is entered for the VLAN, the default is to
                  append the VLAN ID with leading zeros to the word VLAN. For example,
                  VLAN0004 is a default VLAN name for VLAN 4. Corresponding CLI -
                  name <vlan-name>. Example iot_vlan.
                type: str
              vlanId:
                description: VLAN ID is the identifier for a VLAN.
                type: int
            type: list
        type: list
    type: dict
  vtpGlobalConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      vtpGlobalConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality configured for VTP. Config
                  type VTP_GLOBAL is for configuring the global settings for VTP.
                type: str
              configurationFileName:
                description: Configures the ASCII filename of the IFS file system
                  file where the VTP configuration is stored. By default, it is stored
                  in the vlan.dat file. Corresponding CLI - vtp filename <file-name>.example
                  flash saved_vtp_config.
                type: str
              domainName:
                description: Configures the VTP administrative domain name. Global
                  VLAN configuration changes are propagated to the devices that have
                  the same VTP domain name. When the domain name is not specified,
                  VLAN information is not propagated over the network. Once the domain
                  name is configured, it cannot be deleted; it can only be changed.
                  Devices in VTP transparent mode do not exchange VTP messages with
                  other devices, so a VTP domain name does not need to be configured
                  for them. Corresponding CLI - vtp domain <domain-name>.
                type: str
              isPruningEnabled:
                description: Enables pruning in the VTP administrative domain. VTP
                  pruning blocks unneeded flooded traffic for prune-eligible VLANs
                  on trunk ports. It increases network available bandwidth by restricting
                  flooded traffic to those trunk links that the traffic must use to
                  reach the destination devices. VLAN 1 and VLANs 1002 to 1005 are
                  always pruning-ineligible; traffic from these VLANs cannot be pruned.
                  Extended-range VLANs (VLAN IDs higher than 1005) are also pruning-ineligible.
                  VTP pruning can be configured only on a VTP server. Corresponding
                  CLI - vtp pruning.default false.
                type: bool
              mode:
                description: Configures the device for VTP mode. Corresponding CLI
                  - vtp mode. SERVER - Any VLAN configuration changes in this mode
                  are propagated to all devices in the VTP domain. VTP servers advertise
                  their VLAN configurations to other devices in the same VTP domain
                  and synchronize their VLAN configurations with other devices based
                  on advertisements received over trunk links. CLIENT - VLANs cannot
                  be configured in this mode but VTP updates are transmitted as well
                  as received. TRANSPARENT - VLANs can be configured in this mode
                  but the changes are not sent to other devices in the domain, and
                  they affect only the individual device. VTP updates are not generated
                  but the received updates are forwarded. However, in VTP version
                  2 or version 3, transparent devices do forward VTP advertisements
                  that they receive from other devices. OFF - VLANs can be configured
                  in this mode but VTP updates are neither generated nor forwarded.
                type: str
              sourceInterface:
                description: Configures an interface as the preferred source for VTP
                  updates from this device. The IP address of the specified interface
                  becomes the VTP IP updater address, and can be used to determine
                  which VTP server last updated the VLAN database in the VTP domain.
                  Corresponding CLI - vtp interface <interface-name>.example GigabitEthernet1/0/1.
                type: str
              version:
                description: Configures VTP version on the device. Corresponding CLI
                  - vtp version. VERSION_2 supports unrecognized TLV. VERSION_3 supports
                  primary and secondary servers, private VLANs, propagation of extended
                  VLANs (VLAN IDs 1006-4094), propagation of Multiple Spanning Tree
                  (MST) information. VTP domain name needs to be configured for VTP
                  version 3.
                type: str
            type: list
        type: list
    type: dict
  vtpInterfaceConfig:
    description: Wired Network Devices Id Config Features Intended Layer2 Feature's
      vtpInterfaceConfig.
    suboptions:
      items:
        description: Wired Network Devices Id Config Features Intended Layer2 Feature's
          items.
        elements: list
        suboptions:
          - description: Wired Network Devices Id Config Features Intended Layer2
              Feature's items.
            elements: dict
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config
                  type VTP_INTERFACE is for configuring VTP in an interface.
                type: str
              interfaceName:
                description: Interface name. The API /intent/api/v1/interface/network-device/{deviceId}
                  can be used to get the list of interfaces on a device.example GigabitEthernet1/0/1.
                type: str
              isVtpEnabled:
                description: Enables or disables VTP per interface. When VTP is disabled
                  on a trunk interface, it drops incoming VTP packets and prevents
                  VTP advertisements on this particular trunk. Corresponding CLI -
                  vtp. Default true.
                type: bool
            type: list
        type: list
    type: dict
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wired CreateConfigurationsForAnIntendedLayer2FeatureOnAWiredDeviceV1
    description: Complete reference of the CreateConfigurationsForAnIntendedLayer2FeatureOnAWiredDeviceV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!create-configurations-for-an-intended-layer-2-feature-on-a-wired-device
  - name: Cisco DNA Center documentation for Wired DeleteConfigurationsForAnIntendedLayer2FeatureOnAWiredDeviceV1
    description: Complete reference of the DeleteConfigurationsForAnIntendedLayer2FeatureOnAWiredDeviceV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-an-intended-layer-2-feature-on-a-wired-device
  - name: Cisco DNA Center documentation for Wired UpdateConfigurationsForAnIntendedLayer2FeatureOnAWiredDeviceV1
    description: Complete reference of the UpdateConfigurationsForAnIntendedLayer2FeatureOnAWiredDeviceV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!update-configurations-for-an-intended-layer-2-feature-on-a-wired-device
notes:
  - SDK Method used are
    wired.Wired.create_configurations_for_an_intended_layer2_feature_on_a_wired_device_v1,
    wired.Wired.delete_configurations_for_an_intended_layer2_feature_on_a_wired_device_v1,
    wired.Wired.update_configurations_for_an_intended_layer2_feature_on_a_wired_device_v1,
  - Paths used are post
    /dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2/{feature},
    delete
    /dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2/{feature},
    put
    /dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2/{feature},
  - It should be noted that this module is an alias of wired_network_devices_id_config_features_intended_layer2_feature_v1
"""
EXAMPLES = r"""
- name: Delete by id
  cisco.dnac.wired_network_devices_id_config_features_intended_layer2_feature:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    feature: string
    id: string
- name: Update by id
  cisco.dnac.wired_network_devices_id_config_features_intended_layer2_feature:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cdpGlobalConfig:
      items:
        -   - configType: string
              holdTime: 0
              isAdvertiseV2Enabled: true
              isCdpEnabled: true
              isLogDuplexMismatchEnabled: true
              timer: 0
    cdpInterfaceConfig:
      items:
        -   - configType: string
              interfaceName: string
              isCdpEnabled: true
              isLogDuplexMismatchEnabled: true
    dhcpSnoopingGlobalConfig:
      items:
        -   - configType: string
              databaseAgent:
                agentUrl: string
                configType: string
                timeout: 0
                writeDelay: 0
              dhcpSnoopingVlans: string
              isDhcpSnoopingEnabled: true
              isGleaningEnabled: true
              proxyBridgeVlans: string
    dhcpSnoopingInterfaceConfig:
      items:
        -   - configType: string
              interfaceName: string
              isTrustedInterface: true
              messageRateLimit: 0
    dot1xGlobalConfig:
      items:
        -   - authenticationConfigMode: string
              configType: string
              isDot1xEnabled: true
    dot1xInterfaceConfig:
      items:
        -   - authenticationOrder:
                configType: string
                items:
                  - string
              configType: string
              interfaceName: string
    feature: string
    id: string
    igmpSnoopingGlobalConfig:
      items:
        -   - configType: string
              igmpSnoopingVlanSettings:
                configType: string
                items:
                  - configType: string
                    igmpSnoopingVlanMrouters:
                      configType: string
                      items:
                        - configType: string
                          interfaceName: string
                    isIgmpSnoopingEnabled: true
                    isImmediateLeaveEnabled: true
                    isQuerierEnabled: true
                    querierAddress: string
                    querierQueryInterval: 0
                    querierVersion: string
                    vlanId: 0
              isIgmpSnoopingEnabled: true
              isQuerierEnabled: true
              querierAddress: string
              querierQueryInterval: 0
              querierVersion: string
    lldpGlobalConfig:
      items:
        -   - configType: string
              holdTime: 0
              isLldpEnabled: true
              reinitializationDelay: 0
              timer: 0
    lldpInterfaceConfig:
      items:
        -   - adminStatus: string
              configType: string
              interfaceName: string
    mabInterfaceConfig:
      items:
        -   - configType: string
              interfaceName: string
              isMabEnabled: true
    mldSnoopingGlobalConfig:
      items:
        -   - configType: string
              isMldSnoopingEnabled: true
              isQuerierEnabled: true
              isSuppressListenerMessagesEnabled: true
              mldSnoopingVlanSettings:
                configType: string
                items:
                  - configType: string
                    isImmediateLeaveEnabled: true
                    isMldSnoopingEnabled: true
                    isQuerierEnabled: true
                    mldSnoopingVlanMrouters:
                      configType: string
                      items:
                        - configType: string
                          interfaceName: string
                    querierAddress: string
                    querierQueryInterval: 0
                    querierVersion: string
                    vlanId: 0
              querierAddress: string
              querierQueryInterval: 0
              querierVersion: string
    portChannelConfig:
      items:
        -   - configType: string
              isAutoEnabled: true
              lacpSystemPriority: 0
              loadBalancingMethod: string
              portchannels:
                configType: string
                items:
                  - AnyOf:
                      EtherchannelConfig:
                        configType: string
                        memberPorts:
                          configType: string
                          items:
                            - configType: string
                              interfaceName: string
                              mode: string
                        minLinks: 0
                        name: string
                      LacpPortchannelConfig:
                        configType: string
                        memberPorts:
                          configType: string
                          items:
                            - configType: string
                              interfaceName: string
                              mode: string
                              portPriority: 0
                              rate: 0
                        minLinks: 0
                        name: string
                      PagpPortchannelConfig:
                        configType: string
                        memberPorts:
                          configType: string
                          items:
                            - configType: string
                              interfaceName: string
                              learnMethod: string
                              mode: string
                              portPriority: 0
                        minLinks: 0
                        name: string
    stpGlobalConfig:
      items:
        -   - configType: string
              isBackboneFastEnabled: true
              isBpduFilterEnabled: true
              isBpduGuardEnabled: true
              isEtherChannelGuardEnabled: true
              isExtendedSystemIdEnabled: true
              isLoggingEnabled: true
              isLoopGuardEnabled: true
              isUplinkFastEnabled: true
              portFastMode: string
              stpInstances:
                configType: string
                items:
                  - configType: string
                    priority: 0
                    timers:
                      configType: string
                      forwardDelay: 0
                      helloInterval: 0
                      isStpEnabled: true
                      maxAge: 0
                    vlanId: 0
              stpMode: string
              transmitHoldCount: 0
              uplinkFastMaxUpdateRate: 0
    stpInterfaceConfig:
      items:
        - bpduFilter: string
          bpduGuard: string
          configType: string
          guardMode: string
          interfaceName: string
          pathCost: 0
          portFastMode: string
          portVlanCostSettings:
            configType: string
            items:
              - configType: string
                cost: 0
                vlans: string
          portVlanPrioritySettings:
            configType: string
            items:
              - configType: string
                priority: 0
                vlans: string
          priority: 0
    switchportInterfaceConfig:
      items:
        -   - accessVlan: 0
              adminStatus: string
              configType: string
              description: string
              interfaceName: string
              mode: string
              nativeVlan: 0
              trunkAllowedVlans: string
              voiceVlan: 0
    trunkInterfaceConfig:
      items:
        -   - configType: string
              interfaceName: string
              isDtpNegotiationEnabled: true
              isProtected: true
              pruneEligibleVlans: string
    vlanConfig:
      items:
        -   - configType: string
              isVlanEnabled: true
              name: string
              vlanId: 0
    vtpGlobalConfig:
      items:
        -   - configType: string
              configurationFileName: string
              domainName: string
              isPruningEnabled: true
              mode: string
              sourceInterface: string
              version: string
    vtpInterfaceConfig:
      items:
        -   - configType: string
              interfaceName: string
              isVtpEnabled: true
- name: Create
  cisco.dnac.wired_network_devices_id_config_features_intended_layer2_feature:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cdpGlobalConfig:
      items:
        -   - configType: string
              holdTime: 0
              isAdvertiseV2Enabled: true
              isCdpEnabled: true
              isLogDuplexMismatchEnabled: true
              timer: 0
    cdpInterfaceConfig:
      items:
        -   - configType: string
              interfaceName: string
              isCdpEnabled: true
              isLogDuplexMismatchEnabled: true
    dhcpSnoopingGlobalConfig:
      items:
        -   - configType: string
              databaseAgent:
                agentUrl: string
                configType: string
                timeout: 0
                writeDelay: 0
              dhcpSnoopingVlans: string
              isDhcpSnoopingEnabled: true
              isGleaningEnabled: true
              proxyBridgeVlans: string
    dhcpSnoopingInterfaceConfig:
      items:
        -   - configType: string
              interfaceName: string
              isTrustedInterface: true
              messageRateLimit: 0
    dot1xGlobalConfig:
      items:
        -   - authenticationConfigMode: string
              configType: string
              isDot1xEnabled: true
    dot1xInterfaceConfig:
      items:
        -   - authenticationOrder:
                configType: string
                items:
                  - string
              configType: string
              interfaceName: string
    feature: string
    id: string
    igmpSnoopingGlobalConfig:
      items:
        -   - configType: string
              igmpSnoopingVlanSettings:
                configType: string
                items:
                  - configType: string
                    igmpSnoopingVlanMrouters:
                      configType: string
                      items:
                        - configType: string
                          interfaceName: string
                    isIgmpSnoopingEnabled: true
                    isImmediateLeaveEnabled: true
                    isQuerierEnabled: true
                    querierAddress: string
                    querierQueryInterval: 0
                    querierVersion: string
                    vlanId: 0
              isIgmpSnoopingEnabled: true
              isQuerierEnabled: true
              querierAddress: string
              querierQueryInterval: 0
              querierVersion: string
    lldpGlobalConfig:
      items:
        -   - configType: string
              holdTime: 0
              isLldpEnabled: true
              reinitializationDelay: 0
              timer: 0
    lldpInterfaceConfig:
      items:
        -   - adminStatus: string
              configType: string
              interfaceName: string
    mabInterfaceConfig:
      items:
        -   - configType: string
              interfaceName: string
              isMabEnabled: true
    mldSnoopingGlobalConfig:
      items:
        -   - configType: string
              isMldSnoopingEnabled: true
              isQuerierEnabled: true
              isSuppressListenerMessagesEnabled: true
              mldSnoopingVlanSettings:
                configType: string
                items:
                  - configType: string
                    isImmediateLeaveEnabled: true
                    isMldSnoopingEnabled: true
                    isQuerierEnabled: true
                    mldSnoopingVlanMrouters:
                      configType: string
                      items:
                        - configType: string
                          interfaceName: string
                    querierAddress: string
                    querierQueryInterval: 0
                    querierVersion: string
                    vlanId: 0
              querierAddress: string
              querierQueryInterval: 0
              querierVersion: string
    portChannelConfig:
      items:
        -   - configType: string
              isAutoEnabled: true
              lacpSystemPriority: 0
              loadBalancingMethod: string
              portchannels:
                configType: string
                items:
                  - AnyOf:
                      EtherchannelConfig:
                        configType: string
                        memberPorts:
                          configType: string
                          items:
                            - configType: string
                              interfaceName: string
                              mode: string
                        minLinks: 0
                        name: string
                      LacpPortchannelConfig:
                        configType: string
                        memberPorts:
                          configType: string
                          items:
                            - configType: string
                              interfaceName: string
                              mode: string
                              portPriority: 0
                              rate: 0
                        minLinks: 0
                        name: string
                      PagpPortchannelConfig:
                        configType: string
                        memberPorts:
                          configType: string
                          items:
                            - configType: string
                              interfaceName: string
                              learnMethod: string
                              mode: string
                              portPriority: 0
                        minLinks: 0
                        name: string
    stpGlobalConfig:
      items:
        -   - configType: string
              isBackboneFastEnabled: true
              isBpduFilterEnabled: true
              isBpduGuardEnabled: true
              isEtherChannelGuardEnabled: true
              isExtendedSystemIdEnabled: true
              isLoggingEnabled: true
              isLoopGuardEnabled: true
              isUplinkFastEnabled: true
              portFastMode: string
              stpInstances:
                configType: string
                items:
                  - configType: string
                    priority: 0
                    timers:
                      configType: string
                      forwardDelay: 0
                      helloInterval: 0
                      isStpEnabled: true
                      maxAge: 0
                    vlanId: 0
              stpMode: string
              transmitHoldCount: 0
              uplinkFastMaxUpdateRate: 0
    stpInterfaceConfig:
      items:
        - bpduFilter: string
          bpduGuard: string
          configType: string
          guardMode: string
          interfaceName: string
          pathCost: 0
          portFastMode: string
          portVlanCostSettings:
            configType: string
            items:
              - configType: string
                cost: 0
                vlans: string
          portVlanPrioritySettings:
            configType: string
            items:
              - configType: string
                priority: 0
                vlans: string
          priority: 0
    switchportInterfaceConfig:
      items:
        -   - accessVlan: 0
              adminStatus: string
              configType: string
              description: string
              interfaceName: string
              mode: string
              nativeVlan: 0
              trunkAllowedVlans: string
              voiceVlan: 0
    trunkInterfaceConfig:
      items:
        -   - configType: string
              interfaceName: string
              isDtpNegotiationEnabled: true
              isProtected: true
              pruneEligibleVlans: string
    vlanConfig:
      items:
        -   - configType: string
              isVlanEnabled: true
              name: string
              vlanId: 0
    vtpGlobalConfig:
      items:
        -   - configType: string
              configurationFileName: string
              domainName: string
              isPruningEnabled: true
              mode: string
              sourceInterface: string
              version: string
    vtpInterfaceConfig:
      items:
        -   - configType: string
              interfaceName: string
              isVtpEnabled: true
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""

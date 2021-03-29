#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Rafael Campos <rcampos@altus.cr>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_wireless_info
short_description: Manage NetworkDeviceWirelessInfo objects of Devices
description:
- Returns the wireless lan controller info with given device ID.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  id:
    description:
    - Device ID.
    type: str
    required: True

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.network_device_wireless_info
# Reference by Internet resource
- name: NetworkDeviceWirelessInfo reference
  description: Complete reference of the NetworkDeviceWirelessInfo object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: NetworkDeviceWirelessInfo reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
"""

EXAMPLES = r"""
- name: get_wireless_lan_controller_details_by_id
  cisco.dnac.network_device_wireless_info:
    state: query  # required
    id: SomeValue  # string, required
  register: query_result

"""

RETURN = """
"""

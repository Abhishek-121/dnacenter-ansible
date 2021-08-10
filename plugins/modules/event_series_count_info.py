#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_series_count_info
short_description: Information module for Event Series Count
description:
- Get all Event Series Count.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  eventIds:
    description:
    - EventIds query parameter. The registered EventId should be provided.
    type: str
  startTime:
    description:
    - StartTime query parameter. Start Time in milliseconds.
    type: int
  endTime:
    description:
    - EndTime query parameter. End Time in milliseconds.
    type: int
  category:
    description:
    - Category query parameter.
    type: str
  type:
    description:
    - Type query parameter.
    type: str
  severity:
    description:
    - Severity query parameter.
    type: str
  domain:
    description:
    - Domain query parameter.
    type: str
  subDomain:
    description:
    - SubDomain query parameter. Sub Domain.
    type: str
  source:
    description:
    - Source query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Event Series Count reference
  description: Complete reference of the Event Series Count object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Event Series Count
  cisco.dnac.event_series_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    eventIds: string
    startTime: 0
    endTime: 0
    category: string
    type: string
    severity: string
    domain: string
    subDomain: string
    source: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: str
  sample: >
    "string"
"""
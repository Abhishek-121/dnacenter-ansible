#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, first last <email>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: device_detail
short_description: Manage DeviceDetail objects of Devices
description:
- Returns detailed Network Device information retrieved by Mac Address, Device Name or UUID for any given point of time.
version_added: '1.0'
author: first last (@GitHubID)
options:
    identifier:
        description:
        - One of keywords : macAddress or uuid or nwDeviceName.
        type: str
    search_by:
        description:
        - MAC Address or Device Name value or UUID of the network device.
        type: str
    timestamp:
        description:
        - Epoch time(in milliseconds) when the device data is required.
        type: int

requirements:
- dnacentersdk
seealso:
# Reference by module name
- module: cisco.dnac.plugins.module_utils.definitions.device_detail
# Reference by Internet resource
- name: DeviceDetail reference
  description: Complete reference of the DeviceDetail object model.
  link: https://developer.cisco.com/docs/dna-center/api/1-3-3-x
# Reference by Internet resource
- name: DeviceDetail reference
  description: SDK reference.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v2-1-1-summary
'''

EXAMPLES = r'''
'''

RETURN = r'''
data_0:
    description: Returns detailed Network Device information retrieved by Mac Address, Device Name or UUID for any given point of time.
    returned: success,changed,always
    type: dict
    contains:
        response:
            description: Response, property of the response body.
            returned: success,changed,always
            type: dict
            contains:
                HALastResetReason:
                    description: It is the device detail's HALastResetReason.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                managementIpAddr:
                    description: It is the device detail's managementIpAddr.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                HAPrimaryPowerStatus:
                    description: It is the device detail's HAPrimaryPowerStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                redundancyMode:
                    description: It is the device detail's redundancyMode.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                communicationState:
                    description: It is the device detail's communicationState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nwDeviceName:
                    description: It is the device detail's nwDeviceName.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                redundancyUnit:
                    description: It is the device detail's redundancyUnit.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                platformId:
                    description: It is the device detail's platformId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                redundancyPeerState:
                    description: It is the device detail's redundancyPeerState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nwDeviceId:
                    description: It is the device detail's nwDeviceId.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                redundancyState:
                    description: It is the device detail's redundancyState.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nwDeviceRole:
                    description: It is the device detail's nwDeviceRole.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nwDeviceFamily:
                    description: It is the device detail's nwDeviceFamily.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                macAddress:
                    description: It is the device detail's macAddress.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                collectionStatus:
                    description: It is the device detail's collectionStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                deviceSeries:
                    description: It is the device detail's deviceSeries.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                osType:
                    description: It is the device detail's osType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                clientCount:
                    description: It is the device detail's clientCount.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                HASecondaryPowerStatus:
                    description: It is the device detail's HASecondaryPowerStatus.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                softwareVersion:
                    description: It is the device detail's softwareVersion.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                nwDeviceType:
                    description: It is the device detail's nwDeviceType.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                overallHealth:
                    description: It is the device detail's overallHealth.
                    returned: success,changed,always
                    type: int
                    sample: 0
                memoryScore:
                    description: It is the device detail's memoryScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                cpuScore:
                    description: It is the device detail's cpuScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                noiseScore:
                    description: It is the device detail's noiseScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                utilizationScore:
                    description: It is the device detail's utilizationScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                airQualityScore:
                    description: It is the device detail's airQualityScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                interferenceScore:
                    description: It is the device detail's interferenceScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                wqeScore:
                    description: It is the device detail's wqeScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                freeMbufScore:
                    description: It is the device detail's freeMbufScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                packetPoolScore:
                    description: It is the device detail's packetPoolScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                freeTimerScore:
                    description: It is the device detail's freeTimerScore.
                    returned: success,changed,always
                    type: int
                    sample: 0
                memory:
                    description: It is the device detail's memory.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                cpu:
                    description: It is the device detail's cpu.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                noise:
                    description: It is the device detail's noise.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                utilization:
                    description: It is the device detail's utilization.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                airQuality:
                    description: It is the device detail's airQuality.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                interference:
                    description: It is the device detail's interference.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                wqe:
                    description: It is the device detail's wqe.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                freeMbuf:
                    description: It is the device detail's freeMbuf.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                packetPool:
                    description: It is the device detail's packetPool.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                freeTimer:
                    description: It is the device detail's freeTimer.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                location:
                    description: It is the device detail's location.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'
                timestamp:
                    description: It is the device detail's timestamp.
                    returned: success,changed,always
                    type: str
                    sample: 'sample_string'


'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import ModuleDefinition, DNACModule, dnac_argument_spec
from ansible_collections.cisco.dnac.plugins.module_utils.definitions.device_detail import module_definition


def main():

    moddef = ModuleDefinition(module_definition)

    argument_spec = dnac_argument_spec()
    argument_spec.update(moddef.get_argument_spec_dict())

    required_if = moddef.get_required_if_list()
    
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        required_if=required_if
    )

    dnac = DNACModule(module, moddef)

    state = module.params.get("state")

    if state == "query":
        dnac.exec("get")

    dnac.exit_json()


if __name__ == "__main__":
    main()
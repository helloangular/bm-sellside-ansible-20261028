#!/usr/bin/env python3
# STAND-IN inventory for BlueMatrix's ${INVENTORY_SCRIPT} (./inventory/ec2.py): one local Docker
# container per catalog environment. Replace with BlueMatrix's real ops/ansible.git inventory.
import json, sys
groups = {
 "sellside_prd_eu": "bm-sellside-ss-prd-ams-target",
 "sellside_prd_na": "bm-sellside-ss-prd-nj-target",
 "sellside_preprd_au": "bm-sellside-ss-preprd-apse2-target",
 "sellside_preprd_eu": "bm-sellside-ss-preprd-ams-target",
 "sellside_preprd_na": "bm-sellside-ss-preprd-ny-target",
 "sellside_qa_na": "bm-sellside-ss-qa-ny-target",
 "sellside_reporting_backend_prd_eu": "bm-sellside-reporting-ss-prd-ams-target",
 "sellside_reporting_backend_prd_na": "bm-sellside-reporting-ss-prd-nj-target",
 "sellside_reporting_backend_preprd_au": "bm-sellside-reporting-ss-preprd-apse2-target",
 "sellside_reporting_backend_preprd_eu": "bm-sellside-reporting-ss-preprd-ams-target",
 "sellside_reporting_backend_preprd_na": "bm-sellside-reporting-ss-preprd-ny-target",
 "sellside_reporting_backend_qa_na": "bm-sellside-reporting-ss-qa-ny-target"
}
inv = {g: {'hosts': [h]} for g, h in groups.items()}
inv['haproxy'] = {'hosts': []}
inv['_meta'] = {'hostvars': {
 "bm-sellside-reporting-ss-prd-ams-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-reporting-ss-prd-ams"
 },
 "bm-sellside-reporting-ss-prd-nj-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-reporting-ss-prd-nj"
 },
 "bm-sellside-reporting-ss-preprd-ams-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-reporting-ss-preprd-ams"
 },
 "bm-sellside-reporting-ss-preprd-apse2-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-reporting-ss-preprd-apse2"
 },
 "bm-sellside-reporting-ss-preprd-ny-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-reporting-ss-preprd-ny"
 },
 "bm-sellside-reporting-ss-qa-ny-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-reporting-ss-qa-ny"
 },
 "bm-sellside-ss-prd-ams-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-ss-prd-ams"
 },
 "bm-sellside-ss-prd-nj-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-ss-prd-nj"
 },
 "bm-sellside-ss-preprd-ams-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-ss-preprd-ams"
 },
 "bm-sellside-ss-preprd-apse2-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-ss-preprd-apse2"
 },
 "bm-sellside-ss-preprd-ny-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-ss-preprd-ny"
 },
 "bm-sellside-ss-qa-ny-target": {
  "ansible_connection": "local",
  "ansible_python_interpreter": "/usr/local/ansible/bin/python3",
  "target_container": "bm-sellside-ss-qa-ny"
 }
}}
print(json.dumps(inv if '--list' in sys.argv else {}))

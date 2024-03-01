# module_plan_stash

A role to handle the base64 encoding or decoding of a terraform plan file using cloud.terraform.plan_stash module.

## Role Variables

Name | Description | Type | Default | Required
--- | --- | --- | --- | ---
module_plan_stash_operation|Whether to base64-encode the terraform plan file and saves it into ansible stats or base64-decode data from variable/binary_data to create a terraform plan file or apply the specific terraform plan file. Choices: 'create_file', 'set_ansible_stats', 'apply_plan'.|string|create| N/A
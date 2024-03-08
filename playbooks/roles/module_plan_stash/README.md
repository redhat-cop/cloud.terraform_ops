# module_plan_stash

A role to handle the base64 encoding or decoding of a terraform plan file using cloud.terraform.plan_stash module.

## Role Variables

Name | Description | Type | Default | Required
--- | --- | --- | --- | ---
module_plan_stash_operation|Whether to base64-encode the terraform plan file and saves it into ansible stats or base64-decode data from variable/binary_data to create a terraform plan file or apply the specific terraform plan file. Choices: 'stash', 'apply'.|string|N/A|true
module_plan_stash_plan_file_path|-The path to the terraform plan file. -When I(module_plan_stash_generate_plan_file=True), I(module_plan_stash_plan_file_path) will be used to store generated plan file.|path|N/A|true
module_plan_stash_var_name| -When O(state=stash), this parameter defines the variable name to be set into stats. -When O(state=load), this parameter defines the variable from ansible facts containing the base64-encoded data of the terraform plan file. -Variables must start with a letter or underscore character, and contain only letters, numbers and underscores.|string|terraform_plan|false
module_plan_stash_generate_plan_file|Whether to generate plan file from Terraform config to use when doing stash plan|bool|false|false
module_plan_stash_tf_project_path|The path to terraform project directory containing configuration file|path|false|false

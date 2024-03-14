# module_plan_stash

A role to handle the base64 encoding or decoding of a terraform plan file using cloud.terraform.plan_stash module.
This role can be used to
1. Perform base64-encoding of a terraform plan file and saves it into playbook execution stats similar to M(ansible.builtin.set_stats) module.
2. Perform base64-decoding of a terraform plan file from a variable defined into ansible facts and write them
    into a file specified by the user.

## Role Variables

Name | Description | Type | Default | Required
--- | --- | --- | --- | ---
module_plan_stash_operation|Whether to base64-encode the terraform plan file and save it into ansible stats or base64-decode data from variable/binary_data to create a terraform plan file. Choices: 'stash', 'load'.|string|N/A|true
module_plan_stash_plan_file_path|-The path to the terraform plan file. -This will be used for both encoding/decoding plan file depending on the value set into module_plan_stash_operation.|path|N/A|true
module_plan_stash_var_name| -When O(state=stash), this parameter defines the variable name to be set into stats. -When O(state=load), this parameter defines the variable from ansible facts containing the base64-encoded data of the terraform plan file. -Variables must start with a letter or underscore character, and contain only letters, numbers and underscores.|string|terraform_plan|false


## Example Playbook

Below example describes scenario of using the role in Ansible Controller workflow templates.

First create playbook below to stash the terraform plan and store it to ansible stats into variable "my_test_stashed_plan"
```
---
- name: Test the cloud.terraform_ops.module_plan_stash role (stash functionality)
  hosts: localhost
  gather_facts: true
  vars:
    module_plan_stash_var_name_val: my_test_stashed_plan
    module_plan_stash_plan_file_name_val: /path/to/plan/file/to/read/stash/myplan.tfplan
  tasks:

    - name: Stash the Terraform plan file into variable "{{ module_plan_stash_var_name_val }}"
      ansible.builtin.include_role:
        name: cloud.terraform_ops.module_plan_stash
      vars:
        module_plan_stash_operation: stash
        module_plan_stash_var_name: "{{ module_plan_stash_var_name_val }}" # if not provided, defaults to "terraform_plan"
        module_plan_stash_plan_file_path: "{{ module_plan_stash_plan_file_name_val }}"
```

Now, to use the stashed variable containing Terraform plan, create the playbook below
```
---
- name: Test the cloud.terraform_ops.module_plan_stash role (load functionality)
  hosts: localhost
  gather_facts: false
  vars:
    module_plan_stash_var_name_val: my_test_stashed_plan
    module_plan_stash_plan_file_path_val: /path/to/plan/file/to/load/create/loaded.tfplan
  tasks:
    - name: Create a gcs bucket for Terraform remote backend
      ansible.builtin.include_role:
        name: cloud.terraform_ops.module_plan_stash
      vars:
        module_plan_stash_operation: load
        module_plan_stash_var_name: "{{ module_plan_stash_var_name_val }}" # if not provided, defaults to "terraform_plan"
        module_plan_stash_plan_file_path: "{{ module_plan_stash_plan_file_path_val }}" #"path_to_my_plan_file"
```

Finally, add the above playbooks as "Job Templates", use the templates when creating a "Workflow Template".
When the workflow is run, below actions take place
- The first playbook stores b64encoded Terraform Plan into ansible stats (Artifacts) named "module_plan_stash_var_name"
- The second playbook uses artificats from first playbook to pass b64encoded plan as variable named "module_plan_stash_var_name"
- The second playbook loads the variable and creates a file I(module_plan_stash_plan_file_path) and writes the Terraform Plan to it, which can be used further through collections such as [cloud.terraform collection](https://github.com/ansible-collections/cloud.terraform)

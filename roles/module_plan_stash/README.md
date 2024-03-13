# module_plan_stash

A role to handle the base64 encoding or decoding of a terraform plan file using cloud.terraform.plan_stash module.
This role can be used to
1. Perform base64-encoding of a terraform plan file and saves it into playbook execution stats similar to M(ansible.builtin.set_stats) module.
2. Perform base64-decoding of a terraform plan file from a variable defined into ansible facts and write them
    into a file specified by the user.

## Role Variables

Name | Description | Type | Default | Required
--- | --- | --- | --- | ---
module_plan_stash_operation|Whether to base64-encode the terraform plan file and saves it into ansible stats or base64-decode data from variable/binary_data to create a terraform plan file or apply the specific terraform plan file. Choices: 'stash', 'load'.|string|N/A|true
module_plan_stash_plan_file_path|-The path to the terraform plan file. -When I(module_plan_stash_generate_plan_file=True), I(module_plan_stash_plan_file_path) will be used to store generated plan file.|path|N/A|true
module_plan_stash_tf_project_path|The path to terraform project directory containing configuration file|path|false|false
module_plan_stash_var_name| -When O(state=stash), this parameter defines the variable name to be set into stats. -When O(state=load), this parameter defines the variable from ansible facts containing the base64-encoded data of the terraform plan file. -Variables must start with a letter or underscore character, and contain only letters, numbers and underscores.|string|terraform_plan|false
module_plan_stash_generate_plan_file|Whether to generate plan file from Terraform config to use when doing stash plan|bool|false|false

Note:
- When I(module_plan_stash_generate_plan_file_val) is set to False, I(terraform_existing_plan_url) must be provided.

## Example Playbook

Below example describes scenario of using the role in Ansible Controller workflow templates.

First create playbook below to stash the terraform plan and store it to ansible stats into variable "my_test_stashed_plan"
```
---
- name: Test the cloud.terraform_ops.module_plan_stash role (stash functionality)
  hosts: localhost
  gather_facts: true
  vars:
    terraform_existing_config_url: "https://raw.githubusercontent.com/url/of/stored/config/file/main.tf"
    terraform_existing_plan_url: "https://raw.githubusercontent.com/url/of/stored/plan/file/myplan.tfplan"
  tasks:
    - name: Create temporary directory to run terraform configuration
      ansible.builtin.tempfile:
        state: directory
      register: tfdir

    - name: Block for cloud.terraform_ops.module_plan_stash example (stash functionality)
      block:
        - name: Download Terraform configuration
          uri:
            dest: "{{ tfdir.path }}/main.tf"
            url: "{{ terraform_existing_config_url }}"
          when: terraform_existing_config_url is defined and terraform_existing_config_url | length != 0

        - name: Download terraform plan file and store to temp dir as "myplan.tfplan"
          uri:
             dest: "{{ tfdir.path }}/myplan.tfplan"
             url: "{{ terraform_existing_plan_url }}"
          when: terraform_existing_plan_url is defined and terraform_existing_plan_url | length != 0

        - name: Stash the Terraform plan file into variable "my_test_stashed_plan"
          ansible.builtin.include_role:
            name: cloud.terraform_ops.module_plan_stash
          vars:
            module_plan_stash_operation: stash
            module_plan_stash_var_name: "my_test_stashed_plan" # if not provided, defaults to "terraform_plan"
            module_plan_stash_plan_file_path: "{{ tfdir.path }}/myplan.tfplan"
            module_plan_stash_tf_project_path: "{{ tfdir.path }}"
            module_plan_stash_generate_plan_file: false # set to I(true) to generate new plan file from config file, this will ignore plan file provided using "terraform_existing_plan_url"

      always:

        - name: Delete temporary directory
          ansible.builtin.file:
            state: absent
            path: "{{ tfdir.path }}"
```

Now, to use the stashed variable containing Terraform plan, create the playbook below
```
---
- name: Test the cloud.terraform_ops.module_plan_stash role (load functionality)
  hosts: localhost
  gather_facts: true
  vars:
  tasks:
    - name: Create temporary directory to run terraform configuration
      ansible.builtin.tempfile:
        suffix: '.tf'
        state: directory
      register: tfdir

    - name: Block for cloud.terraform_ops.module_plan_stash example (load functionality)
      block:
        - name: Stash the Terraform plan file into variable "my_test_stashed_plan"
          ansible.builtin.include_role:
            name: cloud.terraform_ops.module_plan_stash
          vars:
            module_plan_stash_operation: load
            module_plan_stash_var_name: "my_test_stashed_plan" # if not provided, defaults to "terraform_plan"
            module_plan_stash_plan_file_path: "{{ tfdir.path }}/loaded_plan_file.tfplan"

      always:
        - name: Delete temporary directory
          ansible.builtin.file:
            state: absent
            path: "{{ tfdir.path }}"
```

Finally, add the above playbooks as "Job Templates", use the templates when creating a "Workflow Template".
When the workflow is run, below actions take place
- The first playbook stores b64encoded Terraform Plan into ansible stats (Artifacts) named "module_plan_stash_var_name"
- The second playbook uses artificats from first playbook to pass b64encoded plan as variable named "module_plan_stash_var_name"
- The second playbook loads the variable and creates a file I(module_plan_stash_plan_file_path) and writes the Terraform Plan to it, which can be used further through collections such as [cloud.terraform collection](https://github.com/ansible-collections/cloud.terraform)

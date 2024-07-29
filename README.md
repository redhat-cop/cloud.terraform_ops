# cloud.terraform_ops Validated Content

## Description

The collection includes a variety of Ansible roles, to help automate the management of Cloud providers' resources for Red Hat Ansible Automation Platform Terraform integration.

## Requirements

- The [amazon.aws](https://github.com/ansible-collections/amazon.aws) and [community.aws](https://github.com/ansible-collections/amazon.aws) collections MUST be installed to use the role [cloud.terraform_ops.aws_s3backend](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/roles/aws_s3backend/README.md).

- The [google.cloud](https://github.com/ansible-collections/google.cloud) collection MUST be installed to use the role [cloud.terraform_ops.gcs_backend](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/roles/gcs_backend/README.md).

- The [azure.azcollection](https://github.com/ansible-collections/azure) collection MUST be installed to use the role [cloud.terraform_ops.azurerm_backend](https://github.com/redhat-cop/cloud.terraform_ops/tree/main/roles/azurerm_backend/README.md).

- The [cloud.terraform](https://github.com/ansible-collections/cloud.terraform) collection MUST be installed to use the role [cloud.terraform_ops.plan_stash](https://github.com/redhat-cop/cloud.terraform_ops/tree/main/roles/cloud.terraform_ops.plan_stash/README.md).

<!--start requires_ansible-->
### Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.15.0**.

### Python version compatibility

This collection requires Python 3.9 or greater.

### Included content

Click on the name of a role or playbook to view that content's documentation:

<!--start collection content-->
### Roles
Name | Description
--- | ---
[cloud.terraform_ops.aws_s3backend](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/roles/aws_s3backend/README.md)|A role to create the necessary AWS infrastructure for an S3 remote backend for Terraform.
[cloud.terraform_ops.gcs_backend](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/roles/gcs_backend/README.md)|A role to create the necessary Google Cloud infrastructure for a Google Cloud Storage (GCS) remote backend for Terraform.
[cloud.terraform_ops.azurerm_backend](https://github.com/redhat-cop/cloud.terraform_ops/tree/main/roles/azurerm_backend/README.md)|A role to create/delete the necessary Azure infrastructure for an Azurerm remote backend for Terraform.
[cloud.terraform_ops.plan_stash](https://github.com/redhat-cop/cloud.terraform_ops/tree/main/roles/plan_stash/README.md)|A role to handle the base64 encoding or decoding of a terraform plan file using cloud.terraform.plan_stash module.

## Installation

To consume this Validated Content from Automation Hub, please ensure that you add the following lines to your ansible.cfg file.

```
[galaxy]
server_list = automation_hub

[galaxy_server.automation_hub]
url=https://cloud.redhat.com/api/automation-hub/
auth_url=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
token=<SuperSecretToken>
```
The token can be obtained from the [Automation Hub Web UI](https://console.redhat.com/ansible/automation-hub/token).

Once the above steps are done, you can run the following command to install the collection.

```
ansible-galaxy collection install cloud.terraform_ops
```

## Use Cases

Once installed, you can reference the cloud.terraform_ops collection content by its fully qualified collection name (FQCN), for example:

```yaml
  # create the necessary AWS infrastructure for an S3 remote backend for Terraform.
  - hosts: all

    roles:
      - role: cloud.terraform_ops.aws_s3backend
        aws_s3backend_bucket_name: sample_bucket_for_tf_backend

  # Use plan_stash role to store the plan
  - hosts: localhost
    gather_facts: true
    vars:
      plan_stash_var_name_val: my_test_stashed_plan
      plan_stash_plan_file_name_val: /path/to/plan/file/to/read/stash/myplan.tfplan
    tasks:
      - name: Generate planfile by running Terraform plan
        cloud.terraform.terraform:
          project_path: /path/to/tf/project/directory/
          force_init: true
          plan_file: "{{ plan_stash_generate_plan_file_name_val }}"
          state: present

      - name: Stash the Terraform plan file into variable "{{ plan_stash_var_name_val }}"
        ansible.builtin.include_role:
          name: cloud.terraform_ops.plan_stash
        vars:
          plan_stash_operation: stash
          plan_stash_var_name: "{{ plan_stash_var_name_val }}" # if not provided, defaults to "terraform_plan"
          plan_stash_plan_file_path: "{{ plan_stash_generate_plan_file_name_val }}"
```

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against this collection repository.
See [CONTRIBUTING.md](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/CONTRIBUTING.md) for more details.

## Testing and Development

The project uses `ansible-lint` and `black`.
Assuming this repository is checked out in the proper structure,
e.g. `collections_root/ansible_collections/cloud/terraform_ops/`, run:

```shell
  tox -e linters -vv
```

Sanity and unit tests are run as normal:

```shell
  ansible-test sanity
```

If you want to run AWS cloud integration tests, ensure you log in :

```shell
# using the "default" profile on AWS
  aws configure set aws_access_key_id     my-access-key
  aws configure set aws_secret_access_key my-secret-key
  aws configure set region                eu-north-1

```

Once credentials are set up, run all integration tests with `ansible-test integration` or run a subset of integration tests with `ansible-test integration <target>`.

This collection is tested using GitHub Actions. To know more about CI, refer to [CI.md](https://github.com/https://github.com/redhat-cop/cloud.terraform_ops/blob/main/CI.md).

## Support

For the latest supported versions, refer to the release notes below.

If you encounter issues or have questions, you can submit a support request through the following channels:
 - GitHub Issues: Report bugs, request features, or ask questions by opening an issue in the [GitHub repository](https://github.com/redhat-cop/cloud.terraform_ops/).
 - Ansible Community: Engage with the Ansible community on the Ansible Project Mailing List or [Ansible Forum](https://forum.ansible.com/g/AWS).

## Release Notes

See the [raw generated changelog](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/CHANGELOG.rst).

## Related Information

 - [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html).
 -  [Ansible Rulebook documentation](https://ansible.readthedocs.io/projects/rulebook/en/stable/index.html).
 - [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## License

GNU General Public License v3.0 or later

See [LICENSE](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/LICENSE) to see the full text.

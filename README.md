# cloud.terraform_ops roles to create/configure Cloud providers' resources for Red Hat Ansible Automation Platform Terraform integration

This repository hosts the `cloud.terraform_ops` Ansible Collection.

The collection includes a variety of Ansible roles, to help automate the management of Cloud providers' resources for Red Hat Ansible
Automation Platform Terraform integration.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.14.0**.

## Python version compatibility

This collection requires Python 3.9 or greater.

## Included content

Click on the name of a role or playbook to view that content's documentation:

<!--start collection content-->
### Roles
Name | Description
--- | ---
[cloud.terraform_ops.aws_s3backend](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/roles/aws_s3backend/README.md)|A role to create the necessary AWS infrastructure for an S3 remote backend for Terraform.
[cloud.terraform_ops.gcs_backend](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/roles/gcs_backend/README.md)|A role to create the necessary Google Cloud infrastructure for a Google Cloud Storage (GCS) remote backend for Terraform.
[cloud.terraform_ops.azurerm_backend](https://github.com/redhat-cop/cloud.terraform_ops/tree/main/roles/azurerm_backend/README.md)|A role to create/delete the necessary Azure infrastructure for an Azurerm remote backend for Terraform.
[cloud.terraform_ops.plan_stash](https://github.com/redhat-cop/cloud.terraform_ops/tree/main/roles/plan_stash/README.md)|A role to handle the base64 encoding or decoding of a terraform plan file using cloud.terraform.plan_stash module.

## Installation and Usage

### Requirements

- The [amazon.aws](https://github.com/ansible-collections/amazon.aws) and [community.aws](https://github.com/ansible-collections/amazon.aws) collections MUST be installed to use the role [cloud.terraform_ops.aws_s3backend](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/roles/aws_s3backend/README.md).

- The [google.cloud](https://github.com/ansible-collections/google.cloud) collection MUST be installed to use the role [cloud.terraform_ops.gcs_backend](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/roles/gcs_backend/README.md).

- The [azure.azcollection](https://github.com/ansible-collections/azure) collection MUST be installed to use the role [cloud.terraform_ops.azurerm_backend](https://github.com/redhat-cop/cloud.terraform_ops/tree/main/roles/azurerm_backend/README.md).

- The [cloud.terraform](https://github.com/ansible-collections/cloud.terraform) collection MUST be installed to use the role [cloud.terraform_ops.plan_stash](https://github.com/redhat-cop/cloud.terraform_ops/tree/main/roles/cloud.terraform_ops.plan_stash/README.md).

### Installation

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

### Using this collection

Once installed, you can reference the cloud.terraform_ops collection content by its fully qualified collection name (FQCN), for example:

```yaml
  - hosts: all

    roles:
      - role: cloud.terraform_ops.aws_s3backend
        aws_s3backend_bucket_name: sample_bucket_for_tf_backend
```

### See Also

* [Using Ansible collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against this collection repository.

### Testing and Development

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

## License

GNU General Public License v3.0 or later

See [LICENSE](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/LICENSE) to see the full text.

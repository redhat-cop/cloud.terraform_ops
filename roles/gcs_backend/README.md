# gcs_backend

A role to ensure that the necessary GCP infrastructure is present for the Google Cloud Storage (GCS) remote backend for Terraform.

This role can be used to create or delete the following
- A Google Cloud Storage bucket with object versioning enabled

## Role Variables

Name | Description | Type | Default | Required
--- | --- | --- | --- | ---
gcs_backend_operation|Whether to create or delete the Backend resources (GCS bucket). Choices: 'create', 'delete'.  Note that `delete` operation might fail if bucket is non-empty.|string|create| N/A
gcs_backend_gcp_project|The ID of the Google Cloud Platform project to use. You can set this using the `GCP_PROJECT` env variable.|string|N/A|No
gcs_backend_bucket_name|The name of the bucket to be created. |string|N/A| Yes
gcs_backend_auth_kind|The type of credential used. You can set this using the `GCP_AUTH_KIND` env variable. Choices: 'application', 'serviceaccount', 'machineaccount'.|string|N/A|No
gcs_backend_service_account_file|The path of a Service Account JSON file if serviceaccount is selected as authentication type. You can set this using the `GCP_SERVICE_ACCOUNT_FILE` env variable.|string|N/A| when `gcs_backend_auth_kind = serviceaccount`
gcs_backend_service_account_email|An optional service account email address if machineaccount is selected and the user does not wish to use the default email. You can set this using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.|string|N/A| No

### Using with Ansible Automation Platform (AAP)

Note: When using this role in AAP, authentication to Google Cloud Platform (GCP) can be performed by adding GCE type credentials in AAP and providing it to the job template that makes use of this role.

## Examples
```
- name: Create a gcs bucket for Terraform remote backend
  ansible.builtin.include_role:
    name: cloud.terraform_ops.gcs_backend
  vars:
    gcs_backend_operation: create
    gcs_backend_bucket_name: test-tf-backend-bucket
    gcs_backend_gcp_project: project-uscentral-demo
    gcs_backend_auth_kind: serviceaccount
    gcs_backend_service_account_file: /path/to/auth/credentials.json

- name: Delete the gcs bucket for Terraform remote backend
  ansible.builtin.include_role:
    name: cloud.terraform_ops.gcs_backend
  vars:
    gcs_backend_operation: delete
    gcs_backend_bucket_name: test-tf-backend-bucket
    gcs_backend_gcp_project: project-uscentral-demo
    gcs_backend_auth_kind: serviceaccount
    gcs_backend_service_account_file: /path/to/auth/credentials.json
```

## License

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/cloud.terraform_ops/blob/stable-1/LICENSE) to see the full text.

## Author Information

- Ansible Cloud Content Team

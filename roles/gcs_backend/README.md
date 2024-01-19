# gcs_backend

A role to ensure that the necessary GCP infrastructure is present for an Google Cloud Storage(GCS) remote backend for Terraform.

This role can be used to create or delete following
- A Google Cloud Storage bucket with object versioning enabled

## Role Variables

- operation - Choices include 'create' and 'delete'. `required`

- gcs_backend_gcp_project - The ID of the Google Cloud Platform project to use. `required`

- gcs_backend_gcs_backend_bucket_name - The name of the bucket to be created. `required`

- gcs_backend_auth_kind - The type of credential used. Currently supports "serviceaccount". `required`

- gcs_backend_service_account_file - The path of a Service Account JSON file if serviceaccount is selected as type. `required`


Return Value
------------

## Examples
```
- name: Create a gcs bucket for Terraform remote backend
  ansible.builtin.include_role:
    name: cloud.terraform_ops.gcs_backend
  vars:
    operation: create
    gcs_backend_gcs_backend_bucket_name: test-tf-backend-bucket
    gcs_backend_gcp_project: project-uscentral-demo
    gcs_backend_auth_kind: serviceaccount
    gcs_backend_service_account_file: /path/to/auth/credentials.json

- name: Delete the gcs bucket for Terraform remote backend
  ansible.builtin.include_role:
    name: cloud.terraform_ops.gcs_backend
  vars:
    operation: delete
    gcs_backend_gcs_backend_bucket_name: test-tf-backend-bucket
    gcs_backend_gcp_project: project-uscentral-demo
    gcs_backend_auth_kind: serviceaccount
    gcs_backend_service_account_file: /path/to/auth/credentials.json
```
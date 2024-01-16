# aws_s3backend

A role to ensure that the necessary AWS infrastructure is present/absent for an S3 remote backend for Terraform.
When creating, the S3 bucket will be created with the required permissions for Terraform. See U(https://developer.hashicorp.com/terraform/language/settings/backends/s3#s3-bucket-permissions).
The role also allow for optionally creating a DynamoDB table with the required permissions for state locking and with a partition key named LockID with type of String.
The role is able to either accept an existing IAM role to be granted the above permissions or create a new one.

## Requirements

AWS User Account with permission to create S3 bucket, DynamoDB table and IAM policy.

## Role Variables

- **aws_s3backend_operation**: Whether to create or delete the Backend resources (S3 bucket and DynamoDB table). Choices: 'create', 'delete'. Default: 'create'.
- **aws_s3backend_bucket_name**: The name of the S3 bucket to create/delete. **Required**
- **aws_s3backend_dynamodb_table_name**: The name of the DynamoDB table to create/delete for state locking. The table will be created with a partition key named LockID with type of String.
- **aws_s3backend_iam_type**: The type of IAM resource to grant access to. Choices: 'user', 'group', 'role'.
- **aws_s3backend_iam_name**: The name of the IAM resource (user, group or role)user name, group name or role name of IAM resource you wish to grant access to S3 and DynamoDB. Note that, if the specified resource does not exist, it will be created. Required when I(aws_s3backend_iam_type) is provided.
- **aws_s3backend_terraform_state_path**: Object path granted to the specified user/role/group.
- **aws_s3backend_delete_iam_resource**: On deletion, specifies whether the IAM resource (user, role or group) should be deleted along with the other resources (S3 bucket and DynamoDB table).

## Example Playbook

    - hosts: localhost
      roles:
        - role: cloud.terraform_ops.aws_s3backend
          aws_s3backend_operation: create
          aws_s3backend_bucket_name: test_terraform_s3
          aws_s3backend_dynamodb_table_name: db_state_lock
          aws_s3backend_iam_type: user
          aws_s3backend_iam_name: ansible
          aws_s3backend_terraform_state_path: /test/terraform.tfstate

## License

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/ansible-collections/cloud.terraform_ops/blob/main/LICENSE) to see the full text.

## Author Information

- Ansible Cloud Content Team

=================================
cloud.terraform_ops Release Notes
=================================

.. contents:: Topics

v1.0.0
======

Release Summary
---------------

This first release includes several roles to create/configure Cloud providers' resources for Red Hat Ansible Automation Platform Terraform integration.

New Roles
---------

- aws_s3backend - A role to create/delete the AWS infrastructure for an S3 remote backend for Terraform.
- azurerm_backend - A role to create/delete the necessary Azure infrastructure for an Azurerm remote backend for Terraform.
- gcs_backend - A role to create/delete the GCP infrastructure for a GCS remote backend for Terraform.
- plan_stash - A role to handle the base64 encoding or decoding of a terraform plan file using cloud.terraform.plan_stash module.

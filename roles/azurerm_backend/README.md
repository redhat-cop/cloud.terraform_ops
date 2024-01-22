# azurerm_backend

A role to create/delete the necessary Azure infrastructure for an Azurerm remote backend for Terraform.
The role ensures that the specified resource group, storage account and container are present/absent. When a service principal is specified, the role will assign the [Storage Blob data contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) to the service principal.

## Requirements

Azure Account with permission to create Resource group, Storage account and container, and eventually assign role to service principal.

## Role Variables

Name | Description | Type | Default | Required
--- | --- | --- | --- | ---
azurerm_backend_operation|Whether to create or delete the infrastructure for the azurerm Terraform backend. Choices: 'create', 'delete'|string|'create'|N/A
azurerm_backend_resource_group_name|The name of the resource group to create/delete|string|N/A|Yes
azurerm_backend_location|Azure location for the resource group|string|N/A|When creating a new resource group.
azurerm_backend_storage_account_name|The name of the storage account name to be created. When not specified and if none is existing from the resource group, the role will create a new one with generated name|string|N/A|No
azurerm_backend_storage_account_type|Type of storage account. Valid values are: 'Premium_LRS', 'Standard_GRS', 'Standard_LRS', 'Standard_RAGRS', 'Standard_ZRS', 'Premium_ZRS', 'Standard_RAGZRS', 'Standard_GZRS'.|string|Standard_LRS|When creating a storage account.
azurerm_backend_container_name|The Name of the Storage Container to create within the Storage Account.|string|N/A|When __azurerm_backend_operation=create__.
azurerm_backend_service_principal_id|The service principal Id used by Terraform to push Terraform state to the container. The role will assign the [Storage Blob data contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor) role for the specified container to this service principal.|string|N/A|No

## Example Playbook

    - hosts: localhost
      roles:
        - role: cloud.terraform_ops.azurerm_backend
          azurerm_backend_operation: create
          azurerm_backend_resource_group_name: "StorageAccount-ResourceGroup"
          azurerm_backend_location: eastus
          azurerm_backend_storage_account_name: ansible123
          azurerm_backend_storage_account_type: Premium_LRS
          azurerm_backend_container_name: tfstate
          azurerm_backend_service_principal_id: abcdef12-123a-456b-789c-12345abcde6e

## License

GNU General Public License v3.0 or later

See [LICENCE](https://github.com/redhat-cop/cloud.terraform_ops/blob/main/LICENSE) to see the full text.

## Author Information

- Ansible Cloud Content Team

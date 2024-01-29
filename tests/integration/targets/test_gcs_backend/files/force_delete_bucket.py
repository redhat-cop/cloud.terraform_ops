#!/usr/bin/env python
import os
from google.cloud import storage


def delete_bucket(bucket_name, project_name, credentials_file_path):
    """Deletes a bucket. The bucket must be empty."""
    storage_client = storage.Client(project=project_name, credentials=credentials_file_path)

    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete(force=True)
    print(f"Bucket {bucket.name} deleted")


if __name__ == "__main__":
    bucket_name = os.getenv("BUCKET_NAME")
    project_name = os.getenv("CLOUDSDK_CORE_PROJECT")
    credentials_file_path = os.getenv("GCP_SERVICE_ACCOUNT_CREDENTIALS_FILE")

    delete_bucket(bucket_name, project_name, credentials_file_path)

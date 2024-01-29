#!/usr/bin/env python
import os
from google.cloud import storage
from google.oauth2.service_account import Credentials


def delete_bucket(bucket_name, project_name, credentials):
    """Deletes a bucket. The bucket must be empty."""
    storage_client = storage.Client(project=project_name, credentials=credentials)

    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete(force=True)
    print(f"Bucket {bucket.name} deleted")


if __name__ == "__main__":
    bucket_name = os.getenv("BUCKET_NAME")
    project_name = os.getenv("CLOUDSDK_CORE_PROJECT")
    credentials_file_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    credentials = Credentials.from_service_account_file(credentials_file_path)

    delete_bucket(bucket_name, project_name, credentials)

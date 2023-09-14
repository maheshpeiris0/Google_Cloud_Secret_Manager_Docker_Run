# Import the Secret Manager client library.
from google.cloud import secretmanager

def create_secret(project_id: str, secret_id: str, secret_value: str):
    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the parent project.
    parent = f"projects/{project_id}"

    # Create the secret.
    response = client.create_secret(
        request={
            "parent": parent,
            "secret_id": secret_id,
            "secret": {"replication": {"automatic": {}}},
        }
    )

    # Print the new secret name.
    print(f"Created secret: {response.name}")

    # Add a version to the secret with the specified value.
    version = client.add_secret_version(
        request={
            "parent": response.name,
            "payload": {"data": secret_value.encode("UTF-8")},
        }
    )

    # Print the new secret version name.
    print(f"Added secret version: {version.name}")

    return response

if __name__ == "__main__":
    create_secret("project-name", "python-secret", "my new secret")

# Import the Secret Manager client library.
from google.cloud import secretmanager

def read_secrets(project_id: str, secret_name: str):
    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"

    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode("UTF-8")

    print(f"The secret value is: {payload}")

    return payload

if __name__ == "__main__":
    read_secrets("project-name", "python-secret")

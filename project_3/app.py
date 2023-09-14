from flask import Flask, jsonify
import os
import json
from google.cloud import secretmanager
from google.oauth2 import service_account
from google.cloud import bigquery

# Google Cloud Project ID
project_id = 'project-name'
secret_name = 'my-service-key'
client_sm = secretmanager.SecretManagerServiceClient()

# Access the secret
name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
response = client_sm.access_secret_version(request={"name": name})

# Extract the secret value (JSON string)
secret_value_json = response.payload.data.decode("UTF-8")

# Load the JSON string into a dictionary
secret_value_dict = json.loads(secret_value_json)

# Use the dictionary to create credentials
credentials = service_account.Credentials.from_service_account_info(
    secret_value_dict
)

# Initialize a BigQuery client with the credentials
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

app = Flask(__name__)

@app.route('/')
def hello_world():

    client = bigquery.Client()
    query_job = client.query(
        """
        SELECT
          CONCAT(
            'https://stackoverflow.com/questions/',
            CAST(id as STRING)) as url,
          view_count
        FROM `bigquery-public-data.stackoverflow.posts_questions`
        WHERE tags like '%google-bigquery%'
        ORDER BY view_count DESC
        LIMIT 10"""
    )

    results = []  # Initialize an empty list to store query results

    for row in query_job:
        result_dict = {
            "url": row.url,
            "view_count": row.view_count
        }
        results.append(result_dict)

    # Return the results as JSON in the HTTP response
    return jsonify({"results": results})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
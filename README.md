# Google_Cloud_Secret_Manager_Docker_Run


Creating a secret
<br>

echo -n "my super secret data" | gcloud secrets create my-secret-3 --replication-policy="automatic" --data-file=-

gcloud secrets create my-secret-4 --replication-policy="automatic" --data-file=mahesh.txt  

<br>
gcloud secrets versions access latest --secret="my-secret"


<br>

gcloud secrets versions add my-secret-4 --data-file="hello.txt"

<br>

echo -n "this is my super secret data" | gcloud secrets versions add my-secret-4 --data-file=-

<br>

gcloud secrets list

<br>

gcloud secrets describe secret-id


<br>

gcloud secrets versions access version-id --secret="secret-id"

<br>

import google.auth, google.auth.transport.requests, requests, json, time

PROJECT_ID = "project-d889d417-cdf3-442b-9b3"
LOCATION = "us-central1"
MODEL = "veo-2.0-generate-001"
API_BASE = f"https://{LOCATION}-aiplatform.googleapis.com"

creds, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

op_name = "projects/project-d889d417-cdf3-442b-9b3/locations/us-central1/publishers/google/models/veo-2.0-generate-001/operations/7444b115-c605-4382-8954-c00c54df5af9"

fetch_urls = [
    f"{API_BASE}/v1/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/{MODEL}:fetchPredictOperation",
    f"{API_BASE}/v1beta1/projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/{MODEL}:fetchPredictOperation",
]
body = {"operationName": op_name}
headers = {"Authorization": f"Bearer {creds.token}", "Content-Type": "application/json"}

for url in fetch_urls:
    r = requests.post(url, headers=headers, json=body, timeout=15)
    print(f"[{r.status_code}] {url[-80:]}")
    if r.status_code == 200:
        data = r.json()
        print("done:", data.get("done"))
        print("keys:", list(data.keys()))
        print("Full:", json.dumps(data, ensure_ascii=False)[:600])
    else:
        print("Error:", r.text[:300])
    print()

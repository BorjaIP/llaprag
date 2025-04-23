import mimetypes
import time

import requests

api_key = ""

headers = {"Authorization": f"Bearer {api_key}"}
file_path = "./attention.pdf"
base_url = "https://api.cloud.llamaindex.ai/api/parsing"

with open(file_path, "rb") as f:
    mime_type = mimetypes.guess_type(file_path)[0]
    files = {"file": (f.name, f, mime_type)}

    # send the request, upload the file
    url = f"{base_url}/upload"
    response = requests.post(url, headers=headers, files=files)

response.raise_for_status()
# get the job id for the result_url
job_id = response.json()["id"]
result_type = "text"  # or "markdown"
result_url = f"{base_url}/job/{job_id}/result/{result_type}"

# check for the result until its ready
while True:
    response = requests.get(result_url, headers=headers)
    if response.status_code == 200:
        break

    time.sleep(2)

# download the result
result = response.json()
output = result[result_type]

print(output)

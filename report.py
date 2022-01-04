import os
import requests
import sys
from datetime import datetime, timezone

print("Executing report.py")
branch = os.environ.get('branch')
release_name = os.environ.get('release_name')
version_name = os.environ.get('version_name')
version_code = os.environ.get('version_code')
mobile_platform = os.environ.get('mobile_platform')
url = os.environ.get('url')
auth_token = os.environ.get('auth_token')

released_at = datetime.now(timezone.utc)
released_at = released_at.strftime("%Y-%m-%dT%H:%M:%S.") + released_at.strftime("%f")[:3] + released_at.strftime("%z")

payload = {
    "release_name": release_name,
    "version_name": version_name,
    "version_code": version_code,
    "branch": branch,
    "mobile_platform": mobile_platform,
    "hard_tombstone": False,
    "soft_tombstone": False,
    "locked": False,
    "released_at": released_at
}

print('Payload: {}'.format(payload))

print('Sending payload to {}'.format(url))
request_headers = {'Authorization': auth_token}
r = requests.post(url, json=payload, headers=request_headers)

if r.status_code != 200:
    print('Unable to send build info to {}'.format(url))
    print('Response: {}'.format(r.text))
    sys.exit(1)
else:
    print("Release successfully sent!")
    sys.exit(0)
import requests

HARNESS_API_KEY = "your_harness_api_key"
HARNESS_BASE_URL = "https://app.harness.io/gateway/api"

headers = {
    "x-api-key": HARNESS_API_KEY,
    "Content-Type": "application/json"
}

def get_deployments_paginated(page, limit=100):
    url = f"{HARNESS_BASE_URL}/deployments"
    params = {
        "accountIdentifier": "your_account_id",
        "page": page,
        "limit": limit
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['data']['content']
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

def get_deployments():
    deployments = []
    page = 0
    while True:
        batch = get_deployments_paginated(page)
        if not batch:
            break
        deployments.extend(batch)
        page += 1
    print(f"Total deployments fetched: {len(deployments)}")
    return deployments

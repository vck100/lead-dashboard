"""
API client.

Handles communication with Flask API.
"""


import requests


BASE_URL = "https://lead-qualifier-api-1.onrender.com"


def process_lead(
    company,
    budget,
    notes
):

    response = requests.post(
        f"{BASE_URL}/process-lead",
        json={
            "company": company,
            "budget": budget,
            "notes": notes
        }
    )

    return response.json()



def get_leads():

    response = requests.get(
        f"{BASE_URL}/leads"
    )

    return response.json()
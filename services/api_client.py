"""
API client.

Handles communication with Flask API.
"""


import requests


API_URL = "http://127.0.0.1:5000"


def process_lead(
    company,
    budget,
    notes
):

    response = requests.post(
        f"{API_URL}/process-lead",
        json={
            "company": company,
            "budget": budget,
            "notes": notes
        }
    )

    return response.json()



def get_leads():

    response = requests.get(
        f"{API_URL}/leads"
    )

    return response.json()
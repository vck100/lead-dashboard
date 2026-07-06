"""
API Client.

Handles communication between the
Streamlit frontend and Flask backend.
"""


import requests



API_URL = "http://127.0.0.1:5000/process-lead"



def process_lead(
    company,
    budget,
    notes
):

    payload = {

        "company": company,

        "budget": budget,

        "notes": notes

    }



    response = requests.post(

        API_URL,

        json=payload

    )



    return response.json()
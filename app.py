"""
Sales Lead Dashboard.

Frontend interface for the Lead Qualification API.
"""


import streamlit as st


from services.api_client import process_lead, get_leads
from components.metrics import display_metrics
from components.lead_table import display_lead_table



st.set_page_config(

    page_title="Sales Lead Dashboard",

    layout="wide"

)



st.title(
    "Sales Lead Dashboard"
)



st.session_state.leads = get_leads()

if st.button(
    "Refresh Dashboard"
):

    st.session_state.leads = get_leads()    



company = st.text_input(
    "Company Name"
)



budget = st.number_input(
    "Budget (£)",
    min_value=0
)



notes = st.text_area(
    "Lead Notes"
)



if st.button(
    "Process Lead"
):

    result = process_lead(
        company,
        budget,
        notes
    )


    st.session_state.leads = get_leads()


    st.subheader(
        "AI Insight"
    )


    st.write(
        result["ai_insight"]
    )



st.divider()



display_metrics(
    st.session_state.leads
)



st.subheader(
    "Lead History"
)



display_lead_table(
    st.session_state.leads
)
"""
Sales Lead Dashboard.

Frontend interface for the Lead Qualification API.
"""

import streamlit as st

from components.lead_details import display_lead_details
from services.api_client import get_leads
from components.metrics import display_metrics
from components.priority_leads import display_priority_leads
from components.lead_table import display_lead_table
from components.charts import display_charts

st.set_page_config(
    page_title="Sales Lead Dashboard",
    layout="wide"
)


st.title("Sales Lead Dashboard")
st.caption("Monitor and prioritise inbound sales leads.")


# Load leads once
if "leads" not in st.session_state:
    st.session_state.leads = get_leads()


# Refresh button
if st.button("Refresh Dashboard"):
    st.session_state.leads = get_leads()


# Search
search = st.text_input("🔍 Search Company")


# Filter
filter_option = st.selectbox(
    "Filter Leads",
    [
        "All",
        "Qualified",
        "Not Qualified"
    ]
)


# Start with all leads
filtered_leads = st.session_state.leads


# Search filter
if search:
    filtered_leads = [
        lead
        for lead in filtered_leads
        if search.lower() in str(
            lead.get("company", "")
        ).lower()
    ]


# Qualification filter
if filter_option != "All":
    filtered_leads = [
        lead
        for lead in filtered_leads
        if str(
            lead.get("qualification", "")
        ).lower() == filter_option.lower()
    ]


st.divider()


display_metrics(filtered_leads)
display_charts(
    filtered_leads
)

st.divider()

display_priority_leads(filtered_leads)


st.divider()

display_lead_details(
    filtered_leads
)

st.divider()

st.subheader("Lead History")


display_lead_table(filtered_leads)
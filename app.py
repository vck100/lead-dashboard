import os
from urllib.parse import quote

import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Sales Lead Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv(
    dotenv_path=os.path.join(
        os.path.dirname(__file__),
        ".env"
    )
)

AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
BASE_ID = os.getenv("BASE_ID")

if not AIRTABLE_API_KEY or not BASE_ID:
    st.error("Environment variables could not be loaded.")
    st.stop()

# ==========================================================
# AIRTABLE CONFIGURATION
# ==========================================================

TABLE_NAME = quote("Lead Contact")

AIRTABLE_URL = (
    f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"
)

REQUEST_HEADERS = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}"
}

# ==========================================================
# GET LEADS
# ==========================================================

def get_leads():
    """
    Retrieve all leads from Airtable.
    """

    response = requests.get(
        AIRTABLE_URL,
        headers=REQUEST_HEADERS
    )

    if response.status_code != 200:
        st.error("Unable to retrieve leads from Airtable.")
        return pd.DataFrame()

    lead_data = response.json().get("records", [])

    return pd.DataFrame(
        [record["fields"] for record in lead_data]
    )


leads_df = get_leads()

# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("📊 Sales Lead Dashboard")
st.caption("Manage and prioritise inbound sales leads")

# ==========================================================
# REFRESH BUTTON
# ==========================================================

if st.button("🔄 Refresh Dashboard"):
    st.rerun()

# ==========================================================
# SEARCH
# ==========================================================

search = st.text_input("🔍 Search Company")

if search and "Company" in leads_df.columns:
    leads_df = leads_df[
        leads_df["Company"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# ==========================================================
# QUALIFICATION FILTER
# ==========================================================

if "Qualification" in leads_df.columns:

    filter_option = st.selectbox(
        "Filter Leads",
        [
            "All",
            "Qualified",
            "Not Qualified"
        ]
    )

    if filter_option == "Qualified":
        leads_df = leads_df[
            leads_df["Qualification"] == "qualified"
        ]

    elif filter_option == "Not Qualified":
        leads_df = leads_df[
            leads_df["Qualification"] != "qualified"
        ]

# ==========================================================
# SORT LEADS
# ==========================================================

if "Score" in leads_df.columns:
    leads_df = leads_df.sort_values(
        by="Score",
        ascending=False
    )

# ==========================================================
# DASHBOARD METRICS
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Leads",
        len(leads_df)
    )

with col2:

    if "Qualification" in leads_df.columns:
        qualified_count = len(
            leads_df[
                leads_df["Qualification"] == "qualified"
            ]
        )
    else:
        qualified_count = 0

    st.metric(
        "Qualified Leads",
        qualified_count
    )

with col3:

    if "Score" in leads_df.columns:
        average_score = round(
            leads_df["Score"].mean(),
            2
        )
    else:
        average_score = 0

    st.metric(
        "Average Score",
        average_score
    )

with col4:

    if "Score" in leads_df.columns:
        highest_score = leads_df["Score"].max()
    else:
        highest_score = 0

    st.metric(
        "Highest Score",
        highest_score
    )

# ==========================================================
# TOP PRIORITY LEADS
# ==========================================================

st.subheader("🔥 Top Priority Leads")

if not leads_df.empty:
    st.dataframe(
        leads_df.head(5),
        use_container_width=True
    )

# ==========================================================
# LEAD DETAILS
# ==========================================================

st.subheader("📋 Lead Details")

if not leads_df.empty and "Company" in leads_df.columns:

    selected_company = st.selectbox(
        "Select a Company",
        leads_df["Company"]
    )

    selected_lead = leads_df[
        leads_df["Company"] == selected_company
    ].iloc[0]

    st.write(f"### {selected_company}")

    if "Score" in selected_lead:
        st.write(
            f"**Lead Score:** ⭐ {selected_lead['Score']}/5"
        )

    if "Qualification" in selected_lead:
        st.write(
            f"**Qualification:** {selected_lead['Qualification']}"
        )

    if "Company Summary" in selected_lead:
        st.write("### AI Company Summary")
        st.write(selected_lead["Company Summary"])

    if "Sales Recommendation" in selected_lead:
        st.write("### Sales Recommendation")
        st.write(selected_lead["Sales Recommendation"])

# ==========================================================
# ALL LEADS
# ==========================================================

st.subheader("📄 All Leads")

st.dataframe(
    leads_df,
    use_container_width=True
)
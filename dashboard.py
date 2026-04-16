import streamlit as st
import requests
import pandas as pd

BASE_ID = "lead-dashboard"
TABLE_NAME = "Lead Base (Python)"

url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

headers = {
    "Authorization": f"Bearer {AIRTABLE_API_KEY}"
}

response = requests.get(url, headers=headers)
data = response.json()["records"]

leads = [record["fields"] for record in data]
df = pd.DataFrame(leads)

st.title("Sales Lead Dashboard")
st.metric("Total Leads", len(df))

if "Qualification" in df.columns:
    qualified = df[df["Qualification"] == "qualified"]
    st.metric("Qualified Leads", len(qualified))

    if "Score" in df.columns:
    st.metric("Average Score", round(df["Score"].mean(), 2))

    st.subheader("All Leads")
st.dataframe(df)

if "Qualification" in df.columns:
    chart_data = df["Qualification"].value_counts()
    st.bar_chart(chart_data)

filter_option = st.selectbox(
    "Filter by Qualification",
    ["All", "qualified", "not qualified"]
)

if filter_option != "All":
    df = df[df["Qualification"] == filter_option]

    
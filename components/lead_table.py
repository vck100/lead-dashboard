"""
Lead table component.

Displays processed leads in the dashboard.
"""


import pandas as pd
import streamlit as st



def display_lead_table(
    leads
):

    if len(leads) == 0:

        st.info(
            "No leads processed yet."
        )

        return



    df = pd.DataFrame(leads)

    columns = [
        "company",
        "budget",
        "score",
        "qualification",
        "created"
]

    df = df[columns]

    if "budget" in df.columns:

         df["budget"] = df["budget"].apply(
        lambda x: f"£{x:,.0f}" if x else "N/A"
    )

    df = df.rename(
    columns={
        "company": "Company",
        "budget": "Budget",
        "score": "Score",
        "qualification": "Qualification",
        "created": "Date Added"
    }
)
    df["Qualification"] = df["Qualification"].replace({
    "qualified": "🟢 Qualified",
    "not qualified": "🔴 Not Qualified",
    None: "⚪ Unknown"
})

    df = df.sort_values(
        by=["Score", "Budget"],
        ascending=False
)
    df["Date Added"] = (
    pd.to_datetime(df["Date Added"])
      .dt.strftime("%d %b %Y")
)

    st.dataframe(

        df,

        use_container_width=True

    )
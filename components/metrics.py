"""
Dashboard metric components.

Displays lead performance statistics.
"""


import streamlit as st



def display_metrics(
    leads
):

    total_leads = len(
        leads
    )


    qualified_leads = len(
        [
            lead
            for lead in leads
            if lead.get("qualification") == "Qualified"
        ]
    )


    if total_leads > 0:

        average_score = round(
            sum(
                lead.get("score", 0)
                for lead in leads
            )
            / total_leads,
            1
        )

    else:

        average_score = 0



    col1, col2, col3 = st.columns(
        3
    )



    col1.metric(
        "Total Leads",
        total_leads
    )


    col2.metric(
        "Qualified Leads",
        qualified_leads
    )


    col3.metric(
        "Average Score",
        average_score
    )
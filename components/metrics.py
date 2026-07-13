"""
Dashboard metric components.

Displays lead performance statistics.
"""

import streamlit as st


def display_metrics(leads):

    total_leads = len(leads)

    qualified_leads = 0

    scores = []

    for lead in leads:

        qualification = str(
            lead.get(
                "qualification",
                ""
            )
        ).lower()

        if qualification == "qualified":

            qualified_leads += 1

        score = lead.get(
            "score"
        )

        if score is not None:

            try:

                scores.append(
                    int(score)
                )

            except:

                pass

    if len(scores) > 0:

        average_score = round(

            sum(scores)
            /
            len(scores),

            1

        )

    else:

        average_score = 0

    if total_leads > 0:

        qualified_rate = round(

            (
                qualified_leads
                /
                total_leads
            ) * 100,

            1

        )

    else:

        qualified_rate = 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📋 Total Leads",
        total_leads
    )

    col2.metric(
        "Qualified Leads",
        qualified_leads
    )

    col3.metric(
        "⭐ Average Score",
        average_score
    )

    col4.metric(
        "📈 Qualified Rate",
        f"{qualified_rate}%"
    )
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


        budget = lead.get(
            "budget",
            0
        )


        if budget is None:

            budget = 0


        budget = int(
            budget
        )


        if budget >= 10000:

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
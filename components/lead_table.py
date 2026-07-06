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



    dataframe = pd.DataFrame(
        leads
    )



    st.dataframe(

        dataframe,

        use_container_width=True

    )
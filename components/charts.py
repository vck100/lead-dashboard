import pandas as pd
import plotly.express as px
import streamlit as st


def display_charts(leads):

    if not leads:
        return

    df = pd.DataFrame(leads)

    col1, col2 = st.columns(2)

    with col1:

        qualification = (
            df["qualification"]
            .fillna("Unknown")
            .value_counts()
            .reset_index()
        )

        qualification.columns = ["Qualification", "Count"]

        fig = px.pie(
            qualification,
            names="Qualification",
            values="Count",
            title="Lead Qualification"
        )

        fig.update_layout(

            title_x=0.5,

            legend_title="",

            margin=dict(

                l=20,

                r=20,

                t=50,

                b=20

    )

)

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.histogram(
            df,
            x="budget",
            title="Budget Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)
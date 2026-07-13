import pandas as pd
import streamlit as st


def display_priority_leads(leads):

    qualified = [
        lead
        for lead in leads
        if str(
            lead.get(
                "qualification",
                ""
            )
        ).lower() == "qualified"
    ]

    qualified = sorted(
        qualified,
        key=lambda x: (
            x.get("score", 0),
            x.get("budget", 0)
        ),
        reverse=True
    )

    qualified = qualified[:5]

    if len(qualified) == 0:
        st.info("No qualified leads found.")
        return

    st.subheader("🔥 Top Priority Leads")

    df = pd.DataFrame(qualified)

    df = df[
        [
            "company",
            "budget",
            "score",
            "qualification"
        ]
    ]

    df = df.rename(
        columns={
            "company": "Company",
            "budget": "Budget",
            "score": "Score",
            "qualification": "Qualification"
        }
    )

    df["Budget"] = df["Budget"].apply(
        lambda x:
            f"£{float(x):,.0f}"
            if pd.notna(x)
            and str(x).strip().lower() != "nan"
            else "N/A"
)
    

    df["Qualification"] = (
    df["Qualification"]
    .fillna("Unknown")
    .str.lower()
    .replace({
        "qualified": "🟢 Qualified",
        "not qualified": "🔴 Not Qualified",
        "unknown": "⚪ Unknown"
    })
)

    for _, row in df.iterrows():

        with st.container():

            st.markdown(
                f"""
    ### 🔥 {row['Company']}

    **Budget:** {row['Budget']}

    **Score:** ⭐ {row['Score']}

    **Status:** {row['Qualification']}

    ---
    """
            )
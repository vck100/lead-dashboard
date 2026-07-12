import streamlit as st


def display_lead_details(leads):

    if not leads:
        return

    companies = sorted(
        list(
            {
                lead.get("company")
                for lead in leads
                if lead.get("company")
            }
        )
    )

    company = st.selectbox(
        "Select Company",
        companies
    )

    lead = next(
        (
            l
            for l in leads
            if l.get("company") == company
        ),
        None
    )

    if not lead:
        return

    st.subheader(company)

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Contact**")
        st.write(lead.get("first_name"))
        st.write(lead.get("last_name"))
        st.write(lead.get("email"))
        st.write(lead.get("phone"))

    with col2:
        st.write("**Lead Information**")
        st.write(f"Budget: £{lead.get('budget'):,}" if lead.get("budget") else "Budget: N/A")
        st.write(f"Qualification: {lead.get('qualification')}")
        st.write(f"Score: {lead.get('score')}")
        st.write(f"Created: {lead.get('created')}")

    st.write("### Notes")
    st.info(
        lead.get("notes") or "No notes available."
    )

    st.write("### AI Insight")
    st.success(
        lead.get("ai_insight") or "No AI insight available."
    )
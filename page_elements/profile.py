import streamlit as st
import sys

sys.path.append('..')

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("## 🎯 Create Your Student Personal Webpage")

st.markdown("""### :material/description:  Requirements

- Build a simple personal student webpage that includes:

    - Personal information
    - About Me section
    - Course table
    - Editable skills table 
            
- This exercise strictly uses only the following Streamlit methods: `st.title`, `st.write`, `st.markdown`, `st.dataframe`, `st.data_editor`, and `st.column_config`. No other Streamlit methods are allowed.
""")

st.divider()

st.markdown("#### :material/ssid_chart: :red[Expected output]")

with st.container(border=True):
    import pandas as pd

    # -------------------------
    # Title Section
    # -------------------------
    st.title("John Zhang")  
    st.write("Year 3 Undergraduate Student")
    st.write("Information Systems Major, HKUST")

    # -------------------------
    # About Me
    # -------------------------
    st.markdown("""
    ### About Me

    I am interested in data analytics, digital innovation, and technology management.

    ##### Interests
    - Programming
    - Startups
    - Artificial Intelligence

    [Visit My University Website](https://www.ust.hk)
    """)

    # -------------------------
    # Courses Table
    # -------------------------
    st.markdown("### Courses Taken")

    courses = pd.DataFrame({
        "Course Code": ["ISOM1010", "ISOM2020", "ISOM3030"],
        "Course Name": [
            "Introduction to IS",
            "Business Programming",
            "Data Analytics"
        ],
        "Semester": ["Fall 2023", "Spring 2024", "Fall 2024"],
        "Grade": ["A", "A-", "B+"]
    })

    st.dataframe(courses)

    # -------------------------
    # Skills (Editable Table)
    # -------------------------
    st.markdown("### Skills")

    skills = pd.DataFrame({
        "Skill": ["Python", "SQL", "Excel"],
        "Proficiency": [4, 3, 5],
        "Years of Experience": [2, 1, 3]
    })

    st.data_editor(
        skills,
        column_config={
            "Proficiency": st.column_config.NumberColumn(format="%d ⭐"),
            "Years of Experience": st.column_config.NumberColumn(format="%d")
        }
    )

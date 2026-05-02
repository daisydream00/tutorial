import streamlit as st
import sys

sys.path.append('..')

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("## 🎯 Create Student Course Dashboard")

st.markdown("### :material/dataset: Data to use")

with st.echo():
    import pandas as pd
    
    course_df = pd.DataFrame(
        {
            "Duration": ["6 weeks", "8 weeks", "10 weeks"],
            "Level": ["Beginner", "Intermediate", "Intermediate"],
            "Students Enrolled": [120, 95, 75],
            "Average Rating": [4.5, 4.7, 4.4],
            "Projects Included": [3, 5, 4]
        },
        index=["Python Basics", "Data Science", "Web Development"]
    )

st.divider()

st.markdown("""### :material/description:  Requirements

- Create a simple Streamlit app that demonstrates layout and interaction features. The app should:
    - Use the title of `"📚 Student Course Dashboard"`
    - Use a sidebar for user input ("Choose a course"). You can obtain the options by using `course_df.index`.
    - Organize content using tabs, "Course Info" and "Statistics".
    - Display information using columns for clean layout. Check the expected output for details.
    - Hint: You can use the `.loc` method in Pandas to retrieve the desired course attribute from the `course_df` DataFrame.
""")

st.divider()

st.markdown("#### :material/ssid_chart: :red[Expected output]")

with st.container(border=True):
    st.title("📚 Student Course Dashboard")
    # ----------------------
    # Sidebar
    # ----------------------
    
    course = st.sidebar.selectbox(
        "Choose a course:",
        course_df.index
    )
    
    # ----------------------
    # Tabs
    # ----------------------
    tab1, tab2 = st.tabs(["Course Info", "Statistics"])

    with tab1:
        st.write(f"### {course} Overview")
        
        # Columns inside tab
        col1, col2 = st.columns(2)
    
        with col1:
            st.write(f"**Duration:** {course_df.loc[course,'Duration']}")
    
        with col2:
            st.write(f"**Level:** {course_df.loc[course,'Level']}")

    with tab2:
        st.write("### Course Statistics")
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.write(f"**Students Enrolled:** {course_df.loc[course,'Students Enrolled']}")
    
        with col2:
            st.write(f"**Average Rating:** {course_df.loc[course,'Average Rating']} ⭐")
    
        with col3:
            st.write(f"**Projects Included:** {course_df.loc[course,'Projects Included']}")
    
    




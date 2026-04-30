import streamlit as st
import sys

sys.path.append('..')

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("## 🎯 Create Student Course Dashboard")

st.markdown("""### :material/description:  Requirements

- Create a simple Streamlit app that demonstrates layout and interaction features. The app should:

    - Use a sidebar for user input (e.g., selecting a course),
    - Organize content using tabs,
    - Display information using columns for clean layout,
    - Include a button that triggers a response (e.g., enrollment confirmation).          
""")

st.divider()

st.markdown("#### :material/ssid_chart: :red[Expected output]")

with st.container(border=True):
   st.title("📚 Student Course Dashboard")
        # ----------------------
    # Sidebar
    # ----------------------
    st.sidebar.header("Course Selection")
    
    course = st.sidebar.selectbox(
        "Choose a course:",
        ["Python Basics", "Data Science", "Web Development"]
    )
    
    st.sidebar.write("Selected:", course)
    
    # ----------------------
    # Tabs
    # ----------------------
    tab1, tab2 = st.tabs(["Course Info", "Statistics"])
    




import streamlit as st

st.set_page_config(layout="centered")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>', unsafe_allow_html= True)
    
# Title
st.title("Streamlit")

# Description Paragraph
st.write("""
Streamlit is an open-source Python library that makes it easy to create **interactive web applications** for data science and machine learning. 
It allows you to turn Python scripts into shareable web apps with **minimal effort**—no frontend (HTML, CSS, JavaScript) experience required!
""")

st.write("""
Streamlit is a **game-changer** for Python developers who want to create web apps without learning full-stack development.
""")

# Section Header
st.markdown("### Key Features of Streamlit")

# Bullet Points
st.markdown("""
✅ **Simple & Fast** – Build apps with just a few lines of Python.

✅ **Interactive Widgets** – Add sliders, buttons, dropdowns, and more.

✅ **Works with Popular Libraries** – Compatible with Pandas, Matplotlib, Plotly, TensorFlow, PyTorch, etc.

✅ **No Web Development Needed** – No need to learn HTML, CSS, or JavaScript.

✅ **Deployable** – Share apps via Streamlit Cloud, AWS, Heroku, etc.
""")
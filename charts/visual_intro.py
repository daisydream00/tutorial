import streamlit as st

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("""## Data visualization

Visualization is a fundamental tool for the modern data scientists. It is often the central lens used
to understand items such as statistical models (for example, via an AUC chart), the distribution
of a crucial variable (via a histogram), or even important business metrics.
                            
Essentially, data visualization is a process of expressing many aspects of our data by ***mapping variables (either discrete or continuous) in our data to various visual elements*** (a.k.a. **aesthetics**) that make up the final graphic, such as position on the x and y axes, colors, shapes, sizes, etc.

<br/>

<img src="https://raw.githubusercontent.com/daisydream00/tutorial/refs/heads/main/static/common-aesthetics.png" width="70%"/>

""", unsafe_allow_html=True)





st.markdown("""
---
## Examples of variable-to-aesthetic mapping
<br/>
<img src="https://raw.githubusercontent.com/daisydream00/tutorial/refs/heads/main/static/iris_datasets.png" width="80%"/>
<br/>
            
<img src="https://raw.githubusercontent.com/daisydream00/tutorial/refs/heads/main/static/iris_3_plots.png" width="80%">
<br/>
            
- Discrete (or categorical) variables: positions, marker shapes, line types, colors (on a discrete scale), etc.
- Continuous variables: positions, sizes, widths, colors (on a continuous scale), etc.


> Check out [this link](https://clauswilke.com/dataviz/aesthetic-mapping.html) if you want to know more about data visualization.

""", unsafe_allow_html=True)


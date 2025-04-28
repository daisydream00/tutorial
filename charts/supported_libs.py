import streamlit as st
import plotly.express as px
import altair as alt

import sys

sys.path.append('..')

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.markdown("""
As we've seen, Streamlit built-in charting functions can be useful if we want to visualize data quickly, but we trade off speed for customizability.

In production, more powerful libraries, such as Matplotlib, Seaborn, Plotly, and Altair, can give us the flexibility and customizability we want. 

Streamlit supports several popular Python visualization libraries. The rest of this section will provide a walk-through of Plotly for interactive plotting.
""")

st.markdown("### :material/dataset: Data to use")

with st.echo():
    import pandas as pd
    
    gapminder = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder-unclean.csv").dropna()
    
    st.write(gapminder)

st.divider()



st.markdown("### :material/list_alt: [`st.plotly_chart()`](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart)")


st.markdown("""<br/>

[Plotly](https://plotly.com/) is an interactive visualization library that is popular among data scientists. This library is very similar to Streamlit in its intent and useful in creating interactive visuals and dashboards.
            
Streamlit makes it easy to integrate Plotly graphs into your apps using the `st.plotly_chart()` function. This seamless integration allows you to quickly incorporate Plotly visuals and dashboards into your Streamlit application.
""", unsafe_allow_html=True)


st.markdown("#### :material/code_blocks: :blue[Source code to run]")

code = """
# to run this snippet on your computer, you need to first install Plotly using pip install plotly
import plotly.express as px

fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", color='continent',
                 log_x=True, range_x=[100, 100000], range_y=[25, 90], size_max=55,
                 color_discrete_sequence=px.colors.qualitative.Set1,
                 labels={'gdpPercap': 'GDP Per Capita', 'lifeExp': 'Life Expectancy', "continent": "Continent"},
                 animation_frame="year", animation_group="country",
                 width=800, height=500)
st.plotly_chart(fig)
"""



with st.container(border=True):
    st.code(code)

st.markdown("#### :material/animation: :red[Rendered output]") 

with st.container(border=True):
    # https://plotly.com/python/discrete-color/
    fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", size="pop", color='continent',
                     log_x=True, range_x=[100, 100000], range_y=[25, 90], size_max=55,
                     color_discrete_sequence=px.colors.qualitative.Set1,
                     labels={'gdpPercap': 'GDP Per Capita', 'lifeExp': 'Life Expectancy', "continent": "Continent"},
                     animation_frame="year", animation_group="country",
                     width=800, height=500)
    #fig.update_layout(legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    st.plotly_chart(fig)



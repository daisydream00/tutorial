import streamlit as st

import sys

sys.path.append('..')

st.set_page_config(layout="wide")

with open( "static/font.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.markdown("## 🎯 Dynamic charting for stock price comparison")
            
st.markdown("### :material/dataset: Data to use")

with st.echo():
    import pandas as pd
    
    source = pd.read_csv(
        "https://raw.githubusercontent.com/vega/vega-datasets/main/data/stocks.csv", 
        parse_dates=['date'], date_format="%b %d %Y"
        ).query(f"date < 2010 and date >= 2005")

    st.dataframe(source)

st.divider()

st.markdown("""### :material/description:  Requirements

- Include a multiselect widget (`st.multiselect()`) to choose which stocks should be included for plotting; the default values are `'AMZN'` and `'AAPL'`.
 
- Include a slider widget (`st.slider()`) to indicate a specific year over which stocks are compared; the range is 2005 - 2009; the default value is 2006.

- Include a checkbox widget (`st.checkbox()`) to indicate if the user wants to compare stocks for the whole period. The slider widget should be disabled when this widget is checked.

- When none of the stocks are selected, display an error message, saying "Please select at least one stock!";
            
- Tips:
    - Recall how `st.line_chart()` allows us to align variables with desired aesthetics;
    - Use the `.unique()` method to obtain the unique values of `symbol` column in the dataframe;
    - [`DataFrame.query()`](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method) can be used to filter data for plotting, 
        - e.g., if your variable that holds the selected stocks is called `stocks` and that holds the specified year is called `year`, `.query(f"date < {year + 1} and date >= {year} and symbol in {stocks}")` will give you the desired subset.
    - Use the [`disabled`](https://docs.streamlit.io/develop/api-reference/widgets/st.slider) option of `st.slider()` to control when to disable the slider.
""")

st.divider()

st.markdown("#### :material/widgets: :red[Expected output]")

with st.container(border=True):
    stocks = st.multiselect("Select stocks for comparison", source.symbol.unique(), ['AMZN', 'AAPL'])
    all_years = st.checkbox("Show prices for the whole period")
    year = st.slider("Select a year", min_value=2005, max_value=2009, value=2006, disabled=all_years)
 

    if not stocks:
        st.error("Please select at least one stock!")
    else:
        if not all_years:
            st.markdown(f"### Stock prices in {year}")
            chart_data = source.query(f"date < {year + 1} and date >= {year} and symbol in {stocks}")
        else:
            st.markdown(f"### Stock prices in all years")
            chart_data = source.query(f"symbol in {stocks}")  
        st.line_chart(chart_data, x="date", y="price", color="symbol", 
                      width=720, height=500)


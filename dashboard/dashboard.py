import streamlit as st
import pandas as pd
 
# (1) scrape the tickers/symbols of S&P 100 companies from the [Wikipedia page](https://en.wikipedia.org/wiki/S%26P_100); and (2) 
st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.markdown("""### :material/description:  Requirements
- Please download `In-Class Exercise_5_part1.ipynb` from Canvas. Complete the code to extract relevant info from the **`yfinance`** libarary to generate two files `ticker_info.csv` and `stock_data.csv` (The two data files are also available on Canvas if you want to start with the second part first). Place these two files into your streamlit project folder and complete
this second part of this exercise, which is to set up a streamlit application.
            
- Include a sidebar (`with st.`sidebar`) that contains the following widgets:
    - A checkbox widget (`st.checkbox()`) that alows the user to control whether to show a bar chart that visualizes the market cap of S&P 100 stocks by sector; the default value is checked.
    - A multiselect widget (`st.multiselect()`) that allows the user to choose which stocks should be included for plotting; the options are S&P 100 tickers; the default values are `'TSLA'`, `'NVDA'`, and `'AAPL'`.
    - A slider widget (`st.slider()`) that allows the user to specify the year range over which stocks are compared; the range is 2020 - 2025; the default value is 2004 - 2025.

- If the checkbox is checked, display a bar chart that visualizes the market cap of S&P 100 stocks by sector.

- If none of the stocks are selected, display an error message: "Please select at least one stock!"; 
  if stocks are selected, show a line chart for closing prices (using the column 'Close') and a bar chart for volume (using the column 'Volume').
            
- Tips:
    - Use the `.unique()` method to obtain the unique values of `Ticker` column in the Pandas dataframe `ticker_info`;
    - [`DataFrame.query()`](https://pandas.pydata.org/docs/user_guide/indexing.html#the-query-method) can be used to filter data for plotting, 
        - e.g., if the variable holding the selected stocks is `selected_tickers` and the variable holding the year range is `selected_years`, `query(f"Date < {selected_years[1] + 1} and Date >= {selected_years[0]} and Ticker in {selected_tickers}")` will give you the desired subset of data.
""")          


st.divider()

st.markdown("#### :material/widgets: :red[Expected output]")

st.divider()


# load stock info and data
ticker_info = pd.read_csv("https://raw.githubusercontent.com/daisydream00/tutorial/refs/heads/main/static/ticker_info.csv")
stock_data = pd.read_csv("https://raw.githubusercontent.com/daisydream00/tutorial/refs/heads/main/static/stock_data.csv", parse_dates=['Date'])

# extract S&P 100 tickers from ticker_info
tickers_100 = ticker_info.Ticker.unique()

# set page title
st.title("S&P 100 Stock Dashboard 📊")  #:bar_chart:

# Sidebar controls
with st.sidebar:
    st.header("Sidebar Widgets")

    show_sector = st.checkbox("Show Market Cap by Sector", True)

    selected_tickers = st.multiselect(
        "Select Companies",
        options=tickers_100,
        default=['TSLA', 'NVDA', 'AAPL']
    )

    # Year range slider
    selected_years = st.slider(
        "Select Year Range",
        min_value=2020,
        max_value=2025,
        value=(2024, 2025)
    )

if show_sector:
    st.header("Market Cap by Sector")
    st.bar_chart(ticker_info, x="Sector", y="Market Cap (B)", color="Ticker", horizontal=True,
            width=720, height=500)

if selected_tickers:

    chart_data = stock_data.query(f"Date < {selected_years[1] + 1} and Date >= {selected_years[0]} and Ticker in {selected_tickers}")

    st.header(f"Stock Trend Analysis ({selected_years[0]} - {selected_years[1]})")
    
    # Closing Prices
    st.subheader("Closing Prices")
    st.line_chart(chart_data, x="Date", y="Close", color="Ticker",
                  width=720, height=500)

    
    # Volume Analysis
    st.subheader("Trading Volume")
    st.bar_chart(chart_data, x="Date", y="Volume", color="Ticker",
                  width=720, height=500)

else:
    st.error("Please select at least one company")

import streamlit as st
import pandas as pd
 

st.set_page_config(page_title="Stock Dashboard", layout="wide")
st.markdown("""### :material/description:  Requirements
""")

st.divider()

st.markdown("#### :material/widgets: :red[Expected output]")

st.divider()

st.title("S&P 100 Stock Dashboard 📊")  #:bar_chart:

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

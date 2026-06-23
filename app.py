import streamlit as st
from stock_agent import run_agent

st.set_page_config(
    page_title="Stock Market Assistant",
    page_icon="📈"
)

st.title("📈 Stock Market Assistant")

st.write(
    "Enter a company name or stock symbol to get stock information."
)

query = st.text_input(
    "Company Name or Symbol",
    placeholder="Apple, Tesla, Microsoft, Nvidia, AAPL..."
)

if st.button("Get Stock Price"):

    if not query.strip():

        st.warning("Please enter a stock name.")

    else:

        with st.spinner("Fetching stock data..."):

            result = run_agent(query)

        st.success("Stock Information")

        st.code(result)
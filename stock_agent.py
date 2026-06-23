from openai import OpenAI
import json
import yfinance as yf

# =========================
# OLLAMA CLIENT
# =========================
client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama"
)

# =========================
# STOCK TOOL
# =========================
def get_stock_price(symbol: str):

    try:
        stock = yf.Ticker(symbol.upper())
        info = stock.info

        current_price = info.get("currentPrice")

        if current_price is None:
            return "Stock data not found"

        return (
            f"Symbol: {symbol.upper()}\n"
            f"Current Price: {current_price}\n"
            f"Previous Close: {info.get('previousClose')}\n"
            f"Open: {info.get('open')}\n"
            f"Day High: {info.get('dayHigh')}\n"
            f"Day Low: {info.get('dayLow')}\n"
            f"Volume: {info.get('volume')}"
        )

    except Exception as e:
        return f"Error: {str(e)}"


available_tools = {
    "get_stock_price": get_stock_price
}

SYSTEM_PROMPT = """
You are a Stock Market Assistant.

You ONLY have ONE tool:
get_stock_price(symbol)

Examples:
Apple -> AAPL
Tesla -> TSLA
Microsoft -> MSFT
Nvidia -> NVDA
Infosys -> INFY
Amazon -> AMZN
Google -> GOOGL

Return ONLY JSON.

Example:

{
    "step":"action",
    "function":"get_stock_price",
    "input":"AAPL"
}
"""


def run_agent(query):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": query
        }
    ]

    response = client.chat.completions.create(
        model="qwen2.5-coder:3b",
        response_format={"type": "json_object"},
        messages=messages
    )

    assistant_response = response.choices[0].message.content

    print("RAW RESPONSE:", assistant_response)

    try:
        parsed_response = json.loads(assistant_response)

    except Exception:
        return "Invalid JSON received from model"

    if parsed_response.get("step") == "action":

        tool_name = parsed_response.get("function")
        tool_input = parsed_response.get("input")

        output = available_tools[tool_name](tool_input)

        # RETURN TOOL OUTPUT DIRECTLY
        return output

    return "Unable to process request"


# Terminal Mode
if __name__ == "__main__":

    while True:

        query = input("> ")

        if query.lower() == "exit":
            break

        print(run_agent(query))
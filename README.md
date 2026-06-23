# 📈 Stock Market Assistant

A simple Agentic AI project built using Streamlit, Ollama, Qwen2.5-Coder, and Yahoo Finance.

The application allows users to enter a company name or stock symbol and retrieve real-time stock information.

## Features

* AI-powered stock query handling
* Uses local LLM through Ollama
* Fetches live stock market data using Yahoo Finance
* Streamlit web interface
* Supports company names and stock symbols

## Tech Stack

* Python
* Streamlit
* Ollama
* Qwen2.5-Coder
* Yahoo Finance (yfinance)

## Architecture

User Query
↓
Qwen2.5-Coder (Ollama)
↓
Tool Selection
↓
get_stock_price()
↓
Yahoo Finance API
↓
Stock Information
↓
Streamlit UI

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/stock-market-assistant.git
cd stock-market-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Download and install Ollama:

https://ollama.com

Pull the model:

```bash
ollama pull qwen2.5-coder:3b
```

Start Ollama:

```bash
ollama serve
```

### 6. Run Application

```bash
streamlit run app.py
```

## Example Queries

* Apple
* Tesla
* Microsoft
* Nvidia
* AAPL
* TSLA
* MSFT
* NVDA

## Sample Output

```text
Symbol: AAPL
Current Price: 214.35
Previous Close: 213.50
Open: 212.80
Day High: 216.00
Day Low: 210.75
Volume: 51234567
```

## Learning Concepts

* Agentic AI
* Function Calling
* Tool Use
* Streamlit UI Development
* Local LLM Deployment
* Yahoo Finance Integration

## Author

N Sai Niharika

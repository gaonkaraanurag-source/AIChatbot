# AIChatbot
# Sales & Marketing Insights Chatbot

A Python CLI project that uses LangChain, Groq, pandas, and NumPy to analyze sales and marketing campaign data. The chatbot helps users ask natural language questions about customer behavior, product category sales, campaign response, and revenue performance.

## Project Overview

This project loads a Superstore marketing campaign dataset from a CSV file, calculates key business metrics, and sends a structured data summary to a Groq-hosted LLM through LangChain. The model then returns business-friendly insights based on the dataset.

## Features

- Reads sales and marketing campaign data from a CSV file.
- Calculates total customer spend across product categories.
- Identifies top customers by total spend.
- Finds top product categories by sales.
- Calculates total revenue generated.
- Measures campaign promotion success using the `Response` column.
- Supports natural language Q&A about the dataset.

## Tech Stack

- Python
- LangChain
- Groq
- pandas
- NumPy
- getpass
- Environment variables

## Dataset

The dataset contains customer and campaign information from a previous marketing campaign.

Key columns include:

- `Response`: 1 if the customer accepted the campaign offer, 0 otherwise
- `Id`: Unique customer ID
- `Income`: Customer yearly household income
- `MntWines`, `MntFruits`, `MntMeatProducts`, `MntFishProducts`, `MntSweetProducts`, `MntGoldProds`: Product category spend
- `NumDealsPurchases`: Purchases made with discounts
- `NumWebPurchases`: Website purchases
- `NumCatalogPurchases`: Catalog purchases
- `NumStorePurchases`: Store purchases
- `NumWebVisitsMonth`: Website visits in the last month
- `Recency`: Days since last purchase
- `Complain`: Whether the customer complained in the last 2 years

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install pandas numpy langchain-groq
```

## API Key

The project uses a Groq API key. If `GROQ_API_KEY` is not already set, the script asks for it securely:

```python
os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
```

You can also export it before running:

```bash
export GROQ_API_KEY="your_groq_api_key_here"
```

Do not hardcode API keys in your code or commit them to GitHub.

## Run

Update the CSV path in the script if needed, then run:

```bash
python StoreMarketing_Insights.py
```

Example questions:

```text
What are the top sales and marketing insights?
Who are the top customers?
Which product category generated the most sales?
Was the promotion successful?
What should the marketing team focus on?
```

Type `exit` or `quit` to stop the program.

## How It Works

1. Loads the CSV dataset with pandas.
2. Uses NumPy to calculate business metrics.
3. Creates a summary of the dataset and calculated metrics.
4. Sends the summary and user question to a Groq LLM through LangChain.
5. Prints business insights in natural language.

## Future Improvements

- Add chat memory for follow-up questions.
- Add visual charts for campaign and product performance.
- Move API key handling to a `.env` file.
- Add more detailed customer segmentation.
- Add RAG for retrieving insights from larger internal documents and reports.

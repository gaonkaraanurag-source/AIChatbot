import pandas as pd
import os
import getpass
from langchain_groq import ChatGroq
#from langchain.tools import Tool



# import CSV super store dataset
df = pd.read_csv('/Users/anuraggaonkar/Desktop/Projects/Chatbot/SuperStore Data/superstore_data.csv')

print(df.shape)  # Print the shape of the dataset (rows, columns)
print(df.head()) # First 5 rows of the dataset
print(df.columns.tolist()) # Print the column names of the dataset

# Enter the Gorq API key if not already set in the environment variables
if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")


data_summary = f"""
Dataset shape:
{df.shape}

Column names:
{df.columns.tolist()}

First 5 rows:
{df.head().to_string()}

Numeric summary:
{df.describe().to_string()}
"""

# Select Groq model
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

messages = [
    (
        "system",
        "You are a sales and marketing data analyst. "
        "Use only the dataset summary provided by the user. "
        "Give clear business insights, not generic advice.",
    ),
    (
        "human",
        f"""
Here is a summary of our sales and marketing dataset:

{data_summary}

Question:
What are the top 5 sales and marketing insights from this data?
""",
    ),
]

ai_msg = llm.invoke(messages)

print("\nAI Insights:")
print(ai_msg.content)


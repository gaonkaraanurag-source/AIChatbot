import pandas as pd
import os
import getpass
import numpy as np
from langchain_groq import ChatGroq
#from langchain.tools import Tool



# import CSV super store dataset
df = pd.read_csv('/Users/anuraggaonkar/Desktop/Projects/Chatbot/SuperStore Data/superstore_data.csv')

print(df.shape)  # Print the shape of the dataset (rows, columns)
print(df.head()) # First 5 rows of the dataset
print(df.columns.tolist()) # Print the column names of the dataset

#Lets create calculate measures from the dataset

product_columns = [
    "MntWines",
    "MntFruits",
    "MntMeatProducts",
    "MntFishProducts",
    "MntSweetProducts",
    "MntGoldProds",
]

# Convert product spend columns to a NumPy array
product_spend_array = df[product_columns].to_numpy()

# Total spend per customer
df["TotalSpend"] = np.sum(product_spend_array, axis=1)

# Total revenue generated
total_revenue = np.sum(df["TotalSpend"].to_numpy())

# Top customers by total spend
top_customer_indexes = np.argsort(df["TotalSpend"].to_numpy())[::-1][:10]
top_customers = df.iloc[top_customer_indexes][["Id", "Income", "TotalSpend", "Response"]]

# Total sales by product category
product_sales_values = np.sum(product_spend_array, axis=0)

# Sort product categories by sales
sorted_product_indexes = np.argsort(product_sales_values)[::-1]
top_product_categories = [
    (product_columns[index], product_sales_values[index])
    for index in sorted_product_indexes
]

# Promotion success metrics
response_array = df["Response"].to_numpy()

total_customers = len(response_array)
accepted_customers = np.sum(response_array)
promotion_success_rate = accepted_customers / total_customers * 100

# Average spend for customers who accepted vs did not accept offer
accepted_spend = df.loc[df["Response"] == 1, "TotalSpend"].to_numpy()
not_accepted_spend = df.loc[df["Response"] == 0, "TotalSpend"].to_numpy()

average_spend_accepted = np.mean(accepted_spend)
average_spend_not_accepted = np.mean(not_accepted_spend)

business_metrics = f"""
Total customers:
{total_customers}

Customers who accepted the campaign offer:
{accepted_customers}

Promotion success rate:
{promotion_success_rate:.2f}%

Total revenue generated from product spend:
${total_revenue:,.2f}

Top product categories by sales:
{top_product_categories}

Top 10 customers by total spend:
{top_customers.to_string(index=False)}

Average spend for customers who accepted the campaign:
${average_spend_accepted:,.2f}

Average spend for customers who did not accept the campaign:
${average_spend_not_accepted:,.2f}
"""

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

system_messages = (
            "You are a sales and marketing data analyst. "
            "Use only the dataset summary provided by the user. "
            "Give clear business insights, not generic advice."
            "If the dataset summary does not contain enough information to answer, say what is missing."
    )
print("\nSales & Marketing Insights Q&A Bot")
print("Ask a question about the dataset.")
print("Type 'exit' to quit.\n")

while True:
    questions=input("Enter your question: ")
    if questions.lower() in ['exit', 'quit']:
        print("Exiting the program.")
        break
    messages =[
        ("system", system_messages),
        (
            "human",
        f"""
Here is a summary of our sales and marketing dataset:

{data_summary}

Question:
{questions}
""",
    ),
]

ai_msg = llm.invoke(messages)

print("\nAI Insights:")
print(ai_msg.content)


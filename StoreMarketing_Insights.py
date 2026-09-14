import pandas as pd

# import CSV super store dataset
df = pd.read_csv('/Users/anuraggaonkar/Desktop/Projects/Chatbot/SuperStore Data/superstore_data.csv')

print(df.shape)  # Print the shape of the dataset (rows, columns)
print(df.head()) # First 5 rows of the dataset
print(df.columns.tolist()) # Print the column names of the dataset



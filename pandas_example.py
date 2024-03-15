import pandas as pd

# Read the Excel sheet into a pandas DataFrame
df = pd.read_excel('pandas_example.xlsx')
# df = pd.read_excel('pandas_example.xlsx', header=None)  # deal with no header

# Display the DataFrame
print(df)

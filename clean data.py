import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("Chocolate Sales.csv")

# Step 2: Display basic info
print("Initial Data Info:")
print(df.info())

# Step 3: Remove any leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Step 4: Remove duplicates
df = df.drop_duplicates()

# Step 5: Clean 'Amount' column - remove $ and commas, convert to float
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)

# Step 6: Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], format="%d-%b-%y")

# Step 7: Standardize text columns (title case, no extra spaces)
text_columns = ['Sales Person', 'Country', 'Product']
for col in text_columns:
    df[col] = df[col].str.strip().str.title()

# Step 8: Rename columns to lowercase with underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Step 9: Final check
print("\nCleaned Data Info:")
print(df.info())

# Step 10: Save cleaned data
df.to_csv("chocolate_sales_cleaned.csv", index=False)

print("\n✅ Data cleaning complete! Cleaned file saved as 'chocolate_sales_cleaned.csv'")

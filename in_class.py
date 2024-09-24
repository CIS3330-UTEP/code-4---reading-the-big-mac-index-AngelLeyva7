import pandas as pd

df = pd.read_csv('./big-mac-full-index.csv')

print(df)
country_code = "USA"
query = f"(iso_a3 == '{country_code}')"

print(len(df))
df1 = df.query(query)
print(len(df1))
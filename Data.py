import pandas as pd

df = pd.read_csv("C:/Users/ramma/Downloads/sales_data.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

monthly_sales = df.groupby(['Month', 'Year', 'Cars'])['Sales'].sum().reset_index()

monthly_sales = monthly_sales.sort_values(by=['Month', 'Year', 'Sales'], ascending=[True, True, False])

top_products = monthly_sales.groupby(['Month', 'Year']).head(5)

for (month, year), group in top_products.groupby(['Month', 'Year']):
    print(group)

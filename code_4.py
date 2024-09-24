import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv('big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    file = df[(df['date'].str.startswith(str(year))) & (df['iso_a3'].str.lower() == country_code.lower())]
    price = file['dollar_price'].mean()
    return round(price,2)

def get_big_mac_price_by_country(country_code):
    file = df[df['iso_a3'].str.lower() == country_code]
    price = file['dollar_price'].mean()
    return round(price,2)

def get_the_cheapest_big_mac_price_by_year(year):
    file = df[df['date'].str.startswith(str(year))]
    cheapest = file['dollar_price'].min()
    row = file[file['dollar_price'] == cheapest].iloc[0]
    name = row['name'] 
    code = row['iso_a3']
    price = row['dollar_price']
    return f"{name} {code}: ${round(price,2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    file = df[df['date'].str.startswith(str(year))]
    most_expensive = file['dollar_price'].max()
    row = file[file['dollar_price'] == most_expensive].iloc[0]
    name = row['name']
    code = row['iso_a3']
    price = row['dollar_price']
    return f"{name} {code}: ${round(price,2)}"


if __name__ == "__main__":
    test_1 = get_big_mac_price_by_year('2021','usa')
    print(test_1)
    
    test_2 = get_big_mac_price_by_country('usa')
    print(test_2)
    
    test_3 = get_the_cheapest_big_mac_price_by_year('2022')
    print(test_3)
    
    test_4 = get_the_most_expensive_big_mac_price_by_year('2002')
    print(test_4)
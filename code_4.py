import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    """Returns the average Big Mac price in USD for a given year and country."""
    filtered_df = df[(df['date'].str.startswith(str(year))) & (df['iso_a3'].str.lower() == country_code.lower())]
    return round(filtered_df['dollar_price'].mean(), 2) if not filtered_df.empty else None

def get_big_mac_price_by_country(country_code):
    """Returns the average Big Mac price in USD for a given country."""
    filtered_df = df[df['iso_a3'].str.lower() == country_code.lower()]
    return round(filtered_df['dollar_price'].mean(), 2) if not filtered_df.empty else None

def get_the_cheapest_big_mac_price_by_year(year):
    """Returns the country with the cheapest Big Mac for a given year."""
    filtered_df = df[df['date'].str.startswith(str(year))]
    if not filtered_df.empty:
        cheapest = filtered_df.loc[filtered_df['dollar_price'].idxmin()]
        return f"{cheapest['name']} ({cheapest['iso_a3']}): ${round(cheapest['dollar_price'], 2)}"
    return None

def get_the_most_expensive_big_mac_price_by_year(year):
    """Returns the country with the most expensive Big Mac for a given year."""
    filtered_df = df[df['date'].str.startswith(str(year))]
    if not filtered_df.empty:
        expensive = filtered_df.loc[filtered_df['dollar_price'].idxmax()]
        return f"{expensive['name']} ({expensive['iso_a3']}): ${round(expensive['dollar_price'], 2)}"
    return None

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2008, "usa"))
    print(get_big_mac_price_by_country("usa"))
    print(get_the_cheapest_big_mac_price_by_year(2008))
    print(get_the_most_expensive_big_mac_price_by_year(2003))
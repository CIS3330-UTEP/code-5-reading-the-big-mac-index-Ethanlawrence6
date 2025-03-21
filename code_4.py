import pandas as pd 

df = pd.read_csv("big-mac-full-index.csv")
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year

def get_big_mac_price_by_year(year, country_code):
    filtered = df[(df["year"] == year) & (df['iso_a3'].str.lower() == country_code.lower())]
    mean_price = filtered['dollar_price'].mean()
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    filtered = df[df['iso_a3'].str.lower() == country_code.lower()]
    mean_price = filtered['dollar_price'].mean()
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    filtered = df[df["year"] == year]
    min_row = filtered.loc[filtered['dollar_price'].idxmin()]
    country_name = min_row['name']
    country_code = min_row['iso_a3']
    price = round(min_row['dollar_price'], 2)
    return f"{country_name} ({country_code}): ${price}"

def get_the_most_expensive_big_mac_price_by_year(year):
    filtered = df[df["year"] == year]
    max_row = filtered.loc[filtered['dollar_price'].idxmax()]
    country_name = max_row['name']
    country_code = max_row['iso_a3']
    price = round(max_row['dollar_price'], 2)
    return f"{country_name} ({country_code}): ${price}"

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2008, "mys"))  
    print(get_big_mac_price_by_country("usa"))      
    print(get_the_cheapest_big_mac_price_by_year(2008))  
    print(get_the_most_expensive_big_mac_price_by_year(2003)) 
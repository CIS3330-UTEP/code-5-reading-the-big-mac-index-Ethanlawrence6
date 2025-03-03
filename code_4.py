import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    """
    Returns the average Big Mac price in USD for a given year and country.
    """
    filtered_df = df[(df['date'].str.startswith(str(year))) & (df['iso_a3'].str.lower() == country_code.lower())]

    if not filtered_df.empty:
        return round(filtered_df['dollar_price'].mean(), 2)
    return None
    
def get_big_mac_price_by_country(country_code):
    """
    Returns the average Big Mac price in USD for a given country across all years.
    """
    filtered_df = df[df['iso_a3'].str.lower() == country_code.lower()]

    if not filtered_df.empty:
        return round(filtered_df['dollar_price'].mean(), 2)
    return None

def get_the_cheapest_big_mac_price_by_year(year):
    """
    Returns the country with the cheapest Big Mac for a given year.
    """
    filtered_df = df[df['date'].str.startswith(str(year))]
    if not filtered_df.empty:
        cheapest = filtered_df.loc[filtered_df['dollar_price'].idxmin()]
        return f"{cheapest['name']} ({cheapest['iso_a3']}): ${round(cheapest['dollar_price'], 2)}"
    return None

def get_the_most_expensive_big_mac_price_by_year(year):
    """
    Returns the country with the most expensive Big Mac for a given year.
    """
    filtered_df = df[df['date'].str.startswith(str(year))]
    if not filtered_df.empty:
        expensive = filtered_df.loc[filtered_df['dollar_price'].idxmax()]
        return f"{expensive['name']} ({expensive['iso_a3']}): ${round(expensive['dollar_price'], 2)}"
    return None

if __name__ == "__main__":

    while True:
        print("\nBig Mac Index Data Query")
        print("1. Get Big Mac price by Year & Country")
        print("2. Get Big Mac price by Country")
        print("3. Get the cheapest Big Mac by Year")
        print("4. Get the most expensive Big Mac by Year")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            year=input("Enter the year (YYYY): ")
            country_code = input("Enter the country code (ISO A3 format, e.g., USA, CAN, GBR): ")
            result = get_big_mac_price_by_year(year,country_code)
            print(f"Big Mac price in {country_code.upper()} for the year {year}: ${result}" if result else "No data found.")

        elif choice == '2':
            country_code = input("Enter the country code (ISO A3 format, e.g., USA, CAN, GBR): ")
            result = get_big_mac_price_by_country(country_code)
            print(f"Average Big Mac price in {country_code.upper()}: ${result}" if result else "No data found.")

        elif choice == '3':
            year=input("Enter the year (YYYY): ")
            result = get_the_cheapest_big_mac_price_by_year(year)
            print(result if result else "No data found.")

        elif choice == '4':
            year=input("Enter the year (YYYY): ")
            result = get_the_most_expensive_big_mac_price_by_year(year)
            print(result if result else "No data found.")
        
        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
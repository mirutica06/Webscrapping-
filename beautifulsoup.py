import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://web-scraping.dev/products"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
scraped_data = []

def fetch_and_parse(url):
    print(f"--- Fetching {url} ---")
    time.sleep(1)
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_product_data(soup):
    """Extracts product data from the website."""

    product_containers = soup.select('div.product')

    if not product_containers:
        print("No product containers found. Check the CSS selector.")
        return

    for product in product_containers:

        title = product.select_one('a') # Target the anchor tag inside the product container
        title = title.text.strip() if title else 'N/A'

        price_raw = product.select_one('.price')
        price_raw = price_raw.text.strip() if price_raw else 'N/A'

        description = product.select_one('.description')
        description = description.text.strip() if description else 'N/A'

        scraped_data.append({
            'Title': title,
            'Price_Raw': price_raw,
            'Description': description
        })

    print(f"Successfully scraped {len(scraped_data)} products.")

def clean_and_save(data):
    if not data:
        print("No data was scraped to clean.")
        return

    df = pd.DataFrame(data)

    df['Price'] = pd.to_numeric(
        df['Price_Raw'].str.replace('$', '').str.replace(',', ''),
        errors='coerce'
    )

    df_final = df[['Title', 'Price', 'Description']]
    df_final.to_csv('products_output_cleaned.csv', index=False, encoding='utf-8')
    df_final.to_excel('products_output_cleaned.xlsx', index=False)
    print("\n✅ Data cleaning complete. Saved to 'products_output_cleaned.csv'.")
    print("\n--- Final DataFrame Head ---")
    print(df_final.head())

if __name__ == "__main__":
    soup = fetch_and_parse(URL)
    if soup:
        extract_product_data(soup)
        if scraped_data:
            clean_and_save(scraped_data)
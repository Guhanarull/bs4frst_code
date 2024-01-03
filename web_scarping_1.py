import requests
from bs4 import BeautifulSoup

# List of URLs
url_list = "https://www.cabelas.com/shop/en/garmin-epix-pro-gen-2-standard-edition-smartwatch"

for url in url_list:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        inmage_url = soup.select_one('//*[@id="offerPrice_3074457345624703740"]/span').get('href')

        print("URL:", url)
        print("Extracted URL:", inmage_url)
    else:
        # Skip URLs with non-200 status codes
        print(f"Skipping URL: {url}, Status code: {response.status_code}")

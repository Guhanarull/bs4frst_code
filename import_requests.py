import requests
from bs4 import BeautifulSoup

url = "https://www.cabelas.com/shop/en/garmin-epix-pro-gen-2-standard-edition-smartwatch"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the element containing the price
    # You might need to inspect the HTML structure of the page to find the appropriate tag and class
    price_element = soup.find('span', {'class': 'price'})

    if price_element:
        # Extract the price text
        price = price_element.get_text(strip=True)

        print(f"The price is: {price}")
    else:
        print("Price not found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

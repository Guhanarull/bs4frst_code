import requests
from bs4 import BeautifulSoup

# List of URLs
url_list = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
]

for url in url_list:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        inmage_url = soup.select_one('#mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(2) > td > a').get('href')

        print("URL:", url)
        print("Extracted URL:", inmage_url)
    elif response.status_code == 404:
        print(f"Page not found for URL: {url}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

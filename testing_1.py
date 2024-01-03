import requests
from lxml import html

# Specify the URL of the webpage
url = "https://github.com/"

# Send an HTTP request to the URL and get the content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with lxml
tree = html.fromstring(html_content)

# Use XPath to find the desired element
xpath = '//*[@id="dashboard"]/div/feed-container/div[1]/h3'
result = tree.xpath(xpath)

# Check if the element is found
if result:
    # Print the text content of the found element
    print("Scraped Data:", result[0].text_content())
else:
    print("Element not found. Check the XPath or the structure of the webpage.")

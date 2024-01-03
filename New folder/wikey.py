import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Theropithecus"

a = requests.get(url)
b = a.content

soup = BeautifulSoup(b, "html.parser")

try:
    css_selector = "#mw-content-text > div.mw-content-ltr.mw-parser-output > table"
    span_element = soup.select_one(css_selector)
    if span_element:
        print("output is:", span_element.text.strip())
    else:
        print("do it now")

finally:
    print()


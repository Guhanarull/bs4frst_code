import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/17436014/selenium-versus-beautifulsoup-for-web-scraping"

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")


try:
    CSS_SELECTOR = "#question-header > h1 > a"
    span_element= soup.select_one(CSS_SELECTOR)

    if span_element:
        print("output is:", span_element.text.strip())
    else:
        print("don't_giveup") 

finally:
    print()     
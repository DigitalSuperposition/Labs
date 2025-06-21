from bs4 import BeautifulSoup
import requests
import time

#headers = {
    "User-Agent": "Edg/137.0.3296.83 (Windows NT 10.0; Win64; x64)"
}

url: https://www.barchart.com/stocks/quotes/-SAMI/components?viewName=technical&orderBy=symbolName&orderDir=asc
 
time.sleep(5)

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")  

soup.find("div", div="div.barchart-content-block.invisible.visible")

print(response, response.text, requests.get)

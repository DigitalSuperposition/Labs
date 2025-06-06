from bs4 import BeautifulSoup
import requests
import time
 
url = "https://finance.yahoo.com/markets/stocks/gainers/"

time.sleep(5)

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")                      

print(response, response.text, requests.get)



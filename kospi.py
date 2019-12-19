import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/sise/"

request = requests.get(url).text
#  print(request)

soup = BeautifulSoup(request, 'html.parser')
#print(soup)
kospi = soup.select_one('#KOSPI_now')
print(kospi.text)

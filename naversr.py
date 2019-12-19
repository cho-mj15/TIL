import requests
from bs4 import BeautifulSorp


url = "https://www.naver.com"

req = requests.get(url).text
data = BeautifulSorp(req, 'html.parser')
sel = '#PM_ID_ct > div.header > div.selection_navbar > div.area_hotkeyword PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ak_h'
search = data.select(sel)

for item in search:
   print(item.text)


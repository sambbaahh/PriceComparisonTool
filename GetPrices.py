from bs4 import BeautifulSoup
import requests
import re

url = "https://www.jimms.fi/fi/Product/Show/183386/gv-n3070eagle-oc-8gd-2-0/gigabyte-geforce-rtx-3070-eagle-oc-rev-2-0-lhr-naytonohjain-8gb-gddr6"


result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
prices = doc.findAll('span',{'itemprop' : 'price'}, text= True)[0].text

print(prices)
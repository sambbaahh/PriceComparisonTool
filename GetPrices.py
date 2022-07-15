from bs4 import BeautifulSoup
import requests
import re

class GetPrices:

    def getJimmsPrice(item,url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        prices = doc.findAll('span',{'itemprop' : 'price'}, text= True)[0].text
        print(prices)


olio = GetPrices
olio.getJimmsPrice("https://www.jimms.fi/fi/Product/Show/174925/981-001074/logitech-g435-lightspeed-langattomat-pelikuulokkeet-mikrofonilla-valkoinen")

from bs4 import BeautifulSoup
import requests


class GetPrices:

    def getJimmsPrice(url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        prices = doc.findAll('span',{'itemprop' : 'price'}, text= True)[0].text
        print(prices)
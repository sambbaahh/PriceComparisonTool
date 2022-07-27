from bs4 import BeautifulSoup, SoupStrainer
import requests


class GetPrices:

    def getJimmsPrice(url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        price = doc.findAll('span',{'itemprop' : 'price'}, text= True)[0].text
        return price

    def getVerkkokauppaComPrice(url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        data = doc.find('data',{'data-price' : 'current'})
        priceInteger = data["data-integer"]
        priceDecimal = data["data-decimals"]
        price = priceInteger + "." + priceDecimal
        return price


#olio = GetPrices
#olio.getVerkkokauppaComPrice("https://www.verkkokauppa.com/fi/product/648169/Weber-Master-Touch-GBS-SE-E-5750-hiiligrilli-57-cm-musta")
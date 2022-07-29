from bs4 import BeautifulSoup, SoupStrainer
import requests


class GetPrices:
    #Metodi hakee Jimmsin sivuilta tavaran hinnan
    def getJimmsPrice(url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        price = doc.findAll('span',{'itemprop' : 'price'}, text= True)[0].text
        return price
        
    #Metodi hakee Verkkokauppa.comin sivuilta tavaran hinnan
    def getVerkkokauppaComPrice(url):
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        data = doc.find('data',{'data-price' : 'current'})
        priceInteger = data["data-integer"]
        priceDecimal = data["data-decimals"]
        price = priceInteger + "." + priceDecimal
        return price

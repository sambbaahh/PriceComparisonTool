from sqlite3 import connect
from tkinter import N
from unicodedata import name
import mysql.connector


class Database:
    #Metodi hakee kaupat tietokannasta
    def findShops():
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')
            sql_select = "SELECT shop.ShopName FROM shop"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()

            # Return array
            return records

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi lisää tavaran tietokantaan
    def addItem(self, itemName, URL, shop):
        try:
            print(URL)
            print(itemName)
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "INSERT INTO item (item.ItemName, item.URL, item.ShopID) VALUES ('" + itemName + "', " \
                + "'" + URL + \
                "', (SELECT shop.ShopID FROM shop WHERE shop.ShopName ='" + shop + "'));"

            cursor = connection.cursor()
            cursor.execute(sql_select)
            connection.commit()

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
    
    #Metodi lisää tavaran hinnan tietokantaan
    def addItemPrice(self, price, date, itemName, shop):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "INSERT INTO price (price.Price, price.Date, price.ItemID) VALUES ('" + price + "', '" + date + "'," \
                + "(SELECT item.ItemID FROM item WHERE item.ItemName = '" + itemName + \
                "' AND item.ShopID = (SELECT shop.shopID FROM shop WHERE shop.ShopName = '" + \
                shop + "')));"

            cursor = connection.cursor()
            cursor.execute(sql_select)
            connection.commit()

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()

    #Metodi hakee tietokannasta kaikkien tavaroiden nimet
    def getItemNames():
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT item.ItemName FROM item"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records
        
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
        
    
    #Metodi hakee tietokannasta kaikki tavarat
    def getAllItems():
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT item.ItemID, item.URL FROM item"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()



    def refreshPrices(self, price, date, itemID):
        index = 0
        for item in itemID:
            try:
                connection = mysql.connector.connect(
                    host='localhost', database='PriceComparisonTool', user='root', password='admin')

                sql_select = "INSERT INTO price (price.Price, price.Date, price.ItemID) VALUES ('" + str(price[index]) + "', '" + date + "', '" + str(itemID[index]) + "');"
                print(sql_select)
                cursor = connection.cursor()
                cursor.execute(sql_select)
                connection.commit()
                index += 1

            finally:
                if connection.is_connected():
                    connection.close()
                    cursor.close()



    def checkShops(item):
            try:
                connection = mysql.connector.connect(
                    host='localhost', database='PriceComparisonTool', user='root', password='admin')
                sql_select = "SELECT shop.ShopName FROM shop INNER JOIN item WHERE shop.ShopID = item.ShopID AND item.ItemName = '" + item +"'"
                cursor = connection.cursor()
                cursor.execute(sql_select)
                records = cursor.fetchall()
                return records


            finally:
                if connection.is_connected():
                    connection.close()
                    cursor.close()



    def checkItemNames(itemName):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "SELECT "\
                "CASE WHEN EXISTS "\
                    "( "\
                        "SELECT item.ItemName FROM item "\
                        "WHERE item.ItemName = '" + itemName + "' "\
                    ") "\
                    "THEN 'TRUE' "\
                    "ELSE 'FALSE' "\
                "END"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            return records


        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
from sqlite3 import connect
from tkinter import N
from unicodedata import name
import mysql.connector


class Database:

    def findShops():
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')
            sql_select = "select shop.ShopName from shop"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()

            print(cursor.rowcount)

            for row in records:
                print(row[0])

            # Return array
            return records

        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")


    def addItem(self, itemName, URL, shop):
        try:
            print(URL)
            print(itemName)
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "INSERT INTO item (item.ItemName, item.URL, item.ShopID) VALUES ('" + itemName + "', " \
            + "'" + URL + "', (SELECT shop.ShopID FROM shop WHERE shop.ShopName ='" + shop + "'));"

            print(sql_select)
            cursor = connection.cursor()
            cursor.execute(sql_select)
            connection.commit()


        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")
    

    def addItemPrice(self, price, date, itemName):
        try:
            connection = mysql.connector.connect(
                host='localhost', database='PriceComparisonTool', user='root', password='admin')

            sql_select = "INSERT INTO price (price.Price, price.Date, price.ItemID) VALUES ('" + price + "', '" + date + "'," \
            + "(SELECT item.ItemID FROM item WHERE item.ItemName = '" + itemName + "' AND item.ShopID = (SELECT item.shopID FROM item WHERE item.ItemName = '"+ itemName +"')));"

            print(sql_select)
            cursor = connection.cursor()
            cursor.execute(sql_select)
            connection.commit()


        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")



olio = Database
x = olio.findShops()
olio.addItem(olio, 'jaa','jaa8', 'Jimms')
olio.addItemPrice(olio, "10053", "2021-12-15", "RTX 3080")
print(x)
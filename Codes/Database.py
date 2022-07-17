from sqlite3 import connect
import mysql.connector

class Database:
        try:
            connection = mysql.connector.connect(host = 'localhost', database ='PriceComparisonTool', user = 'root', password ='admin')

            sql_select = "select * from shop"
            cursor = connection.cursor()
            cursor.execute(sql_select)
            records = cursor.fetchall()
            print(cursor.rowcount)

            for row in records:
                print("ShopID = ", row[0])
                print("ShopName = ", row[1])



        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")


Database()
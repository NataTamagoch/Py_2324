import pymysql

connection = pymysql.connect(host="10.10.103.161", user='pyuser', password='123456', database="test")

cursor = connection.cursor()

cursor.execute("insert into telsprav values("kirill", "morozov", "m", "89110271345")")
connection.commit()
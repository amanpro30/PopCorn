import mysql.connector
import csv
import pymysql
# from collections import OrderedDict
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# passwd="Aman@123",
# database="popcorn"
# ) 

conn = pymysql.connect(host="localhost", user="root",passwd="Aman@123",database="popcorn")
mycursor = conn.cursor()

with open('celebrity.csv', 'r') as new_file:

    csv_reader = csv.DictReader(new_file) 
    # list1 = []
    for line in csv_reader:
        # print(line['id'])
        # print(line)

        data1 = ("INSERT INTO celebrity "
              "(id, name, bday, location, final, p) "
              "VALUES (%(id)s, %(name)s, %(bday)s, %(location)s, %(final)s, %(p)s)")

        mycursor.execute(data1, line)   
        conn.commit()
        break
conn.close()

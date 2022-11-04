import requests

import json

import mysql.connector

import sys

try:

    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='tododb')

except mysql.connector.Error as e:

    sys.exit("connection error")

mycursor=mydb.cursor()

data=requests.get("https://jsonplaceholder.typicode.com/todos").text

data_info=json.loads(data)

for i in data_info:

    if(i['completed']==False):

        id=str(i['userId'])

        complete=str(i['completed'])

        sql="INSERT INTO `todo`(`userid`, `title`, `completed`) VALUES ('"+id+"','"+i['title']+"','"+complete+"')"

        mycursor.execute(sql)

        mydb.commit()
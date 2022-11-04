import requests
import json 
import mysql.connector
try:
   mydb=mysql.connector.connect(host='localhost',user='root',password='',database='userdb')
except mysql.connector.Error as e:
    print("sql connection error",e)
mycursor = mydb.cursor()
data = requests.get("https://jsonplaceholder.typicode.com/todos").text
data_info = json.loads(data)
for i in data_info:
    id = str(i['userId'])
    
    sql = "INSERT INTO `post`(`userid`, `title`, `body`) VALUES ('"+id+"','"+i['title']+"','"+i['body']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print("data inserted successfully",i['userId'])
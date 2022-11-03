import requests
import json 
import mysql.connector

try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='userdb')
except mysql.connector.Error as e:
    print("sql connection error",e)
mycursor = mydb.cursor()
data = requests.get("https://jsonplaceholder.typicode.com/users").text
data_info = json.loads(data)

#print(data_info)
#user_list =[]
for i in data_info:
    #user_list.append([i["name"],["email"],["phone"]])
    sql = "INSERT INTO `users`(`name`, `email`, `phone`) VALUES('"+i['name']+"','"+i['email']+"','"+i['phone']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print("data inserted successfully",i['name'])
    #print(user_list)


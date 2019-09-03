# Python mysql connection process
1. download and install mysql Connector. for installation mysql connector below code have to run

'''
bash
python -m pip install mysql-connector 
'''

2.now create one file and setup connection of mysql using follow command

'''
bash
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

print(mydb) 

'''

<div align="center"><h1>Python Mysql Connection Process</h1></div>

* download and install mysql Connector. for installation mysql connector below code have to run

'''bash
python -m pip install mysql-connector 
'''

* Now create one file and setup connection of mysql using follow command

'''bash
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)
print(mydb) 
'''

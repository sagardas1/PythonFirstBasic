import mysql.connector
"""connect to db"""
mydb= mysql.connector.connect(host="localhost" ,user  ="root",password="Sagardas@12345",database="pythonDb")

"""cursor is like pointers,its points to a particular location"""
myCursor=mydb.cursor()
"""here to write sql quries"""
myCursor.execute('insert into student(name,schoolName) values("rrr","dav public school")')
"""fetching data from db and storing in list that all myCursor.fetchall() do"""
result=myCursor.fetchall()


mydb.commit()

print("bye")

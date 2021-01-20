import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="phpmyadmin",
  password="mypass",
  database="Empresa"
)

mycursor = mydb.cursor()

mycursor.execute("show tables")

myresult = mycursor.fetchall()

for table in myresult:
  miocursor=mydb.cursor()
  miocursor.execute("select * from "+table[0])
  tb_contents=miocursor.fetchall()
  print(table)
  for entry in tb_contents:
    print(entry)
  print("\n")

import sqlite3
from sqlite3 import Error

#função para criar ligação ao 'servidor'
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful\n\n")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

#função para executar a query
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection("/Users/iamthesenate/Documents/menina/db.sqlite3")
select_users = "select name from sqlite_master where type = 'table'"
users = execute_read_query(connection, select_users)

print(str(users)+'\n\n')

select_users = "select * from mdpapp_client"
users = execute_read_query(connection, select_users)

print(str(users[2])+'\n')
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host=' 172.22.167.209',
        user='jhon_root',
        password='Free-Sould-99',
        database='lexy_DB'
    )
    
coon = connect_db()



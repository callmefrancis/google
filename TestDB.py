#C:\Users\frans\AppData\Local\Programs\Python\Python37-32\Scripts>pip install pyodbc

import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=LAPTOP-BNLANS16;"
    "Database=Test;"
    "Trusted_Connection=yes;"
    )
cursor = conn.cursor()
cursor.execute('SELECT * FROM Cube')

for row in cursor:
    print(row)

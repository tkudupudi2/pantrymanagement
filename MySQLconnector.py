import mysql.connector as mysql


db = mysql.connect (
    host = "database-2.cx1eac0mujhy.us-east-2.rds.amazonaws.com",
    user = "admin",
    passwd = "chods123",
    database = "pantry_management"
)


""" 
~ Below code is to insert rows into table 

cursor = db.cursor()

query = "INSERT INTO SHOPPING_LIST (product_type, item_name, item_quantity, unit_type) VALUES (%s,%s,%s,%s)"

values = ("Dairy", "2% Milk", 1, "Gallon")

cursor.execute(query, values)

db.commit()

"""


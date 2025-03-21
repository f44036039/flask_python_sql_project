import mysql.connector # type: ignore
con = mysql.connector.connect(
    user = "root",
    password = "12345678",
    host = "localhost",
    database = "mydb",
)
print("success")
con.close()
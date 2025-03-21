import pymysql # type: ignore
con = pymysql.connect(
    user = "root",
    password = "12345678",
    host = "localhost",
    database = "mydb",
)
print("success")
con.close()
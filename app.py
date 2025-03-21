import mysql.connector # type: ignore
con = mysql.connector.connect(
    user = "root",
    password = "12345678",
    host = "localhost",
    database = "mydb",
)
print("success")
cursor = con.cursor()

from flask import *
app = Flask(
    __name__,
    static_folder = "public",
    static_url_path = "/"
    )
app.secret_key = "any string but secert"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods = ["POST"])
def signup():
    nickname = request.form["nickname"]
    email = request.form["email"]
    password = request.form["password"]

    cursor.execute("select * from member_data where email = %s", (email, ))

    result = cursor.fetchall()
    # print(result)
    if result == []:
        cursor.execute("insert into member_data(nickname, email, password) values(%s, %s, %s)", (nickname, email, password))
        print("list is null")       
    else:
        return redirect("/error?msg=已被註冊")

    con.commit()
    return redirect("/")

@app.route("/member")
def member():
    return render_template("member.html")

@app.route("/error")
def error():
    message = request.args.get("msg", "發生錯誤")
    return render_template("error.html", message = message)

app.run()
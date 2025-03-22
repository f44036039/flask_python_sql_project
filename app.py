import pymysql # mysql-connector-python has import issues
con = pymysql.connect(       # mysql.connector.connect
    user = "root",
    password = "12345678",
    host = "localhost",
    database = "mydb",
)
# print("success")


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

@app.route("/member")
def member():
    # print(session)
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    message = request.args.get("msg", "發生錯誤")
    return render_template("error.html", message = message)

@app.route("/signup", methods = ["POST"])
def signup():
    nickname = request.form["nickname"]
    email = request.form["email"]
    password = request.form["password"]

    cursor = con.cursor()
    cursor.execute("select * from member_data where email = %s", (email, ))

    result = cursor.fetchall()
    # print(result)
    if len(result) == 0:
        cursor.execute("insert into member_data(nickname, email, password) values(%s, %s, %s)", (nickname, email, password))
        print("list is null")       
    else:
        return redirect("/error?msg=已被註冊")

    con.commit()
    return redirect("/")

@app.route("/signin", methods = ["POST"])
def signin():
    email = request.form["email"]
    password = request.form["password"]

    cursor = con.cursor()
    cursor.execute("select * from member_data where email = %s and password = %s", (email, password))

    result = cursor.fetchall()
    # print (result)
    if len(result) == 0:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    else:
        session["nickname"] = result[0][0]
        print(session)
        return redirect("/member")
    
@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect("/")

app.run()
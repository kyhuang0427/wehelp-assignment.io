import pymongo
client = pymongo.MongoClient("mongodb+srv://a5171030:a5171030@cluster0.cpwfktt.mongodb.net/?retryWrites=true&w=majority")
db = client.member_system
collection=db.user

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

except Exception as e:
    print(e)

from flask import *
import json

app=Flask(
    __name__,
    static_folder="static", # 靜態檔案的資料夾名稱
    static_url_path="/" # 靜態檔案對應的網址路徑
) 

app.secret_key = "secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/signout")
def signout():
    del session["nickname"]
    return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("msg", "發生錯誤，請聯繫客服")
    return render_template("error.html", message=message)

@app.route("/signin", methods=["POST"])
def signin():
    email=request.form["email"]
    password=request.form["password"]
    if email=="" or password=="":
        return redirect("/error?message=請輸入帳號密碼")

    collection=db.user
    result=collection.find_one({
        "$and":[
            {"email":email},
            {"password":password}
        ]
    })
    if result==None:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    
    session["nickname"]=result["nickname"]
    
    return redirect("/member")

@app.route('/square/<int:num>')
def square(num):
    result = num ** 2
    return render_template("squareNumber.html", number=num, result=result)

app.run(port=3000)


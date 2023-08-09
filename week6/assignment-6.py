from flask import *
import json
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                        port='3306',
                                        user='root',
                                        password='123456789',
                                        database='website')
cursor = connection.cursor()

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
    if "email" in session:
        name = session['name']
        if request.method == "POST":
            content = request.form["msg"]
     
        select_query = "SELECT message.id, message.member_id, message.content, member.name AS member_name FROM message JOIN member ON message.member_id = member.id;"
        cursor.execute(select_query)
        messages = cursor.fetchall()

        return render_template("member.html", name=name, messages=messages)

    else:
        return redirect("/")

@app.route("/signout")
def signout():
    del session['user_id'] 
    del session['email'] 
    del session['name'] 
    return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("message", "發生錯誤，請聯繫客服")
    return render_template("error.html", message=message)

@app.route("/signup", methods=["POST"])
def signup():
    if  request.method == 'POST':
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        cursor.execute('SELECT * FROM member WHERE username = %s', (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            return redirect("/error?message=帳號已經被註冊")
        else:

            query = "INSERT INTO member (name, username, password) VALUES (%s , %s, %s )"  
            values = (name, email, password)
            
            cursor.execute(query, values)
            connection.commit()
        return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    if  request.method == 'POST':
        email=request.form["email"]
        password=request.form["password"]
        cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        if user:
        # 登入成功，將訊息儲存在session中
            session['user_id'] = user[0]
            session['email'] = user[2]
            session['name'] = user[1]

            return redirect('/member')
        else:
             return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route('/createMessage', methods=['POST'])
def create_message():
    
    user_id = session.get('user_id')
    content = request.form.get('msg')
    cursor.execute("INSERT INTO message (member_id, content) VALUES (%s, %s)", (user_id, content))
    connection.commit()
    return redirect("/member") 

@app.route("/deleteMessage", methods=["POST"])
def delete_message():
    message_id = request.form["message_id"]
    
    # 根據留言ID和會員名稱刪除該留言
    delete_query = "DELETE FROM message WHERE id = %s AND member_id = %s"
    cursor.execute(delete_query, (message_id, session['user_id']))
    
    connection.commit()
    return redirect("/member")
       
app.run(port=3000)


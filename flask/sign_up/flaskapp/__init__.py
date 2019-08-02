from flask import Flask, render_template,request
import pymysql
app=Flask(__name__)
app.debug=True

@app.route ("/tutee_signup")
def tutee_signup():
    return render_template("signup.html")

@app.route("/signup_succeess",methods=["POST","GET"])
def tuteesignup():
    error = None

    if request.methods=="POST":

        id=request.form["id"]
        pw=request.form["pw"]
        email=request.form["email"]
        mac=request.form["mac"]

        conn = pymysql.connect(host='127.0.0.1',
                port=3306,
                user='admin',
                passwd='0507',
                db='attendance',
                charset='utf8')

        cursor = conn.cursor()
        query = "SELECT 1 FROM tutee_info WHERE email=%s AND pw=%s;"%(email,pw)
        #value =(email,pw)

        cursor.execute(query)
        data=(cursor.fetchall())
        
        if data :
            error = "The email is already used. please use another one"
        else:
            query = "INSERT INTO user_table (id, email, pw, mac) values (%s, %s, %s,%s)"
            value = (id, email, pw, mac)
            cursor.execute(query, value)
            data = cursor.fetchall()

            if not data:
                conn.commit()
                return "Tutee_Sign Success"
            else:
                conn.rollback()
                return "Tutee_sign Failed"
                   
        
        cursor.close()
        conn.close()

    #return render_template('.html', error=error)
    #에러페이지


    else :
        id=request.args.get("id")
        pw=request.args.get("pw")
        email=request.args.get("email")
        mac=request.args.get("mac")
        return """sign_up succeed\n
            id = %s\n
            pw = %s\nemail = %s
            mac = %s """%(id,pw,email,mac)
from flask import Flask, render_template,request
import pymysql
app=Flask(__name__)
app.debug=True

@app.route ("/sign_up")
def sign_up():
    return render_template("signup.html")

@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.methods=="POST":
        id=request.form["id"]
        pw=request.form["pw"]
        email=request.form["email"]
        return "sign_up succeed\nid = %s\npw = %s\nemail = %s"%(id,pw,email)
    else :
        id=request.args.get("id")
        pw=request.args.get("pw")
        email=request.args.get("email")
        return "sign_up succeed\nid = %s\npw = %s\nemail = %s"%(id,pw,email)
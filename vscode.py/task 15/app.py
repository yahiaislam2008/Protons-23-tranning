from flask import Flask, render_template, request, redirect
from Model.database import database
import datetime
app = Flask(__name__)
enteries=[]
@app.route("/")
def index():
    return render_template("main.html")

app.route("/new",methods=["GET","POST"])
def indextr():
    if request.method=="POST":
        title= request.form["title"]
        contant=request.form["content"]
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        entry=database(title,contant,date)
        enteries.append(entry)
        return redirect("/")
    return render_template("newentry.html")
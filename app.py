from flask import Flask, render_template,request
import datetime
from pymongo import MongoClient

app=Flask(__name__)
client=MongoClient("mongodb+srv://eunbiyoon:Emily135@microblog-application.vihgli5.mongodb.net/test")
app.db=client.microblog
entries=[]

@app.route("/", methods=["GET","POST"])
def home():
    print([e for e in app.db.entries.find({})])
    if request.method=="POST":
        entry_content=request.form.get("content")
        formatted_date=datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((entry_content, formatted_date))

    entries_with_date=[
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d")
        )
        for entry in entries
    ]
    return render_template("home.html", entries=entries_with_date)


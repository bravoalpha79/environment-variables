import os
from flask import Flask, render_template, request, flash
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        content = int(request.form.get("content"))
        mongo.db.Numbers.insert_one({"number": content})
        flash(f"Number '{content}' has been successfully inserted!")
    return render_template("home.html", numbers=mongo.db.Numbers.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)

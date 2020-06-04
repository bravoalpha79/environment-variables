import os
from flask import Flask, render_template, request, flash


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        content = request.form.get("content")
        flash(f"Thank you, your message '{content}' has been received!")
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=os.environ.get("PORT"), 
            debug=True)
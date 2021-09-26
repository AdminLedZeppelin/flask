from flask import Flask
from flask import redirect, url_for


app = Flask(__name__)



@app.route("/")
def home():
    return "Hello! Main page."

@app.route("/<name>")
def user(name):
    return f"Helloe {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()

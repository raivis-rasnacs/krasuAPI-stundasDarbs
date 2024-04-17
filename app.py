from flask import (
    Flask,
    render_template,
    redirect,
    request
)
import sqlite3

# connecting database
try:
    con = sqlite3.connect("db/keys.db")
    cur = con.cursor()
except:
    print("Neizdevās pieslēgties!")

app = Flask(__name__)

app.config["SECRET_KEY"] = "59fbabd4-fc76-4e01-8393-733abc547822"

@app.route("/")
def index():
    return "<p>Hello World</p>"

if __name__ == "__main__":
    app.run(debug=True)
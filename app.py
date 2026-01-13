from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("attendance.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        roll = request.form["roll"]

        db = get_db()
        cur = db.cursor()
        cur.execute("INSERT INTO attendance (name, roll) VALUES (?, ?)", (name, roll))
        db.commit()
        db.close()

        return "Attendance marked successfully"

    return render_template("index.html")

@app.route("/admin")
def admin():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM attendance")
    records = cur.fetchall()
    db.close()
    return render_template("admin.html", records=records)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

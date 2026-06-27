from flask import Flask, render_template, request
import mysql.connector as sql

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Signup Route
@app.route("/aftersignup", methods=["POST"])
def signup():

    conn = None
    cur = None

    try:
        conn = sql.connect(
            host="localhost",
            user="root",
            password="Vrashbh@123",   # apna MySQL password
            database="grrass"
        )

        cur = conn.cursor()

        email = request.form["email"]
        password = request.form["password"]

        query = "INSERT INTO students (email, password) VALUES (%s, %s)"

        cur.execute(query, (email, password))
        conn.commit()

        return "Signup Successful"

    except Exception as e:
        return render_template("error.html", e=str(e))

    finally:
        if cur:
            cur.close()

        if conn and conn.is_connected():
            conn.close()


# Login Route
@app.route("/afterlogin", methods=["POST"])
def afterlogin():

    conn = None
    cur = None

    try:
        conn = sql.connect(
            host="localhost",
            user="root",
            password="Vrashbh@123",   # apna MySQL password
            database="grrass"
        )

        cur = conn.cursor()

        email = request.form["email"]
        password = request.form["password"]

        query = "SELECT * FROM students WHERE email=%s AND password=%s"

        cur.execute(query, (email, password))

        user = cur.fetchone()

        if user:
            return "Login Successful"
        else:
            return "Invalid Email or Password"

    except Exception as e:
        return render_template("error.html", e=str(e))

    finally:
        if cur:
            cur.close()

        if conn and conn.is_connected():
            conn.close()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
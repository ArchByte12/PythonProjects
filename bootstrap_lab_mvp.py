from textwrap import dedent
import os

# Dictionary of files to create
files = {
    "app.py": dedent('''
        from flask import Flask, render_template, request, redirect, url_for
        import sqlite3, datetime

        app = Flask(__name__)

        def get_db():
            conn = sqlite3.connect("lab_log.db")
            conn.row_factory = sqlite3.Row
            return conn

        @app.route("/")
        def index():
            conn = get_db()
            logs = conn.execute("SELECT * FROM logs ORDER BY time DESC LIMIT 20").fetchall()
            conn.close()
            return render_template("index.html", logs=logs)

        @app.route("/login", methods=["POST"])
        def login():
            user_id = request.form["user_id"]
            lab = request.form["lab"]

            conn = get_db()
            conn.execute(
                "INSERT INTO logs (user_id, lab, action, time) VALUES (?, ?, ?, ?)",
                (user_id, lab, "login", datetime.datetime.now()),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

        @app.route("/logout", methods=["POST"])
        def logout():
            user_id = request.form["user_id"]
            lab = request.form["lab"]

            conn = get_db()
            conn.execute(
                "INSERT INTO logs (user_id, lab, action, time) VALUES (?, ?, ?, ?)",
                (user_id, lab, "logout", datetime.datetime.now()),
            )
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

        if __name__ == "__main__":
            app.run(debug=True)
    '''),

    "init_db.py": dedent('''
        import sqlite3

        conn = sqlite3.connect("lab_log.db")
        c = conn.cursor()

        c.execute("DROP TABLE IF EXISTS logs")
        c.execute("""
        CREATE TABLE logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            lab TEXT,
            action TEXT,
            time TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()
        print("Database initialized.")
    '''),

    "templates/index.html": dedent('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Lab Log MVP</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
        </head>
        <body>
            <h1>Lab Logbook MVP</h1>
            <form method="POST" action="/login">
                <input type="text" name="user_id" placeholder="Enter User ID" required>
                <select name="lab" required>
                    <option value="Lab 1">Lab 1</option>
                    <option value="Lab 2">Lab 2</option>
                    <option value="Lab 3">Lab 3</option>
                </select>
                <button type="submit">Login</button>
            </form>

            <form method="POST" action="/logout">
                <input type="text" name="user_id" placeholder="Enter User ID" required>
                <select name="lab" required>
                    <option value="Lab 1">Lab 1</option>
                    <option value="Lab 2">Lab 2</option>
                    <option value="Lab 3">Lab 3</option>
                </select>
                <button type="submit">Logout</button>
            </form>

            <h2>Recent Activity</h2>
            <table>
                <tr><th>User</th><th>Lab</th><th>Action</th><th>Time</th></tr>
                {% for log in logs %}
                <tr>
                    <td>{{ log.user_id }}</td>
                    <td>{{ log.lab }}</td>
                    <td>{{ log.action }}</td>
                    <td>{{ log.time }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
        </html>
    '''),

    "static/style.css": dedent('''
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        h1, h2 {
            color: #2c3e50;
        }
        form {
            margin-bottom: 20px;
        }
        input, select, button {
            margin: 5px;
            padding: 8px;
        }
        table {
            border-collapse: collapse;
            width: 80%;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 8px;
            text-align: center;
        }
        th {
            background: #f4f4f4;
        }
    '''),
}

# Write files to disk
for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

print("✅ Project files created! Now run: python init_db.py then python app.py")


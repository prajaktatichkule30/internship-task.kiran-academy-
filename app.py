from flask import Flask, render_template
from config import Config
from database.db_connection import get_db_connection

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def dashboard():
    conn = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) AS total FROM candidates")
        total_candidates = cursor.fetchone()["total"]

        cursor.execute("SELECT COUNT(*) AS total FROM companies")
        total_companies = cursor.fetchone()["total"]

        cursor.execute("SELECT COUNT(*) AS total FROM jobs")
        total_jobs = cursor.fetchone()["total"]

        cursor.execute("SELECT COUNT(*) AS total FROM applications")
        total_applications = cursor.fetchone()["total"]

        cursor.close()

        return render_template(
            "dashboard.html",
            total_candidates=total_candidates,
            total_companies=total_companies,
            total_jobs=total_jobs,
            total_applications=total_applications
        )

    except Exception as e:
        return f"Database Error: {str(e)}"

    finally:
        if conn:
            conn.close()


@app.route("/health")
def health():
    return "Recruitment & Placement Management System is Running!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
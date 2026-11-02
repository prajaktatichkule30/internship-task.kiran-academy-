from pathlib import Path
from database.db_connection import get_db_connection

sql_file = Path(__file__).parent / "database" / "database_schema.sql"

conn = get_db_connection()

try:
    cursor = conn.cursor()

    sql = sql_file.read_text(encoding="utf-8")

    # Skip CREATE DATABASE and USE statements
    statements = [
        s.strip()
        for s in sql.split(";")
        if s.strip()
        and not s.strip().upper().startswith("CREATE DATABASE")
        and not s.strip().upper().startswith("USE ")
    ]

    for statement in statements:
        cursor.execute(statement)

    conn.commit()
    print("All database tables created successfully!")

except Exception as e:
    conn.rollback()
    print("Database Error:", e)

finally:
    conn.close()
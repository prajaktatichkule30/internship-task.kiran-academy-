from database.db_connection import get_connection

def run_report(sql):
    con = get_connection()
    try:
        with con.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
    finally:
        con.close()

def applications_by_status():
    return run_report("SELECT application_status,COUNT(*) AS total FROM applications GROUP BY application_status")

def open_jobs_by_company():
    return run_report("SELECT c.company_name,COUNT(j.job_id) AS open_jobs FROM companies c LEFT JOIN jobs j ON j.company_id=c.company_id AND j.status='OPEN' GROUP BY c.company_id,c.company_name")

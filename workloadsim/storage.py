
from workloadsim.database import (
    get_connection,
    initialize_database
)


def create_job(job_id, cpu, memory):
    initialize_database()

    with get_connection() as connection:
        connection.execute("""
            INSERT INTO jobs (job_id, cpu, memory)
            VALUES (?, ?, ?)
        """, (job_id, cpu, memory))


def find_job(job_id):
    initialize_database()

    with get_connection() as connection:
        return connection.execute("""
            SELECT * FROM jobs WHERE job_id = ?
        """, (job_id,)).fetchone()


def get_all_jobs():
    initialize_database()

    with get_connection() as connection:
        rows = connection.execute("""
            SELECT * FROM jobs ORDER BY created_at
        """).fetchall()

        return [dict(row) for row in rows]


def update_job_status(job_id, status):
    initialize_database()

    with get_connection() as connection:
        connection.execute("""
            UPDATE jobs SET status = ?
            WHERE job_id = ?
        """, (status, job_id))

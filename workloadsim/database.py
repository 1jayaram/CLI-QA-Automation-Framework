
import sqlite3
import os
from pathlib import Path


def get_db_path():
    custom_path = os.environ.get("WORKLOADSIM_DB")

    if custom_path:
        return custom_path

    return str(Path(__file__).parent / "workloadsim.db")


def get_connection():
    connection = sqlite3.connect(get_db_path())
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                job_id TEXT PRIMARY KEY,
                cpu INTEGER NOT NULL CHECK(cpu > 0),
                memory INTEGER NOT NULL CHECK(memory > 0),
                status TEXT NOT NULL DEFAULT 'queued',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

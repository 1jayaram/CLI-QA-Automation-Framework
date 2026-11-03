

import subprocess
import sys
from pathlib import Path

import pytest


# Absolute path to the cli-qa-framework folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def isolated_database(tmp_path, monkeypatch):
    db_path = tmp_path / "test_jobs.db"

    monkeypatch.setenv("WORKLOADSIM_DB", str(db_path))

    return db_path


@pytest.fixture
def run_cli(isolated_database):
    def execute(*args, timeout=5):

        command = [
            sys.executable,
            "-m",
            "workloadsim.cli",
            *args
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(PROJECT_ROOT),
        )

        return result

    return execute

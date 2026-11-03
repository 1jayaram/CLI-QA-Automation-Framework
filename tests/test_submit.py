
import json
import pytest

@pytest.mark.smoke
def test_submit_valid_job(run_cli):
    result = run_cli(
        "submit",
        "--job-id", "101",
        "--cpu", "4",
        "--memory", "8"
    )

    assert result.returncode == 0

    data = json.loads(result.stdout)

    assert data["job_id"] == "101"
    assert data["cpu"] == 4
    assert data["memory"] == 8
    assert data["status"] == "queued"


def test_submit_multiple_jobs(run_cli):
    for job_id in ["101", "102", "103"]:
        result = run_cli(
            "submit",
            "--job-id", job_id,
            "--cpu", "2",
            "--memory", "4"
        )

        assert result.returncode == 0

    result = run_cli("list")

    jobs = json.loads(result.stdout)

    assert len(jobs) == 3

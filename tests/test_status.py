
import json


def test_get_existing_job_status(run_cli):
    run_cli(
        "submit",
        "--job-id", "201",
        "--cpu", "2",
        "--memory", "4"
    )

    result = run_cli(
        "status",
        "--job-id", "201"
    )

    assert result.returncode == 0

    data = json.loads(result.stdout)

    assert data["status"] == "queued"


def test_status_of_nonexistent_job(run_cli):
    result = run_cli(
        "status",
        "--job-id", "999"
    )

    assert result.returncode == 1
    assert "Job not found" in result.stderr

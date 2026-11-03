
import json


def test_cancel_existing_job(run_cli):
    run_cli(
        "submit",
        "--job-id", "301",
        "--cpu", "2",
        "--memory", "4"
    )

    result = run_cli(
        "cancel",
        "--job-id", "301"
    )

    assert result.returncode == 0

    data = json.loads(result.stdout)

    assert data["status"] == "cancelled"


def test_cancel_nonexistent_job(run_cli):
    result = run_cli(
        "cancel",
        "--job-id", "999"
    )

    assert result.returncode == 1
    assert "Job not found" in result.stderr

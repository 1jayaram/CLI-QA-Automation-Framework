
import pytest


@pytest.mark.parametrize(
    "cpu, memory, expected_error",
    [
        ("0", "8", "CPU must be greater than zero"),
        ("-1", "8", "CPU must be greater than zero"),
        ("4", "0", "Memory must be greater than zero"),
        ("4", "-8", "Memory must be greater than zero"),
    ]
)
def test_invalid_resource_values(
    run_cli,
    cpu,
    memory,
    expected_error
):
    result = run_cli(
        "submit",
        "--job-id", "401",
        "--cpu", cpu,
        "--memory", memory
    )

    assert result.returncode == 1
    assert expected_error in result.stderr


def test_duplicate_job_id(run_cli):
    run_cli(
        "submit",
        "--job-id", "402",
        "--cpu", "2",
        "--memory", "4"
    )

    result = run_cli(
        "submit",
        "--job-id", "402",
        "--cpu", "4",
        "--memory", "8"
    )

    assert result.returncode == 1
    assert "Job ID already exists" in result.stderr


def test_missing_required_argument(run_cli):
    result = run_cli(
        "submit",
        "--job-id", "403",
        "--cpu", "2"
    )

    assert result.returncode == 2
    assert "required" in result.stderr.lower()


def test_invalid_cpu_data_type(run_cli):
    result = run_cli(
        "submit",
        "--job-id", "404",
        "--cpu", "four",
        "--memory", "8"
    )

    assert result.returncode == 2
    assert "invalid int value" in result.stderr.lower()

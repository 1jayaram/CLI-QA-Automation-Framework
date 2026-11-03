
import time


def test_cli_execution_time(run_cli):
    start = time.perf_counter()

    result = run_cli(
        "submit",
        "--job-id", "601",
        "--cpu", "2",
        "--memory", "4"
    )

    elapsed = time.perf_counter() - start

    assert result.returncode == 0
    assert elapsed < 3.0


def test_repeated_cli_execution(run_cli):
    for i in range(10):
        result = run_cli(
            "submit",
            "--job-id", f"job-{i}",
            "--cpu", "2",
            "--memory", "4"
        )

        assert result.returncode == 0

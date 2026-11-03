
def test_successful_command_exit_code(run_cli):
    result = run_cli(
        "submit",
        "--job-id", "501",
        "--cpu", "2",
        "--memory", "4"
    )

    assert result.returncode == 0


def test_application_error_exit_code(run_cli):
    result = run_cli(
        "status",
        "--job-id", "999"
    )

    assert result.returncode == 1


def test_invalid_command_exit_code(run_cli):
    result = run_cli("unknown-command")

    assert result.returncode == 2

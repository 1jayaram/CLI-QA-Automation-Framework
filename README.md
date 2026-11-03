# CLI QA Automation Framework – WorkloadSim

## Overview

WorkloadSim is a Python-based command-line application developed to demonstrate automated software testing of enterprise-style CLI tools.

The project focuses on building a reusable QA automation framework using **Pytest, Python subprocess, and SQLite** to validate command execution, input handling, application behaviour, database operations, and exit codes.

The framework is designed to simulate real-world software quality assurance scenarios, including functional testing, negative testing, boundary testing, regression testing, and basic performance testing.

## Project Objectives

- Develop a command-line application that simulates an enterprise workload management tool.
- Automate CLI testing using Python and Pytest.
- Validate command-line arguments, outputs, and process exit codes.
- Test application behaviour under valid and invalid inputs.
- Integrate SQLite for persistent job data storage.
- Execute tests in isolated environments to avoid test-data interference.
- Prepare the framework for cross-platform execution on Windows and Linux.

## Architecture

The project consists of two major components:

### 1. Application Under Test – WorkloadSim

A Python-based CLI application that simulates workload management operations.

Supported commands:

| Command | Description |
|---|---|
| `submit` | Submit a new workload job |
| `status` | Retrieve the status of a job |
| `list` | Display available jobs |
| `cancel` | Cancel an existing job |

Example:

```bash
python -m workloadsim.cli submit --job-id 101 --cpu 4 --memory 8
```

### 2. QA Automation Framework

The testing framework uses Pytest and Python's subprocess module to execute CLI commands independently and validate their behaviour.

The test framework checks:

- Command execution and output validation
- Valid and invalid command-line arguments
- Job submission and retrieval
- Job cancellation
- Application exit codes
- Database operations
- Basic execution-time behaviour

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development and test automation |
| Pytest | Automated testing framework |
| SQLite | Persistent database storage |
| Subprocess | Independent CLI execution |
| JSON | Structured command output |
| Git | Version control |
| GitHub Actions | CI/CD and automated test execution |

## Project Structure

```text
cli-qa-framework/
│
├── workloadsim/
│   ├── __init__.py
│   ├── cli.py
│   ├── database.py
│   ├── job_manager.py
│   └── storage.py
│
├── tests/
│   ├── conftest.py
│   ├── test_submit.py
│   ├── test_status.py
│   ├── test_cancel.py
│   ├── test_invalid_inputs.py
│   ├── test_cli_exit_codes.py
│   └── test_performance.py
│
├── test_data/
├── reports/
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- VS Code or another Python IDE

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/cli-qa-framework.git
```

### 2. Navigate to the project directory

```bash
cd cli-qa-framework
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

On Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Run the following commands from the project root.

**Submit a job**

```bash
python -m workloadsim.cli submit --job-id 101 --cpu 4 --memory 8
```

**Check job status**

```bash
python -m workloadsim.cli status --job-id 101
```

**List jobs**

```bash
python -m workloadsim.cli list
```

**Cancel a job**

```bash
python -m workloadsim.cli cancel --job-id 101
```

## Running Automated Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Generate an HTML test report:

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

Generate a JUnit XML report:

```bash
python -m pytest --junitxml=reports/junit.xml
```

## Testing Strategy

| Testing Type | Objective |
|---|---|
| Functional Testing | Validate expected application behaviour |
| Negative Testing | Verify handling of invalid inputs |
| Boundary Testing | Validate minimum and maximum input values |
| Regression Testing | Ensure existing functionality remains stable |
| Exit Code Testing | Verify correct process exit codes |
| Performance Testing | Measure basic command execution time |
| Integration Testing | Validate interaction between CLI, application logic, and SQLite |

## Continuous Integration

The project is designed to support automated test execution through GitHub Actions.

The CI workflow can execute the Pytest suite on Windows and Linux environments to help identify platform-specific issues.

## Skills Demonstrated

- Python programming and scripting
- Software Quality Assurance
- Test automation with Pytest
- CLI testing and subprocess management
- Functional, negative, and regression testing
- SQLite database operations
- Test fixtures and test isolation
- Debugging and failure analysis
- Git and GitHub
- CI/CD fundamentals

## Future Enhancements

- Add concurrent job-submission testing.
- Implement workload simulation with running and completed states.
- Add advanced stress, load, and endurance testing.
- Integrate structured logging and test execution metrics.
- Expand API and backend integration testing.
- Improve CI/CD reporting and automated test coverage.

## Author

**Jayaram S**

GitHub: https://github.com/YOUR_USERNAME

---

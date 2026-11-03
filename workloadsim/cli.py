# Import standard Python libraries for argument parsing, JSON formatting, and system-level operations
import argparse
import json
import sys

# Import the core backend functions that interact with the workload simulator
from workloadsim.job_manager import (
    submit_job,
    get_job_status,
    cancel_job,
    list_jobs
)


def main():
    # Initialize the main argument parser with the application name and description
    parser = argparse.ArgumentParser(
        prog="workloadsim",
        description="WorkloadSim CLI application"
    )

    # Create a subparser group to handle specific action commands (e.g., 'submit', 'status')
    # 'dest="command"' saves the chosen subcommand to args.command, and 'required=True' forces the user to pick one
    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # --- Setup 'submit' subcommand ---
    submit_parser = subparsers.add_parser("submit")
    submit_parser.add_argument("--job-id", required=True)
    submit_parser.add_argument("--cpu", type=int, required=True)      # Expects an integer value for CPU allocation
    submit_parser.add_argument("--memory", type=int, required=True)   # Expects an integer value for Memory allocation

    # --- Setup 'status' subcommand ---
    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("--job-id", required=True)

    # --- Setup 'cancel' subcommand ---
    cancel_parser = subparsers.add_parser("cancel")
    cancel_parser.add_argument("--job-id", required=True)

    # --- Setup 'list' subcommand ---
    # This command doesn't need additional arguments; it just lists everything
    subparsers.add_parser("list")

    # Parse the arguments provided by the user via the terminal command line
    args = parser.parse_args()

    try:
        # Route execution based on the specific subcommand the user typed
        if args.command == "submit":
            result = submit_job(
                args.job_id,
                args.cpu,
                args.memory
            )

        elif args.command == "status":
            result = get_job_status(args.job_id)

        elif args.command == "cancel":
            result = cancel_job(args.job_id)

        elif args.command == "list":
            result = list_jobs()

        # Convert the backend response (dictionary/list) into a pretty-printed JSON string and display it
        print(json.dumps(result, indent=4))
        return 0  # Return exit code 0 indicating successful execution

    except ValueError as error:
        # Catch value-related errors, print the error message to stderr, and exit with failure code 1
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


# Standard boilerplate: ensure main() runs only if this file is executed directly (not imported elsewhere)
if __name__ == "__main__":
    sys.exit(main())

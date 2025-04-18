import pytest
import io
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def run_pytest_in_current_directory():
    """
    Runs all pytest files in the directory specified by the BDDFILESPATH environment variable
    and captures the results summary.

    Returns:
        str: The captured pytest output (including the summary).
        int: The pytest exit code.
    """
    test_directory = os.getenv('BDDFILESPATH')
    if not test_directory:
        print("Error: BDDFILESPATH environment variable not set.")
        return "", 1  # Return an error indication

    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    exit_code = pytest.main([test_directory])  # Pass the directory as a list

    sys.stdout = old_stdout
    output = redirected_output.getvalue()

    return output, exit_code

if __name__ == "__main__":
    output, exit_code = run_pytest_in_current_directory()

    print("Pytest Output:\n")
    print(output)

    print(f"\nPytest Exit Code: {exit_code}")

    if exit_code == 0:
        print("All tests passed.")
    else:
        print("Some tests failed.")
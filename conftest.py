import pytest
from Utilities.email_pytest_report import Email_Pytest_Report


# Test arguments
@pytest.fixture
def email_pytest_report(request):
    "pytest fixture for device flag"
    return request.config.getoption("--email_pytest_report")


def pytest_addoption(parser):  # Command line options:
    parser.addoption("--email_pytest_report",
                     dest="email_pytest_report",
                     help="Email pytest report: Y or N",
                     default="N")


def pytest_terminal_summary(terminalreporter, exitstatus):
    "add additional section in terminal summary reporting."
    if not hasattr(terminalreporter.config, 'workerinput'):
        if terminalreporter.config.getoption("--email_pytest_report").lower() == 'y':
            # Initialize the Email_Pytest_Report object
            email_obj = Email_Pytest_Report()
            # Send html formatted email body message with pytest report as an attachment
            email_obj.send_test_report_email(html_body_flag=True, attachment_flag=True, report_file_path='default')

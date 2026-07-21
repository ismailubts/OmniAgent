from server.auth.sheets_client import GoogleSheetsClient

from omniagent.app_server.utils.logger import omniagent_logger


def test_import():
    assert omniagent_logger is not None
    assert GoogleSheetsClient is not None

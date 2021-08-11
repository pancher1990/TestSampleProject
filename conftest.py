import pytest
from tests.utils.api import Api


@pytest.fixture(scope="function", autouse=False)
def authentication():
    Api.login()




# def pytest_exception_interact(node, call: CallInfo, report):
#     logger = logging.getLogger(__name__)
#     if report.failed:
#         logger.error(call.excinfo)

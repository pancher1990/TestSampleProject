import pytest
from tests.utils.api import Api


@pytest.fixture(scope="function", autouse=False)
def authentication():
    Api.login()

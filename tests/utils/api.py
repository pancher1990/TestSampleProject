import configparser
import logging

from tests.utils.http_requests_manager import HttpManager
from tests.utils.json_fixture import JSONFixture


class Api:
    LOGGER = logging.getLogger(__name__)
    parser = configparser.ConfigParser()
    parser.read('config_sample.ini')

    BASE_URL = parser.get('reqres', 'url')

    @staticmethod
    def login():
        url = Api.BASE_URL + "api/login"
        user_email = Api.parser.get('reqres', 'email')
        password = Api.parser.get('reqres', 'password')
        result = HttpManager.auth(url, user_email, password)
        Api.LOGGER.info('TEST: Try to login with {0}, {1} '.format(user_email, password))
        assert 200 == result.status_code

    @staticmethod
    def create_user(name, job):
        url = Api.BASE_URL + "api/users"
        body_request = JSONFixture.for_create_user(name, job)
        result = HttpManager.post(url, body_request)
        Api.LOGGER.info('TEST: Try to create user : request {0} with data {1} '.format("POST", body_request))
        return result

    @staticmethod
    def get_user(id):
        url = Api.BASE_URL + "api/users/{0}".format(id)
        result = HttpManager.get(url)
        Api.LOGGER.info('TEST: Try to get user: request {0}  with id {1} '.format("GET", id))
        return result

    @staticmethod
    def update_user(id, name, job):
        url = Api.BASE_URL + "api/users/{0}".format(id)
        body_request = JSONFixture.for_update_user(name, job)
        result = HttpManager.put(url, body_request)
        Api.LOGGER.info('TEST: Try to update user: request {0}  with id {1} '.format("PUT", body_request))
        return result

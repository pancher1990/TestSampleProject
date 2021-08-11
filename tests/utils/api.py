import configparser
import logging
from tests.utils.http_requests_manager import HttpManager
from tests.utils.json_fixture import JSONFixture


class Api:
    parser = configparser.ConfigParser()
    parser.read('config_sample.ini')

    BASE_URL = parser.get('reqres', 'url')

    @staticmethod
    def login():
        url = Api.BASE_URL + "api/login"
        user_email = Api.parser.get('reqres', 'email')
        password = Api.parser.get('reqres', 'password')
        result = HttpManager.auth(url, user_email, password)
        assert 200 == result.status_code

    @staticmethod
    def create_user(name, job):
        url = Api.BASE_URL + "api/users"
        result = HttpManager.post(url, JSONFixture.for_create_user(name, job))
        return result

    @staticmethod
    def get_user(id):
        url = Api.BASE_URL + "api/users/{0}".format(id)
        result = HttpManager.get(url)
        return result

    @staticmethod
    def update_user(id, name, job):
        url = Api.BASE_URL + "api/users/{0}".format(id)
        result = HttpManager.put(url, JSONFixture.for_update_user(name, job))
        return result

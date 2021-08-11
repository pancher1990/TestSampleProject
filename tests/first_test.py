import pytest
from tests.utils.api import Api


class TestIssue:
    create_user_test_data = [("morpheus", "leader", 201)]
    update_user_test_data = [(2, "morpheus", "zion resident", 200)]
    get_user_test_data = [(2, "janet.weaver@reqres.in", "Janet", "Weaver", 200)]

    @pytest.mark.parametrize("name,job,expected_status_code", create_user_test_data)
    @pytest.mark.api
    def test_create(self, authentication, name, job, expected_status_code):
        response_create_user = Api.create_user(name, job)
        assert expected_status_code == response_create_user.status_code
        response_json = response_create_user.json()

        user_name = response_json["name"]
        user_job = response_json["job"]
        assert (user_job == job) and (user_name == name)

    @pytest.mark.parametrize("user_id, email, first_name, last_name,expected_status_code", get_user_test_data)
    @pytest.mark.api
    def test_get(self, authentication, user_id, email, first_name, last_name, expected_status_code):
        response_get_user = Api.get_user(user_id)
        assert expected_status_code == response_get_user.status_code

        response_json = response_get_user.json()
        user_first_name = response_json["data"]["first_name"]
        user_last_name = response_json["data"]["last_name"]
        user_email = response_json["data"]["email"]

        assert (user_first_name == first_name) \
               and (user_last_name == last_name) \
               and (user_email == email)

    @pytest.mark.parametrize("user_id, name, job, expected_status_code", update_user_test_data)
    @pytest.mark.api
    def test_update(self, authentication, user_id, name, job, expected_status_code):
        response_update_user = Api.update_user(user_id, "morpheus", "zion resident")
        assert 200 == response_update_user.status_code

        response_json=response_update_user.json()
        user_name = response_json["name"]
        user_job = response_json["job"]

        assert (user_name == name) and (user_job == job)

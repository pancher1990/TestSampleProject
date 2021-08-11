class JSONFixture:

    @staticmethod
    def for_create_user(name, job):
        json = {
            "name": name,
            "job": job
        }
        return json

    @staticmethod
    def for_update_user(name, job):
        # возможно не всю информацию можно менять поэтому вынес отдельно от for_create_user
        json = {
            "name": name,
            "job": job
        }
        return json

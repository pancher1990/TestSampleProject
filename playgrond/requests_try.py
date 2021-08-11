import requests

body ={
                "email": "eve.holt@reqres.in",
                "password": "pistol"
            }
result = requests.post("https://reqres.in/api/register", json=body)
pass
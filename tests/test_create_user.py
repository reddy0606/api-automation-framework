# import requests
#
# BASE_URL = "https://reqres.in/api"   # sample API
#
# def test_create_user():
#     payload = {
#         "name": "Sai",
#         "job": "Automation Engineer"
#     }
#     response = requests.post(f"{BASE_URL}/users", json=payload)
#
#     # Assertions
#     assert response.status_code == 201
#     data = response.json()
#     assert data["name"] == "Sai"
#     assert data["job"] == "Automation Engineer"



from utils.api_client import APIClient
from data.payloads import create_user_payload


def test_create_user(headers):

    response = APIClient.post(
        "/users",
        json=create_user_payload,
        headers=headers
    )

    print(response.status_code)
    print(response.text)

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["name"] == "morpheus"
    assert response_data["job"] == "leader"
# from utils.api_client import APIClient
# from data.payloads import update_user_payload
#
# def test_update_user(headers):
#
#     response = APIClient.put(
#         "/users/2",
#         update_user_payload,
#         headers=headers
#     )
#     print(response.status_code)
#     print(response.text)
#
#     assert response.status_code == 200
#
#     response_data = response.json()
#
#     assert response_data["name"] == "neo"
#     print(response_data)



from utils.api_client import APIClient
from data.payloads import update_user_payload


def test_update_user(headers):

    response = APIClient.put(
        "/users/2",
        json=update_user_payload,
        headers=headers
    )

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["name"] == "neo"
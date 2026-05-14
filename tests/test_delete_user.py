# from utils.api_client import APIClient
#
# def test_delete_user(headers):
#
#     response = APIClient.delete(
#         "/users/2",
#         headers
#     )
#
#     assert response.status_code != 204


from utils.api_client import APIClient


def test_delete_user(headers):

    response = APIClient.delete(
        "/users/2",
        headers=headers
    )

    print(response.status_code)

    assert response.status_code == 204
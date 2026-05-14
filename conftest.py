# import pytest
# import requests
#
# @pytest.fixture
# def api_client():
#     base_url = "https://reqres.in/api"
#     def _client(method, endpoint, **kwargs):
#         return requests.request(method, f"{base_url}{endpoint}", **kwargs)
#     return _client



import pytest
from config.config import HEADERS


@pytest.fixture
def headers():
    return HEADERS
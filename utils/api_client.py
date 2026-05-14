import requests
from config.config import BASE_URL


class APIClient:

    @staticmethod
    def get(endpoint, headers=None):
        return requests.get(
            f"{BASE_URL}{endpoint}",
            headers=headers
        )

    @staticmethod
    def post(endpoint, json=None, headers=None):
        return requests.post(
            f"{BASE_URL}{endpoint}",
            json=json,
            headers=headers
        )

    @staticmethod
    def put(endpoint, json=None, headers=None):
        return requests.put(
            f"{BASE_URL}{endpoint}",
            json=json,
            headers=headers
        )

    @staticmethod
    def delete(endpoint, headers=None):
        return requests.delete(
            f"{BASE_URL}{endpoint}",
            headers=headers
        )
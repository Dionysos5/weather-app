import requests

class APIRequest:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def make_request(self, endpoint, params):
        url = f"{self.base_url}/{endpoint}"
        params["appid"] = self.api_key
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
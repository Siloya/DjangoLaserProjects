import json
import os

import requests
from marshmallow import Schema, fields


class RequestProvider:
    def __init__(self, host: str, path: str, token: str, request_nb: int) -> None:
        self.requestNb = request_nb
        self._host = host
        self.path = path
        self._token = token

    def request(self):
        print("\tRequesting...")
        return requests.get(f"https://{self._host}{self.path}{self._token}")

    def handle_error(self, response_code: int):
        """
        Placeholder method for handling errors
        """
        pass

    def run(self):
        response = self.request()
        if response.status_code != 200:
            self.handle_error(response.status_code)
        else:
            self.handle_response(response.content)

    def handle_response(self, response):
        print(self._host)
        print("\tHandling...")
        print(f"{type(response) = }")
        print(f"{len(response) = }")
        print(response[0: len(response) // 4])


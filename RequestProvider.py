import requests


class RequestProvider:
    def __init__(self, host: str, token: str, time: int) -> None:
        self.time = time
        self._host = host
        self._token = token

    def request(self):
        print("\tRequesting...")
        return requests.get(f"{self._host}{self._token}")

    def handle_response(self, response):
        print("\tHandling...")
        print(f"{type(response) = }")
        print(f"{len(response) = }")
        print(response[0: len(response) // 4])

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

import json
import time

import requests
from jsonpath_ng import parse


class RequestProvider:
    def __init__(self, host: str, path: str, token: str, request_nb: int, mapping: list) -> None:
        self.requestNb = request_nb
        self._host = host
        self.path = path
        self._token = token
        self.mapping = mapping
        self.retries = 3
        self.sleep_time = 2  # in seconds

    def request(self):
        print("\tRequesting...")
        return requests.get(f"http://{self._host}{self.path}{self._token}")

    def handle_error(self, response_code: int, response):
        """
        Handle errors
        """
        if 500 <= response_code < 600:
            for i in range(self.retries):
                # Retry the request
                print(f"Retrying request, attempt {i + 1} of {self.retries}...")
                response = self.request()
                if response.status_code != 200:
                    time.sleep(self.sleep_time)
                else:
                    self.handle_response(response.content)
                    return
            print("Error: Request failed after all retries.")
        else:
            # Handle other types of errors (e.g. client-side errors)
            print(f"Error: Request failed with response code {response_code}.")
            print(response)

    def run(self):
        response = self.request()
        if response.status_code != 200:
            self.handle_error(response.status_code, response.content)
        else:
            self.handle_response(response.content)

    def handle_response(self, response):
        print(self._host)
        print("\tHandling...")
        print(f"{type(response) = }")
        print(f"{len(response) = }")
        print(response[0: len(response) // 4])
        news = []
        response = json.loads(response.decode())
        title_expr = parse(self.mapping['title'])
        sub_title_expr = parse(self.mapping['subTitle'])
        content_expr = parse(self.mapping['content'])
        url_to_image_expr = parse(self.mapping['imageUrl'])
        provider_expr = parse(self.mapping['provider'])
        published_at_expr = parse(self.mapping['publishedAt'])
        src_expr = parse(self.mapping['source'])
        category_expr = parse(self.mapping['category'])
        for new in response[self.mapping['dataPath']]:
            title = title_expr.find(new)[0].value
            sub_title = sub_title_expr.find(new)[0].value
            content = content_expr.find(new)[0].value
            url_to_image = url_to_image_expr.find(new)[0].value
            provider = provider_expr.find(new)[0].value
            published_at = published_at_expr.find(new)[0].value
            src = src_expr.find(new)[0].value
            category = category_expr.find(new)[0].value
            news.append(
                # News(new['title'], new['sub_title'], new['content'], new['urlToImage'], new['source']['provider'], new['publishedAt'], new['src'],
                # None)
                News(title, sub_title, content, url_to_image, provider, published_at, src, category)
            )

        # for book in news:
        #     print(f'category: {book.title} author: {book.sub_title} title: {book.content} price: {book.url_image}')


class News:
    def __init__(self, title, sub_title, content, url_image, provider, date_published, src, category):
        self.title = title
        self.sub_title = sub_title
        self.content = content
        self.url_image = url_image
        self.provider = provider
        self.date_published = date_published
        self.src = src
        self.category = category

import json
import os
from threading import Thread

from dotenv import load_dotenv

from RequestProvider import RequestProvider
from RequestProvidersScheduler import RequestProvidersScheduler

load_dotenv()
news_api = []
with open("providers.json", "r") as file:
    data = json.load(file)
for element in data:
    if element['active']:
        news_api.append(
            RequestProvider(os.getenv(element["host"]), element["path"], os.getenv(element["token"]), int(element["requestNb"]), element["mapping"]))
if __name__ == "__main__":
    scheduler = RequestProvidersScheduler(news_api, True)
    scheduler_thread = Thread(target=scheduler.run)
    scheduler_thread.start()
    # time.sleep(10) # wait for 10 seconds for example
    # scheduler.stop()
    # schedule.clear()

import time

from RequestProvider import RequestProvider
from RequestProvidersScheduler import RequestProvidersScheduler
from threading import Thread
import os
from dotenv import load_dotenv
import json

load_dotenv()
news_api = []
with open("providers.json", "r") as file:
    data = json.load(file)
for element in data:
    news_api.append(RequestProvider(os.getenv(element["host"]), element["path"], os.getenv(element["token"]), int(element["requestNb"])))
if __name__ == "__main__":
    scheduler = RequestProvidersScheduler(news_api, True)
    scheduler_thread = Thread(target=scheduler.run)
    scheduler_thread.start()
    # time.sleep(10) # wait for 10 seconds for example
    # scheduler.stop()
    # schedule.clear()

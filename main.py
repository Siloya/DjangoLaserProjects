import time

from RequestProvider import RequestProvider
from RequestProvidersScheduler import RequestProvidersScheduler
from threading import Thread
import os
from dotenv import load_dotenv

load_dotenv()

news_api = [
    RequestProvider(os.getenv("HOST"), os.getenv("TOKEN"), int(os.getenv("ALLOWED_REQUEST_PER_DAY"))),
]

if __name__ == "__main__":
    scheduler = RequestProvidersScheduler(news_api, True)
    scheduler_thread = Thread(target=scheduler.run)
    scheduler_thread.start()
    # time.sleep(10) # wait for 10 seconds for example
    # scheduler.stop()
    # schedule.clear()

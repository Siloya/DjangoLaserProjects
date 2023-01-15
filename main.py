import time

from RequestProvider import RequestProvider
from RequestProvidersScheduler import RequestProvidersScheduler
from threading import Thread

ALLOWED_REQUEST_PER_DAY = 3600  # (minutes)

news_api = RequestProvider("https://newsapi.org/v2/top-headlines?country=us&apiKey=", "0a3682d43c4b47eab54374b1b5f2fc19", ALLOWED_REQUEST_PER_DAY)

if __name__ == "__main__":
    scheduler = RequestProvidersScheduler([news_api], True)
    scheduler_thread = Thread(target=scheduler.run)
    scheduler_thread.start()
    # time.sleep(10) # wait for 10 seconds for example
    # scheduler.stop()
    # schedule.clear()

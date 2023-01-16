from typing import List, Optional

import schedule

from RequestProvider import RequestProvider


class RequestProvidersScheduler:
    def __init__(self, providers: List[RequestProvider], debug: Optional[bool] = False):
        self._providers = providers
        self._debug = debug
        self._running = True

    def stop(self):
        print("Exiting Scheduler...", end="")
        schedule.clear()
        self._running = False

    def run(self):
        for p in self._providers:
            print(f"Scheduling {type(p).__name__}...", end="")
            if self._debug:
                schedule.every(p.requestNb).seconds.do(p.run)
            else:
                interval = 1440 / p.requestNb
                schedule.every(interval).minutes.do(p.run)
            print("Done")
        while self._running:
            schedule.run_pending()
        print("Done")

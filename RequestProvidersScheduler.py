from typing import List, Optional

import schedule

from RequestProvider import RequestProvider


class RequestProvidersScheduler:
    def __init__(self, providers: List[RequestProvider], debug: Optional[bool] = False):
        self._providers = providers
        self._debug = debug

    def stop(self):
        schedule.clear()

    def run(self):
        for p in self._providers:
            print(f"Scheduling {p.__class__.__name__}...", end="")
            if self._debug:
                schedule.every(p.time).seconds.do(p.run)
            else:
                schedule.every(p.time).minutes.do(p.run)
            print("Done")
        while True:
            schedule.run_pending()

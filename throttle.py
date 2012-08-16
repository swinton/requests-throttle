#!/usr/bin/env python

import datetime
import sys
import time

def throttle_hook(response):
    ratelimited = "x-ratelimit-remaining" in response.headers and \
                  "x-ratelimit-reset" in response.headers 

    if ratelimited:
        remaining = int(response.headers["x-ratelimit-remaining"])
        reset = datetime.datetime.utcfromtimestamp(float(response.headers["x-ratelimit-reset"]))
        now = datetime.datetime.utcnow()
        
        time_to_reset = reset - now
        time_to_sleep = time_to_reset.seconds / remaining

        sys.stderr.write("Throttling... Sleeping for %d secs...\n" % time_to_sleep)
        time.sleep(time_to_sleep)

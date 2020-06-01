#! /usr/bin/env python3
"""Cronometro"""
import time
import sys
import datetime

then=time.time()



while True:
    try:    
        now=time.time()
        lap=now-then
        sys.stdout.write('\r'+str(round(lap,3)))
    except KeyboardInterrupt:
        print()
        print(datetime.datetime.fromtimestamp(now))



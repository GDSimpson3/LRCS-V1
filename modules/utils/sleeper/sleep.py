from config import ENVIRONMENT

import time

def SleepFor(timeTs):
    if ENVIRONMENT == 'DEV':
        time.sleep(timeTs)
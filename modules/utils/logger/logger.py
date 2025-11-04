from config import ENVIRONMENT

def LOG(item):
    if ENVIRONMENT == 'DEV':
        print(f'DEBUG----- {item}')
import os
import sys
from dotenv import load_dotenv, find_dotenv

class Utils:
    def __init__(self):
        pass
    
    def get_dlai_api_key(self):
        _ = load_dotenv(find_dotenv())
        return os.getenv("DLAI_API_KEY")
    

# testing

def __init__():
    utils = Utils()
    DLAI_API_KEY = utils.get_dlai_api_key()
    print(f"DLAI_API_KEY: {DLAI_API_KEY}")

if __name__ == '__main__':
    __init__()
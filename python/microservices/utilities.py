import os
import sys
from dotenv import load_dotenv, find_dotenv

class Utils:
    def __init__(self):
        pass
    
    def get_dlai_api_key(self):
        _ = load_dotenv(find_dotenv())
        return os.getenv('DLAI_API_KEY')
    
    def get_file_extension(self, file_name):
        _, file_extension = os.path.splitext(file_name)
        return file_extension.replace('.', '')
    

# testing

def __init__():
    utils = Utils()

    DLAI_API_KEY = utils.get_dlai_api_key()
    print(f"DLAI_API_KEY: {DLAI_API_KEY}")

    file_name = 'example.pdf'
    file_ext = utils.get_file_extension(file_name)
    print(f"File {file_name} has extension: {file_ext}")


if __name__ == '__main__':
    __init__()
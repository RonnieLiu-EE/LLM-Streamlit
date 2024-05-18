import json

from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError
from unstructured.partition.html import partition_html
from unstructured.partition.pptx import partition_pptx
from unstructured.staging.base import dict_to_elements, elements_to_json

from utilities import Utils

# get unstructured api key
utils = Utils()
DLAI_API_KEY = utils.get_dlai_api_key()


# testing

def __init__():
    print(f"DLAI_API_KEY: {DLAI_API_KEY}")

if __name__ == '__main__':
    __init__()
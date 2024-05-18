import json
import logging

from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError
from unstructured.partition.pdf import partition_pdf
from unstructured.partition.html import partition_html
from unstructured.partition.pptx import partition_pptx
from unstructured.staging.base import dict_to_elements, elements_to_json

from .utilities import Utils

# set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# get unstructured api key
utils = Utils()
DLAI_API_KEY = utils.get_dlai_api_key()


class Preprocessor:
    def __init__(self):
        pass

    def run(self, file_path):
        # subclasses to implement
        raise NotImplementedError("Subclasses must implement this method")


class PDFPreprocessor(Preprocessor):
    def run(self, file_path):
        logger.info("Running PDF Preprocessor...")

        # partition file
        elements = partition_pdf(file_path, strategy='fast')
        for element in elements[:10]:
            print(f"{element.category.upper()}: {element.text}")


class PreprocessorFactory:
    @staticmethod
    def create_preprocessor(format):
        if format.lower() == 'pdf':
            return PDFPreprocessor()
        else:
            raise ValueError(f"Unknown format: {format}")



# testing

def __init__():
    # api key
    logger.info(f"DLAI_API_KEY: {DLAI_API_KEY}")

    # object factory
    preprocessor = PreprocessorFactory.create_preprocessor(format='pdf')
    logger.info(f"Preprocessor Type: {type(preprocessor)}")


if __name__ == '__main__':
    __init__()
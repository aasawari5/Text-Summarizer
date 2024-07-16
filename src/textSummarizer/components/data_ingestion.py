# update the components
import os
import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
import logging

import urllib.request 


class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_file(self):
        source_url = self.config.source_URL
        local_file_path = self.config.local_data_file
        urllib.request.urlretrieve(source_url, local_file_path)
        logging.info(f"Downloaded file from {source_url} to {local_file_path}")

        # Log the file size and type
        if os.path.exists(local_file_path):
            logging.info(f"File size: {os.path.getsize(local_file_path)} bytes")
            with open(local_file_path, 'rb') as file:
                header = file.read(4)
                logging.info(f"File header: {header}")

    def extract_zip_file(self):
        local_file_path = self.config.local_data_file
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        try:
            with zipfile.ZipFile(local_file_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logging.info(f"Extracted {local_file_path} to {unzip_path}")
        except zipfile.BadZipFile:
            logging.error(f"File {local_file_path} is not a zip file")

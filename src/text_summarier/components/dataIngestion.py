import os 
import urllib.request as request
import zipfile 
from src.text_summarier.logging import logger
from src.text_summarier.entity import DataIngestionConfig
from src.text_summarier.config.configuration import ConfigruationManager
#from src.text_summarier.config.configuration import (ConfigruationManager, DataIngestionConfig)

class DataIngestionComponent:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"File is downloading")
        else:
            logger.info(f"File already exits")

    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
    

if __name__=="__main__":
    config=ConfigruationManager()
    data_ingestion_config=config.get_data_ingestion_config()
    data_ingestion=DataIngestionComponent(config=data_ingestion_config)

    data_ingestion.download_file()
    data_ingestion.extract_zip_file()
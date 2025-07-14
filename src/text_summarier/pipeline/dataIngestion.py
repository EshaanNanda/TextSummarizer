from src.text_summarier.config.configuration import ConfigruationManager
from src.text_summarier.components.dataIngestion import DataIngestionComponent


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config=ConfigruationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestionComponent(config=data_ingestion_config)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
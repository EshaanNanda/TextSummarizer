from src.text_summarier.logging import logger
from src.text_summarier.pipeline.dataIngestion import DataIngestionTrainingPipeline
from src.text_summarier.pipeline.dataTransformation import DataTransformationTrainingPipeline


STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_validation_pipeline=DataTransformationTrainingPipeline()
    data_validation_pipeline.initiate_data_transformation()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

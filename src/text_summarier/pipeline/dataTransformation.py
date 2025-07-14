from src.text_summarier.components.dataTransformation import DataTransformationComponent
from src.text_summarier.config.configuration import ConfigruationManager



class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        config=ConfigruationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformationComponent(config=data_transformation_config)

        data_transformation.convert()

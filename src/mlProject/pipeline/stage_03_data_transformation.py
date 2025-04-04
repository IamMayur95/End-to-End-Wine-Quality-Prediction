from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts\data_validation\status.txt"),'r') as file:
                data_validation_status = file.read().split(":")[-1].strip()
                logger.info(f"Data_Validation_Status = {data_validation_status}")

            if data_validation_status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("Your data schema is not valid.")
                

        except Exception as e:
            print(e)


        
        
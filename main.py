from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationPipline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"
try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
      data_validation = DataValidationPipline()
      data_validation.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      logger.exception(e)
      raise e

STAGE_NAME = "Data Transformation stage"
try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
      data_transformation = DataTransformationPipeline()
      data_transformation.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      logger.exception(e)
      raise e

STAGE_NAME = "Model Training stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Evaluation stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = ModelEvaluationPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
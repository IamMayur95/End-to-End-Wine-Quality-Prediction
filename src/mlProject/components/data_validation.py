import os
from mlProject import logger
import pandas as pd
from mlProject.config.configuration import DataValidationConfig

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            data.drop(columns=["Id"],inplace=True)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            if not os.path.exists(self.config.STATUS_FILE):
                os.makedirs(os.path.dirname(self.config.STATUS_FILE), exist_ok=True)  # Create directory if missing

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e
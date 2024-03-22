from src.constants import *
from src.config.configuration import *
import pandas as pd
import os,sys
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    row_data_path:str = RAW_FILE_PATH
    train_data_path:str = TRAIN_FILE_PATH
    test_data_path:str = TEST_FILE_PATH

class DataIngestion:
    def __init__(self):
        
        self.data_ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        
        try:
            df = pd.read_csv(DATASET_PATH)
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.row_data_path),exist_ok=True)          
            df.to_csv(self.data_ingestion_config.row_data_path,index=False)
            
            train_data_set,test_data_set = train_test_split(df,test_size=0.2,random_state=42)
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            train_data_set.to_csv(self.data_ingestion_config.train_data_path,header=True)
            
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)
            test_data_set.to_csv(self.data_ingestion_config.test_data_path,header=True)
            
            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data = obj.initiate_data_ingestion()
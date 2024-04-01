from src.constants import *
from src.config.configuration import *
import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
from src.utils import load_model

class PredictionPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            processor_path = PROCESSOR_OBJ_FILE_PATH
            model_path = MODEL_FILE_PATH
            
            processor = load_model(processor_path)
            model = load_model(model_path)
            
            data_scaled = processor.transform(features)
            pred = model.predict(data_scaled)
            
            return pred
        
        except Exception as e:
            logging.info('Error occured in prediction pipeline')
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(self,
                 carat:float,
                 cut:str,
                 color:str,
                 clarity:str,
                 depth:float, 
                 table:float,
                 x:float, 
                 y:float,
                 z:float):
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                
                'carat':[self.carat],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity],
                'depth':[self.depth], 
                'table':[self.table],
                'x':[self.x], 
                'y':[self.y],
                'z':[self.z]
            }
            
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe gathered')
            
            return df
                        
        except Exception as e:
            logging.info('Error occured in custom pipeline dataframe')
            raise CustomException(e,sys)
        
             

        
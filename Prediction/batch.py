from src.constants import *
from src.config.configuration import *
import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
import pickle
from src.utils import load_model
from sklearn.pipeline import Pipeline

PREDICTION_FOLDER = 'batch_prediction'
PREDICTION_CSV = 'prediction_csv'
PREDICTION_FILE = 'output.csv'
FEATURE_ENG_FOLDER = 'feature_engg'


ROOT_DIR = os.getcwd()
BATCH_PREDICTION = os.path.join(ROOT_DIR,PREDICTION_FOLDER,PREDICTION_CSV)
FEATURE_ENGG = os.path.join(ROOT_DIR,PREDICTION_FOLDER,FEATURE_ENG_FOLDER)

class batch_prediction:
    def __init__(self,
                 input_file_path,
                 model_file_path,
                 transformation_file_path,                
                 ):
        self.input_file_path = input_file_path
        self.model_file_path = model_file_path
        self.transformation_file_path = transformation_file_path
        
        
    def start_batch_prediction(self):
        try:
                            
            ## load data transformation pipeline path
            with open(self.transformation_file_path,'rb') as f:
                processor = pickle.load(f)
                
            ## load the model separately
            model = load_model(filepath=self.model_file_path)
                             
            df = pd.read_csv(self.input_file_path)
            
            df = df.drop('id',axis=1)
            
            transformed_data = processor.transform(df)
            
            FEATURE_ENGG_PATH = FEATURE_ENGG
            
            os.makedirs(FEATURE_ENGG_PATH,exist_ok=True)
            
            file_path = os.path.join(FEATURE_ENGG_PATH,'processor.csv')
            
            predictions = model.predict(transformed_data)
            
            df_prediction = pd.DataFrame(predictions,columns=['prediction'])
            
            BATCH_PREDICTION_PATH = BATCH_PREDICTION
            os.makedirs(BATCH_PREDICTION_PATH,exist_ok=True)
            csv_path = os.path.join(BATCH_PREDICTION_PATH,'output.csv')
            
            df_prediction.to_csv(csv_path,index=False)
            logging.info('Batch Prediction done')
            
            
            
                                  
        except Exception as e:
            raise CustomException(e,sys)
        
     

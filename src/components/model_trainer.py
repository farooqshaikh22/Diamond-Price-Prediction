from src.logger import logging
from src.exception import CustomException
from src.constants import *
from src.config.configuration import *
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet,SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score,mean_absolute_error
from src.utils import save_object,evaluate_model

class ModelTrainerConfig:
    model_file_path:str = MODEL_FILE_PATH
    
class Modeltrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info('Splitting dependant and independant variables from train and test data')
            X_train,y_train,X_test,y_test = (train_arr[:,:-1],
                                             train_arr[:,-1],
                                             test_arr[:,:-1],
                                             test_arr[:,-1])
            
            models = {
                    'LinearRegression':LinearRegression(),
                    'Lasso':Lasso(),
                    'Ridge':Ridge(),
                    'Elasticnet':ElasticNet(),
                    'SGD':SGDRegressor(),
                    'Decision Tree' :DecisionTreeRegressor(),
                    'KNN':KNeighborsRegressor(),
                    'XBG':XGBRegressor(),
                    'RandomForest':RandomForestRegressor(),
                    'Adaboost':AdaBoostRegressor(),
                    'Gradientboost':GradientBoostingRegressor()
            }
            
            model_report:dict = evaluate_model(X_train,y_train,X_test,y_test,models)

            print(model_report)
            print('\n==========================================================================\n')
            logging.info(f'Model Report : {model_report}')
            
            ##Get best model score from dictionary
            
            best_model_score = max(model_report.values())
            
            ## Best model name 
            best_model_name = list(model_report.keys())[
                list(model_report.value()).index(best_model_score)
                ]
            best_model = models[best_model_name]
            
            print(f'Best Model Found , Model Name : {best_model_name},R2 Score : {best_model_score}')
            print('\n========================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name},R2 Score : {best_model_score}')
            
            save_object(file_path=self.model_trainer_config.model_file_path,
                        obj=best_model)
            

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)
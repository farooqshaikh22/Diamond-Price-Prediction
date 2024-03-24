from src.logger import logging
from src.exception import CustomException
from src.constants import *
from src.config.configuration import *
import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    processor_obj_file_path:str = PROCESSOR_OBJ_FILE_PATH
    transform_train_data_path:str = TRANSFORMED_TRAIN_DATA_FILE_PATH
    transform_test_data_path:str = TRANSFORMED_TEST_DATA_FILE_PATH
    
def remove_features(df):
    return df.drop(columns=['x','y','z'],axis=1)
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformation(self):
        
        try:
            logging.info('data transformation started')
            
            ## defining numerical and categorical columns
            categorical_cols = ['cut', 'color', 'clarity']
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            logging.info('Pipeline Initiated')
            ## Numerical pipeline
            num_pipeline = Pipeline(steps=[
                ('remove_features',FunctionTransformer(remove_features,validate=False)),
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
            ])

            ## categorical pipeline
            cat_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinal',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
            ])

            preprocessor = ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            
            return preprocessor

                        
        except Exception as e:
            logging.info('Exception occured in the get_data_transformation')
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info('read train and test data')
            logging.info(f"Train Dataframe Head : /n {train_df.head().to_string()}")
            logging.info(f"Test Dataframe Head : /n {test_df.head().to_string()}")
            
            preprocessor_obj = self.get_data_transformation()
            
            target_col_name = 'price'
            drop_columns = ['id',target_col_name]
            
            X_train = train_df.drop(columns=drop_columns,axis=1)
            y_train = train_df[target_col_name]
            
            X_test = test_df.drop(columns=drop_columns,axis=1)
            y_test = test_df[target_col_name]
            
            logging.info('Applying preprocessor object on train and test data')
            X_train_transformed = preprocessor_obj.fit_transform(X_train)
            X_test_transformed = preprocessor_obj.transform(X_test)
            
            train_array = np.c_[X_train_transformed,np.array(y_train)]
            test_array = np.c_[X_test_transformed,np.array(y_test)]
            
            df_train = pd.DataFrame(train_array)
            df_test = pd.DataFrame(test_array)
            
            os.makedirs(os.path.dirname(self.data_transformation_config.transform_train_data_path),
                        exist_ok=True)
            df_train.to_csv(self.data_transformation_config.transform_train_data_path,
                            index=False,header=True)
            
            os.makedirs(os.path.dirname(self.data_transformation_config.transform_test_data_path),
                        exist_ok=True)
            df_test.to_csv(self.data_transformation_config.transform_test_data_path,
                           index=False,header=True)
            
            save_object(file_path=self.data_transformation_config.processor_obj_file_path,
                        obj=preprocessor_obj)
            
            logging.info('preprocessor pickle file saved')
            
            return(train_array,
                   test_array)
            
        except Exception as e:
            logging.info('Exception occured in the initiate_data_transformation')
            raise CustomException(e,sys)
        
        
        
        
        
        
        

    
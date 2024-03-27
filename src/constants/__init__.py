import os,sys
from datetime import datetime

def current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = current_time_stamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = 'data'
DATA = 'gemstone.csv'


ARTIFACT_DIR_KEY = 'Artifact'

## data ingestion related variables
DATA_INGESTION_KEY = 'data_ingestion'
RAW_DATA_DIR_KEY = 'raw_data_dir'
INGESTED_DATA_DIR_KEY = 'ingested_data_dir'
RAW_DATA = 'row.csv'
TRAIN_DATA = 'train.csv'
TEST_DATA = 'test.csv'

## data transformation related variables
DATA_TRANSFORMATION_ARTIFACT_KEY = 'data_transformation'
DATA_PROCESSOR_DIR = 'processor'
PROCESSOR_OBJ = 'processor.pkl'
FEATURE_ENGINEERING_OBJ = 'feature_engg.pkl'
DATA_TRANSFORMATION_DIR = 'transformation'
TRANSFORMED_TRAIN_DATA = 'train.csv'
TRANSFORMED_TEST_DATA = 'test.csv'

## model trainer
MODEL_TRAINER_KEY = 'model_trainer'
MODEL_OBJ = 'model.plk'
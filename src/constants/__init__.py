import os,sys
from datetime import datetime

def current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = current_time_stamp()

ROOT_DIR = os.getcwd()
DATA_DIR = 'data'
ARTIFACT_DIR_KEY = 'Artifact'

## data ingestion related variables
DATA_INGESTION_KEY = 'data_ingestion'
ROW_DATA_DIR_KEY = 'raw_data_dir'
INGESTED_DATA_DIR_KEY = 'ingested_data_dir'
ROW_DATA = 'gemstone.csv'
TRAIN_DATA = 'train.csv'
TEST_DATA = 'test.csv'
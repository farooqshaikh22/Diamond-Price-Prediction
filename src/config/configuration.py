from src.constants import *
import os,sys

ROOT_DIR = ROOT_DIR_KEY

DATASET_PATH = os.path.join(ROOT_DIR,DATA_DIR,DATA)

## data ingestion 
RAW_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_KEY,CURRENT_TIME_STAMP,
                             RAW_DATA_DIR_KEY,RAW_DATA)

TRAIN_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_KEY,CURRENT_TIME_STAMP,
                               INGESTED_DATA_DIR_KEY,TRAIN_DATA)

TEST_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_KEY,CURRENT_TIME_STAMP,
                              INGESTED_DATA_DIR_KEY,TEST_DATA)

## data transformation

PROCESSOR_OBJ_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,
                                                        DATA_TRANSFORMATION_ARTIFACT_KEY,
                                                        DATA_PROCESSOR_DIR,
                                                        PROCESSOR_OBJ)

FEATURE_ENGINEERING_OBJ_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,
                                                 DATA_TRANSFORMATION_ARTIFACT_KEY,
                                                 DATA_PROCESSOR_DIR,FEATURE_ENGINEERING_OBJ)

TRANSFORMED_TRAIN_DATA_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,
                                                DATA_TRANSFORMATION_ARTIFACT_KEY,
                                                DATA_TRANSFORMATION_DIR,
                                                TRANSFORMED_TRAIN_DATA)

TRANSFORMED_TEST_DATA_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,
                                               DATA_TRANSFORMATION_ARTIFACT_KEY,
                                               DATA_TRANSFORMATION_DIR,
                                               TRANSFORMED_TEST_DATA)

## model trainer

MODEL_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,MODEL_TRAINER_KEY,MODEL_OBJ)
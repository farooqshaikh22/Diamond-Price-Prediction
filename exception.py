from flask import Flask
from src.logger import logging
from src.exception import CustomException
import sys,os



if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        ml =  CustomException(e,sys)
        logging.info(ml)
    
    
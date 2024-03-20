import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format = '[%(asctime)s]: %(message)s')

list_of_files = [
    'src/__init__.py',
    'src/components/__init__.py',
    'src/config/__init__.py',
    'src/constants/__init__.py',
    'src/entity/__init__.py',
    'src/exception/__init__.py',
    'src/logger/__init__.py',
    'src/pipeline/__init__.py',
    'src/utils/__init__.py',
    'src/config/config.yaml',
    'schema.yaml',
    'app.py',
    'main.py',
    'logs.py',
    'exception.py',
    'setup.py'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory; {filedir} for the file {filename}')
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filename)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating empty file: {filename}')
            
    else:
        logging.info(f'{filename} is already created')
        
    
        
    
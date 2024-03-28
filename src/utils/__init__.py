from src.logger import logging
from src.exception import CustomException
import pickle
import os,sys
from sklearn.metrics import r2_score

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        
        for i in range(len(models)):
            model = list(models.values())[i]
            
            ## Train Model
            model.fit(X_train,y_train)
            
            ## Predict testing data
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            ## Get R2 score for both train and test data
            train_r2_score = r2_score(y_train,y_train_pred)
            test_r2_score = r2_score(y_test,y_test_pred)
            
            report[list(report.keys())[i]] = test_r2_score
            
            return report
        
    except Exception as e:
        logging.info('Excwption occured during model training')
        raise CustomException(e,sys)
    
        
        
    
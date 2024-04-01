from flask import Flask, request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictionPipeline
import os
from werkzeug.utils import secure_filename
from Prediction.batch import batch_prediction
from src.logger import logging
from src.components.data_transformation import DataTransformationConfig
from src.config.configuration import *
from src.pipeline.training_pipeline import Train

transformer_file_path = PROCESSOR_OBJ_FILE_PATH
model_file_path = MODEL_FILE_PATH

UPLOAD_FOLDER = 'batch_prediction/uploaded_csv_file'

app = Flask(__name__,template_folder='templates')

ALLOWED_EXTENSIONS = {'csv'}

@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/predict",methods = ["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template('form.html')
    
    else:
        data = CustomData(
            carat = float(request.form.get('carat')),
            cut = str(request.form.get('cut')),
            color = str(request.form.get('color')),
            clarity = str(request.form.get('clarity')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z'))
        )
        
        final_new_data = data.get_data_as_dataframe()
        
        prediction_pipeline = PredictionPipeline()
              
        pred = prediction_pipeline.predict(features=final_new_data)
        
        result = int(pred[0])
        
        return render_template('form.html',final_result = result)



if __name__ == '__main__':
    app.run(debug=True)
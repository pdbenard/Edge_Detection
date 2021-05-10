from flask import Flask, request, render_template, flash, redirect, send_from_directory, url_for
from flask_restful import Resource, Api, reqparse
import numpy as np
import requests
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

from edge_opencv import edge_detection


app = Flask(__name__, static_folder='images', template_folder='template')

app.config["DEBUG"] = True

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, 'images/')

full_path = target + 'result.png'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>OPENCV EDGE DETECTION</h1><p>This app performs edge detection using OpenCV Canny algorithm on an image.</p>"

@app.route('/uploads', methods=['GET', 'POST'])
def upload_process_image():
    if request.method == 'GET':
        return render_template('index.html',name = "index")
    
    if request.method == 'POST':
        #Checking for upload errors
        if 'file' not in request.files:
            flash('No file part')
            return render_template('error.html', message='FILE_LOAD_ERROR: No file part, please try again')
            
        
        file = request.files['file']
        
        if file.filename=='':
            flash('No selected file')
            return render_template('error.html', message='FILE_LOAD_ERROR: No file selected, please select a file')
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
        image = file.read()
        npimg = np.fromstring(image, np.uint8)
        
        
        result_paths = edge_detection(npimg)
        
        
        return render_template('result.html',
            image_name1=result_paths[0],
            image_name2=result_paths[1],
            image_name3=result_paths[2]
            )
    
if __name__ == '__main__':
    app.run()
# from flask import Flask,render_template, request
# from keras.preprocessing.image import load_img
# from keras.preprocessing.image import img_to_array
# from keras.application.vgg16 import preprocess_input
# from keras.application.vgg16 import decode_predictions
# from keras.applicatioin.vgg16 import VGG16


# app=Flask(__name__)

# @app.route("/",methods=['GET'])
# def hello_world():
#     return render_template('index.html')
# @app.route('/',methods=['POST'])
# def predicr():
#     imagefile=request.files['imgfiles']
#     image_path='./images/'+imagefile.filename
#     imagefile.save(image_path)
#     return render_template('index.html')

# if __name__=='__main__':
#     app.run(port=5000,debug=True)
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'F:/Cv/dogs_vs_cats_classifiation/static/images'
MODEL_PATH = "F:/Cv/dogs_vs_cats_classifiation/model/dogs_cats_clss_97.h5"
IMG_SIZE = (150, 150)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model
model = tf.keras.models.load_model(MODEL_PATH)

# Prediction function
def predict(filepath):
    img = image.load_img(filepath, target_size=IMG_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)[0][0]
    return "Dog" if prediction > 0.5 else "Cat"

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            label = predict(path)
            return render_template('index.html', filename=filename, label=label)
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)

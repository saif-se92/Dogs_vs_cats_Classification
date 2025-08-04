# Dogs vs. Cats Image Classification with CNN

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-%23000.svg?logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00.svg?logo=tensorflow)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?logo=numpy&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-9.0+-blue.svg?logo=python&logoColor=white)

## Project Overview

This project implements a Convolutional Neural Network (CNN) using TensorFlow and Keras to classify images of dogs and cats. The application allows users to upload an image and get a prediction on whether it contains a dog or a cat.

## Key Features

- Flask-based web application for easy interaction
- Uses TensorFlow/Keras deep learning framework
- Pre-trained CNN model with 97.14% validation accuracy
- Simple and intuitive user interface
- Handles image uploads and displays prediction results

## Model Architecture

The CNN model includes:
- Conv2D + BatchNorm + MaxPooling blocks
- GlobalAveragePooling layer
- Dense layers with Dropout regularization
- Trained with binary crossentropy loss and Adam optimizer

## Results

The model achieves:
- Training accuracy: 98.97%
- Validation accuracy: 97.14%
- Validation loss: 0.0976

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dogs-vs-cats-classification.git
   cd dogs-vs-cats-classification
   ```
2.Install required packages:
  ```bash
  pip install -r requirements.txt
  ```
3.Download the pre-trained model and place it in the model/ directory.
## Usage
1.Run the Flask application:
  ```bash
  python app.py
  ```
2.Open your browser and navigate to http://localhost:5000.

3.Upload an image of a dog or cat and view the prediction.
## Requirements

- Python 3.6+

- TensorFlow 2.x

- Flask

- NumPy

- Pillow

## File Structure
  ```bash
  dogs-vs-cats-classification/
├── app.py                # Flask application
├── model/                # Contains pre-trained model
├── static/               # Static files (CSS, JS)
│   └── images/           # Uploaded images storage
├── templates/            # HTML templates
│   └── index.html        # Main page template
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

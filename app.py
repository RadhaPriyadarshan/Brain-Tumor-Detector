from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model('model.h5')  # Load your trained model

def preprocess_image(image):
    img = image.resize((150, 150))  # Resize image as per your model's input shape
    img_array = np.array(img)
    img_array = img_array.reshape(1,150,150,3) # Add batch dimension
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            labels = ['Glioma_Tumor','Meningioma_Tumor','No_Tumor','Pituitary Tumor']
            image_bytes = file.read()
            image = Image.open(io.BytesIO(image_bytes))
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)
            indices = prediction.argmax()
            print(labels[indices])
            # Customize the response based on your model's output
            # For example, if it's a classification model, you might get class probabilities
            # Display the result accordingly in the HTML
            result = f"Prediction: {labels[indices]}"  # Modify this line based on your model's output
            
            return render_template('index.html', prediction_result=result)

if __name__ == '__main__':
    app.run(debug=True)

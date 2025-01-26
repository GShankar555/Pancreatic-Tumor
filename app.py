from flask import Flask, render_template, request, flash, redirect
import tensorflow as tf
from tensorflow.keras.preprocessing import image # type: ignore
import numpy as np
from werkzeug.utils import secure_filename
import os

model = tf.keras.models.load_model('model.h5')

img_height = 112
img_width = 112

class_names = ['Normal', 'Pancreatic Tumor']

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(img_height, img_width))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    prediction = model.predict(img_array)
    return class_names[int(prediction[0][0] > 0.5)]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            prediction = predict_image(file_path)
            flash(f'Prediction: {prediction}')
            try:
                os.remove(file_path)
            except:
                pass
            return render_template('index.html', prediction=prediction)
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['jpg', 'png', 'jpeg']

# if __name__ == '__main__':
#     app.run(debug=True)
# Pancreatic Tumor Detection Using CNN

## Project Overview
This project implements a deep learning model using a Convolutional Neural Network (CNN) for detecting pancreatic tumors from CT scan images. The primary goal is to assist in the early detection of pancreatic tumors by analyzing medical imaging data. The project includes data preprocessing, feature extraction, and classification stages, providing an accessible interface for medical professionals to input images and receive diagnostic predictions.

## Project Structure
```
├── app.py                # Flask application for serving predictions
├── static
├── templates
│   └── index.html        # Web interface for uploading CT scan images
├── README.md             # Project documentation
```

## Features
- **Image Upload and Detection**: Upload CT scan images and detect the presence of pancreatic tumors.
- **REST API**: Provides an endpoint for integrating automated tumor detection into other systems.
- **Web Interface**: A user-friendly interface for uploading and receiving results.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GShankar555/Pancreatic-Tumor.git
   cd Pancreatic-tumor
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

## Usage

1. **Run the Flask server:**
   ```bash
   python app.py
   ```

2. **Access the web interface:**
   Open a browser and navigate to `http://127.0.0.1:5000`.

3. **Upload a CT scan image:**
   Use the interface to upload a CT scan image and get the prediction for tumor detection.

## API Endpoint

- **POST** `/`
  - **Description**: Accepts a CT scan image and returns the tumor detection result.
  - **Request**: `multipart/form-data` with a file parameter named `file`.
  - **Response**: JSON object indicating the prediction.

  **Example using cURL:**
  ```bash
  curl -X POST -F "file=@path/to/image.jpg" http://127.0.0.1:5000/
  ```

## Model Description
The CNN model is designed to:
- Preprocess and normalize CT scan images.
- Extract critical imaging features relevant to pancreatic tumor detection.
- Classify images into tumor-positive or tumor-negative categories.

### Training Dataset
- Pancreatic CT scan images labeled with tumor presence or absence.
- Data augmentation techniques applied to enhance model performance.

## Dependencies
- Flask
- TensorFlow
- Keras
- OpenCV
- NumPy

---

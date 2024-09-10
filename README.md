
# Brain Tumor Detector

This repository contains a deep learning-based application designed to detect brain tumors from MRI images. The model is trained using a convolutional neural network (CNN) and integrated into a simple web interface for easy use. The following sections explain the structure and functionality of the repository.

## Table of Contents
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Model](#model)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RadhaPriyadarshan/Brain-Tumor-Detector.git
    cd Brain-Tumor-Detector
    ```

2. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

The app will be hosted on `http://localhost:5000`.

## Project Structure

```bash
├── static/               # Contains static files like CSS and images
├── templates/            # HTML templates for the web interface
├── app.py                # Main Flask app to run the web server
├── brain-tumor.ipynb     # Jupyter notebook for training and evaluating the CNN model
├── model.h5              # Pre-trained model file
└── README.md             # Project documentation
```

### Files Description

- **`app.py`**: The Flask web application to serve the model and provide a simple user interface.
- **`brain-tumor.ipynb`**: A Jupyter notebook used to build and train the CNN model.
- **`model.h5`**: The pre-trained model file that is loaded by the Flask app for inference.
- **`static/` and `templates/`**: These directories contain the CSS, images, and HTML files needed for the front-end of the web application.

## Usage

1. **Web Interface**: After running the `app.py` script, you can navigate to `http://localhost:5000` to upload an MRI image. The model will predict whether the MRI shows a brain tumor or not.
   
2. **Model Training and Evaluation**: The `brain-tumor.ipynb` notebook contains the code for training the model using MRI images. You can open this file using Jupyter Notebook or JupyterLab to experiment with the model architecture, training, and evaluation.

## Model

The brain tumor detection model is a Convolutional Neural Network (CNN) trained on MRI images. The model file (`model.h5`) is used to perform predictions in the web interface. If you want to retrain or fine-tune the model, use the `brain-tumor.ipynb` notebook, which contains all the steps from preprocessing the data to training the model.

## Contributing

Contributions are welcome! If you'd like to improve the code or add new features, feel free to fork the repository and submit a pull request. Please make sure your code follows the same style and is well-documented.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

# Image Shape Detection API

This project provides a RESTful API to detect shapes in images using a pre-trained TensorFlow model. It uses Flask for the API and OpenCV for image processing.

## File Description

- `app.py`: The main Flask application that provides an endpoint for shape detection.
- `function.py`: Contains the `Function` class with methods for image processing and shape prediction.
- `model.h5`: Model for shape detection. Download the model from [this link](https://drive.google.com/file/d/1d0lvE77jSMmldKyt_g3CfYTJ73aOimoh/view?usp=sharing).

## Installation
1. **Clone the repository**:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```
3. **Download the pre-trained model**.

## Usage
1. **Start the Flask server**:

    ```bash
    python app.py
    ```

2. **Send a POST request** to the `/detection` endpoint with an image file. The image should be in PNG, JPG, or JPEG format.

    **Example using `curl`**:

    ```bash
    curl -X POST http://127.0.0.1:5000/detection -F "image=@path/to/your/image.jpg"
    ```

    **Example using `requests` in Python**:

    ```python
    import requests

    url = "http://127.0.0.1:5000/detection"
    files = {'image': open('path/to/your/image.jpg', 'rb')}
    response = requests.post(url, files=files)
    print(response.json())
    ```

3. **Response**:
    On success, the response will include:

    ```json
    {
        "message": "success process",
        "label": "ShapeLabel",
        "image_original_base64": "Base64EncodedImageString"
    }
    ```

    On error, the response will include:

    ```json
    {
        "error": "ErrorMessage"
    }
    ```

## Contributing
Feel free to open issues or submit pull requests to improve this project.    
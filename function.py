import cv2
import base64
import numpy as np

from tensorflow.keras.models import load_model

# this function return base64 string
# can convert from base64 to image to display the original image on the website
class Function:
    def __init__(self, path_model):
        self.model = load_model(path_model)

    def predict(self, image):

        resize = cv2.resize(image, (190, 250))
        grayscale = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

        i = grayscale / 255.0
        i = np.expand_dims(i, axis=0)

        labels = {
            0: 'Heart',
            1: 'Oblong',
            2: 'Oval',
            3: 'Round',
            4: 'Square'
        }

        predictions = np.argmax(self.model.predict(i))

        return image, labels[predictions]
    
    @classmethod
    def encode_img(self, img):
        _, buffer = cv2.imencode('.jpg', img)
        img_str = base64.b64encode(buffer).decode('utf-8')
        return img_str
    
    @classmethod
    def decode_img(self, file_img):
        nparr = np.frombuffer(file_img, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return image
from flask_cors import CORS
from flask import Flask, request, jsonify

from function import Function

app = Flask(__name__)
CORS(app)

# model = "your/path/model"
model = "face-shape-recognizer.h5"
function = Function(path_model=model)

@app.route("/detection", methods=['POST'])
def detection():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return jsonify({'error': 'Invalid file format'}), 400
    
    if file:
        try:
            image = file.read()
            image = function.decode_img(image)
            img_ori, label = function.predict(image=image)
            image_base64 = function.encode_img(img_ori)
            
            return jsonify({"message": "success process",
                            "label": label,
                            "image_original_base64": image_base64}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
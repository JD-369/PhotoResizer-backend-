from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image
import io

app = Flask(__name__)
CORS(app, origins=["https://pscpicresizer.netlify.app/"])


@app.route('/resize', methods=['POST'])
def resize_image():
    image_file = request.files['image']
    width = int(request.form['width'])
    height = int(request.form['height'])

    image = Image.open(image_file)
    resized_image = image.resize((width, height))

    img_io = io.BytesIO()
    resized_image.save(img_io, format='JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)

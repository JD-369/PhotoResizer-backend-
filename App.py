from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import os

app = Flask(__name__)

# Enable CORS for specific origins (add your Netlify URL here)
CORS(app, origins=["https://pscpicresizer.netlify.app"])

# Resize image endpoint
@app.route('/resize', methods=['POST'])
def resize_image():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400
        
        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        # Open the image using PIL
        image = Image.open(image_file)
        
        # Resize the image (height=200px, width=150px)
        resized_image = image.resize((150, 200))
        
        # Save the resized image to a temporary file
        output_path = "resized_image.jpg"
        resized_image.save(output_path)
        
        return jsonify({"message": "Image resized successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Health check endpoint
@app.route('/')
def home():
    return "Flask backend is running!"

if __name__ == "__main__":
    # Use the PORT environment variable for deployment compatibility
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

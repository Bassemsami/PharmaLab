from flask import Blueprint, render_template, request, jsonify
import cv2
import numpy as np
import base64

manual_selection_blueprint = Blueprint('manual_selection', __name__)

@manual_selection_blueprint.route('/process_image', methods=['POST'])
def process_image():
    image_data = request.form['image_data']
    image_data_decoded = base64.b64decode(image_data.split(',')[1])
    nparr = np.frombuffer(image_data_decoded, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

    return jsonify({'width': img.shape[1], 'height': img.shape[0]})

@manual_selection_blueprint.route('/calculate_pixels', methods=['POST'])
def calculate_pixels():
    image_data = request.form['image_data']
    points_str = request.form['points']

    # Decode image data and convert to numpy array
    image_data_decoded = base64.b64decode(image_data.split(',')[1])
    nparr = np.frombuffer(image_data_decoded, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

    # Convert the points string to a list of tuples with floating-point coordinates
    points = [tuple(map(float, pair.split(','))) for pair in points_str.split(';')]

    # Create a mask based on the selected region
    mask = np.zeros_like(img)
    pts = np.array(points, dtype=np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(mask, [pts], color=255)

    # Calculate the pixel count within the selected region
    pixel_count = int(cv2.countNonZero(mask))

    # Calculate the total number of pixels in the image
    total_pixels = int(np.prod(img.shape))

    return jsonify({'pixel_count': pixel_count, 'total_pixels': total_pixels})

# yolo_api.py
from flask import Blueprint, request, jsonify
from ultralytics import YOLO
import numpy as np
import cv2
import base64

yolo_blueprint = Blueprint('yolo', __name__)

# Load the YOLO model
yolo_model = YOLO('weights/best.pt')

@yolo_blueprint.route('/detect_wound', methods=['POST'])
def detect_wound():
    # Get the image file from the request
    image_path = request.form['image_path']


    # Perform YOLO detection
    results = yolo_model.predict(source=image_path, conf=0.5)
    boxes = results[0].boxes
    boxes = np.int_(boxes.xyxy.numpy())

    # Crop the image based on YOLO bounding box
    image = cv2.imread(image_path)
    cropped_image = image[boxes[0][1]:boxes[0][3], boxes[0][0]:boxes[0][2]]

    # Save the cropped image
    cv2.imwrite('/Users/bassemawad/Desktop/projectgrad/backend/temp_cropped_image.jpg', cropped_image)
    cv2.imwrite('/Applications/XAMPP/xamppfiles/htdocs/CalculateApp/assets/temp_cropped_image.jpg', cropped_image)

    # Return the YOLO results and paths to the original and cropped images
    response = {
        'yolo_results': boxes.tolist(),
        'original_image_path': image_path,
        'cropped_image_path': '/Users/bassemawad/Desktop/projectgrad/backend/temp_cropped_image.jpg'
    }
    from ultralytics import YOLO

    # Load a model
    model = YOLO('weights/bestseg.pt')  # load a custom model

    # Run batched inference on a list of images
    results = model('/Users/bassemawad/Desktop/projectgrad/backend/temp_cropped_image.jpg')
    
    # Process results list
    for result in results:
        masks = result.masks  # Masks object for segmentation masks outputs
    from PIL import Image

    for r in results:
        im_array = r.plot(labels=False, boxes=False)  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save('results2.jpg')  # save image
        im.save('/Applications/XAMPP/xamppfiles/htdocs/CalculateApp/assets/results.jpg')
    image = cv2.imread('/Users/bassemawad/Desktop/projectgrad/backend/temp_cropped_image.jpg')
    mask_tensor = result.masks.data 
    binary_masks = (mask_tensor > 0.5).int()
    pixel_counts = binary_masks.view(binary_masks.shape[0], -1).sum(dim=1)

    bigoutput=binary_masks.shape[1]*binary_masks.shape[2]
    originaloutput= image.shape[0]*image.shape[1]
    pixelcountbig=pixel_counts.item()
    wound_count = originaloutput*pixelcountbig/bigoutput


    return jsonify({ 'response': response, 'wound_count': wound_count })
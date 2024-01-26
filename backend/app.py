from flask import Flask, jsonify,request,Response,redirect,url_for,session
from manual_selection_api import manual_selection_blueprint
from yolo_api import yolo_blueprint
from signup import signup_blueprint
from login import login_blueprint
from project import project_blueprint
from mouse import mouse_blueprint
from calculation import calculation_blueprint
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(manual_selection_blueprint, url_prefix='/manual_selection')
app.register_blueprint(yolo_blueprint, url_prefix='/yolo')
app.register_blueprint(signup_blueprint,url_prefix='/signup')
app.register_blueprint(login_blueprint,url_prefix='/login')
app.register_blueprint(project_blueprint,url_prefix='/project')
app.register_blueprint(mouse_blueprint,url_prefix='/mouse')
app.register_blueprint(calculation_blueprint,url_prefix='/calculation')
# Define the main route as an API endpoint
@app.route('/')
def index():
    # Return a simple JSON response or some data for the Vue app
    return jsonify({"message": "Welcome to the API"})

if __name__ == "__main__":
    app.run(debug=True)
from flask import Blueprint, request, jsonify
import pymysql

signup_blueprint = Blueprint('signup_blueprint', __name__)

# Function to create a new MySQL connection
def get_db_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='MiceProj',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

@signup_blueprint.route('/signupAuth', methods=['POST'])
def add_user():
    data = request.json
    name = data['name']
    email = data['email']
    password = data['password']  # Make sure to hash passwords in a real app
    orgname = data['organisationname']

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO user (name, email, password, `organisationname`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, email, password, orgname))
            connection.commit()
        message = 1
    except Exception as e:
        connection.rollback()
        message = 0
    finally:
        connection.close()

    return jsonify({'message': message})

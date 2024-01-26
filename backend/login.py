from flask import Blueprint, request, jsonify
import pymysql

login_blueprint = Blueprint('login_blueprint', __name__)

# Function to create a new MySQL connection
def get_db_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='MiceProj',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)


@login_blueprint.route('/loginAuth', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')  

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # SQL query to find user with the given email and password
            sql = "SELECT ID FROM user WHERE email = %s AND password = %s"
            cursor.execute(sql, (email, password))
            user = cursor.fetchone() 
           
        if user:
            return jsonify({'message':1,'user': user}), 200
        else:
            return jsonify({'message': 'Invalid email or password'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    finally:
        connection.close()

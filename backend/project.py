from flask import Blueprint, request, jsonify
import pymysql
from datetime import datetime
project_blueprint = Blueprint('project_blueprint', __name__)

# Function to create a new MySQL connection
def get_db_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='MiceProj',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

@project_blueprint.route('/addproject', methods=['POST'])
def add_project():
    data = request.json
    projectname = data['projectname']
    currdate = datetime.now()
    datenow = currdate.strftime("%Y-%m-%d %H:%M:%S")
    createdby = data['createdby']
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO project (projectname, createddate, createdby) VALUES (%s,%s,%s)"
            cursor.execute(sql, (projectname,datenow,createdby))
            connection.commit()
        message = "project added successfully."
    except Exception as e:
        connection.rollback()
        message = f"An error occurred: {e}"
    finally:
        connection.close()

    return jsonify({'message': message})

@project_blueprint.route('/showproject', methods=['POST'])
def showproject():
    data = request.json
    createdby = data['createdby']
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # SQL query to find user with the given email and password
            sql = "SELECT * FROM project WHERE createdby = %s"
            cursor.execute(sql, (createdby))
            proj = cursor.fetchall()

        if proj:
            return jsonify({'message': 1, 'proj': proj}), 200
        else:
            return jsonify({'message': 2})
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    finally:
        connection.close()



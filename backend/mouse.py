from flask import Blueprint, request, jsonify
import pymysql
from datetime import datetime
mouse_blueprint = Blueprint('mouse_blueprint', __name__)

# Function to create a new MySQL connection
def get_db_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='MiceProj',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

@mouse_blueprint.route('/addmouse', methods=['POST'])
def add_mouse():
    currdate = datetime.now()
    data = request.json
    mouseName = data['mouseName']
    project = data['project']
    datenow = currdate.strftime("%Y-%m-%d %H:%M:%S")
    createdby = data['createdby']
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO mouse (mouseName, project, createdby, date) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, (mouseName,project,createdby,datenow))
            connection.commit()
        message = "mouse added successfully."
    except Exception as e:
        connection.rollback()
        message = f"An error occurred: {e}"
    finally:
        connection.close()

    return jsonify({'message': message})

@mouse_blueprint.route('/showmouse', methods=['POST'])
def showmouse():
    data = request.json
    createdby = data['createdby']
    project = data['project']
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:

            sql = "SELECT * FROM mouse WHERE createdby = %s AND project = %s ORDER BY mouseName ASC"
            cursor.execute(sql, (createdby,project))
            mice = cursor.fetchall()
        if mice:
            return jsonify({'message': 1, 'mouse': mice}), 200
        else:
            return jsonify({'message': 2}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    finally:
        connection.close()
@mouse_blueprint.route('/<int:mouse_id>', methods=['DELETE'])
def delete_calculation(mouse_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:

            sql = "DELETE FROM mouse WHERE mouseID = %s"
            cursor.execute(sql, (mouse_id))
            connection.commit()
        return jsonify({'message': 1}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    finally:
        connection.close()
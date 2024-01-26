from flask import Blueprint, request, jsonify
import pymysql
from datetime import datetime
calculation_blueprint = Blueprint('calculation_blueprint', __name__)


def get_db_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           db='MiceProj',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

@calculation_blueprint.route('/addcalculation', methods=['POST'])
def add_calculation():
    currdate = datetime.now()
    data = request.json
    mouseID = data['mouseID']
    projectID = data['projectID']
    pixels = data['pixels']
    datenow = currdate.strftime("%Y-%m-%d %H:%M:%S")
    createdby = data['createdby']
    percentage = 0
    
    day = data['day']
    oold=1
    demoday = int(day)
    if demoday > 1:
        
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT pixels FROM calculation WHERE createdby = %s AND projectID = %s AND mouseID = %s AND day = %s"
                cursor.execute(sql, (createdby, projectID, mouseID,oold))
                connection.commit()
            resu = cursor.fetchone()
            id_value = resu["pixels"]
            temp=float(pixels)/id_value
            percentagetemp= temp*100
            percentage = 100-percentagetemp
            
        
            
        except Exception as e:
            connection.rollback()
            message = f"An error occurred: {e}"
        finally:
            connection.close()

   

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO calculation (mouseID, projectID, pixels, date, createdby, percentage, day) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (mouseID, projectID, pixels, datenow, createdby, percentage, day))
            connection.commit()
            message = 1
        
    except Exception as e:
        connection.rollback()
        message = f"An error occurred: {e}"
    finally:
        connection.close()

    return jsonify({'message': message})

@calculation_blueprint.route('/showcalculation', methods=['POST'])
def showcalculation():
    data = request.json
    createdby = data['createdby']
    projectID = data['projectID']
    mouseID = data['mouseID']
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:

            sql = "SELECT * FROM calculation WHERE createdby = %s AND projectID = %s AND mouseID = %s ORDER BY day ASC"
            cursor.execute(sql, (createdby,projectID,mouseID))
            mice = cursor.fetchall()
        if mice:
            return jsonify({'message': 1, 'calculation': mice}), 200
        else:
            return jsonify({'message': 2}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    finally:
        connection.close()

@calculation_blueprint.route('/<int:calculation_id>', methods=['DELETE'])
def delete_calculation(calculation_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:

            sql = "DELETE FROM calculation WHERE id = %s"
            cursor.execute(sql, (calculation_id,))
            connection.commit()
        return jsonify({'message': 1}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    finally:
        connection.close()



@calculation_blueprint.route('/showdays', methods=['POST'])
def showdays():
    data = request.json
    createdby = data['createdby']
    projectID = data['projectID']

    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:

            sql = "SELECT distinct day FROM mousecalculations WHERE createdby = %s AND projectID = %s ORDER BY day ASC"
            cursor.execute(sql, (createdby,projectID))
            days = cursor.fetchall()
        if days:
            return jsonify({'message': 1, 'days': days}), 200
        else:
            return jsonify({'message': 2}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    finally:
        connection.close()
@calculation_blueprint.route('/oneday', methods=['POST'])
def oneday():
    data = request.json
    createdby = data['createdby']
    projectID = data['projectID']
    day = data['day']
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:

            sql = "SELECT * FROM mousecalculations WHERE createdby = %s AND projectID = %s AND day = %s ORDER BY mouseName ASC"
            cursor.execute(sql, (createdby,projectID,day))
            mice = cursor.fetchall()
        if mice:
            return jsonify({'message': 1, 'calculation': mice}), 200
        else:
            return jsonify({'message': 2}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    finally:
        connection.close()
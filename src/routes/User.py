from flask import Blueprint, jsonify, request

#Entities
from models.entities.User import User

# Models
from models.UserModel import UserModel

main = Blueprint('users_blueprint', __name__)


@main.route('/')
def get_usuarios():
    try:
        users = UserModel.get_users()
        return jsonify(users)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_usuario(id):
    try:
        user = UserModel.get_user(id)
        if user != None:
            return jsonify(user)
        else:
            return jsonify({}),404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_user():
    try:
        id=request.json['id']
        nombre=request.json['nombre']
        apellido=request.json['apellido']
        edad=int(request.json['edad'])
        user=User(id,nombre,apellido,edad)

        affected_rows = UserModel.add_user(user)

        if affected_rows == 1:
            return jsonify({'message': "User Create"}), 200
        else:
            return jsonify({'message': "Error on Insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User(id)

        affected_rows = UserModel.delete_user(user)

        if affected_rows == 1:
            return jsonify({'message': "User Deleted"}), 200
        else:
            return jsonify({'message': "No User Deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_user(id):
    try:
        nombre=request.json['nombre']
        apellido=request.json['apellido']
        edad=int(request.json['edad'])
        user=User(id,nombre,apellido,edad)

        affected_rows = UserModel.update_user(user)

        if affected_rows == 1:
            return jsonify({'message': "User Updated"}), 200
        else:
            return jsonify({'message': "Error on Updated"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/promedio-edad', methods=['GET'])
def prom_users():
    try:
        promedio = UserModel.prom_users()
        return jsonify({'PromedioEdad': promedio})
    except Exception as ex:
        return jsonify({'message': "Error en Promediar Edades"}), 500

@main.route('/status', methods=['GET'])
def status_users():
    try:
        status = UserModel.status_users()
        return jsonify({'NameSystem': status[0], 'Version': status[1], 'Developer': status[2], 'Email': status[3]})
    except Exception as ex:
        return jsonify({'message': "Error al Mostrar Status"}), 500
from flask import request, jsonify
from models.user_model import UserModel

class UserController:

    @staticmethod
    def create_user():
        data = request.json
        user = UserModel.create(data.get('name'), data.get('email'))
        return jsonify(user), 201

    @staticmethod
    def get_users():
        return jsonify(UserModel.get_all())

    @staticmethod
    def get_user(user_id):
        user = UserModel.get(user_id)
        if user:
            return jsonify(user)
        return jsonify({'error': 'User not found'}), 404

    @staticmethod
    def update_user(user_id):
        data = request.json
        user = UserModel.update(user_id, data.get('name'), data.get('email'))
        if user:
            return jsonify(user)
        return jsonify({'error': 'User not found'}), 404

    @staticmethod
    def delete_user(user_id):
        user = UserModel.delete(user_id)
        if user:
            return jsonify(user)
        return jsonify({'error': 'User not found'}), 404

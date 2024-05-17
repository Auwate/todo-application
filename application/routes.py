import random

from flask import request, jsonify, Response, abort
from database import db, Item


def register_routes(app):

    @app.errorhandler(400)
    def error_handler_400(error_str: str) -> Response:
        data = {"code": 400,
                "response": str(error_str)}
        return jsonify(data)

    @app.errorhandler(404)
    def error_handler_404(error_str: str) -> Response:
        data = {"code": 404,
                "response": str(error_str)}
        return jsonify(data)

    @app.route('/create', methods=['POST'])
    def create() -> Response:

        if not request.is_json:
            abort(400, description="Data is not in json format")

        data = request.get_json()

        if not data or 'name' not in data:
            abort(code=400, description="Invalid data provided")

        name = data['name']
        description = data.get("description", None)
        id_value = data.get('id', random.randint(0, 2_000_000_000))

        db.session.add(Item(name=name, id=id_value, description=description))
        db.session.commit()

        return jsonify({"code": 200,
                        "response": "success"})

    @app.route("/read", methods=['GET'])
    def read() -> Response:

        all_items: list[Item] = Item.query.all()

        return_values = {"code": 200, "response": []}

        for item in all_items:

            current = {
                'name': item.name,
                'attributes': {
                    'id': item.id,
                    'description': item.description
                },
            }

            return_values['response'].append(current)

        return jsonify(return_values)

    @app.route("/update", methods=['PUT'])
    def update() -> Response:

        if not request.is_json:
            abort(400, description="Data is not in json format")

        data = request.get_json()

        if not data or 'id' not in data:
            abort(code=400, description="Invalid data provided")

        item = Item.query.get(data['id'])

        if not item:
            abort(code=400, description="Invalid ID provided")

        if 'name' in data:
            item.name = data['name']

        if 'description' in data:
            item.description = data['description']

        db.session.commit()

        return jsonify({"code": 200,
                        "response": "success"})

    @app.route('/delete', methods=['DELETE'])
    def delete() -> Response:

        if not request.is_json:
            abort(400, description="Data is not in json format")

        data = request.get_json()

        if not data or 'id' not in data:
            abort(code=400, description="Invalid data provided")

        item = Item.query.get(data['id'])

        if not item:
            abort(code=400, description="Invalid ID provided")

        db.session.delete(item)
        db.session.commit()

        return jsonify({"code": 200,
                        "response": "success"})

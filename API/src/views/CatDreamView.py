from flask import request, json, Response, Blueprint, g
from ..models.CatDreamModel import CatDreamModel, CatDreamSchema
from ..shared.Authentication import Auth

# from marshmallow import pprint

catdream_api = Blueprint('catdream_api', __name__)
catdream_schema = CatDreamSchema()

@Auth.auth_required
@catdream_api.route('/create', methods=['POST'])
def create() :
    """
    Create Catégorie for Dream Function
    """
    req_data = request.get_json()
    data, error = catdream_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    cat_in_db = CatDreamModel.get_one_cat(data.get('name'))

    if cat_in_db:
        message = {
            'error': 'Cat already exist, please supply another categorie name'}
        return custom_response(message, 400)

    catDream = CatDreamModel(data)
    catDream.save()

    return custom_response(data, 201)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
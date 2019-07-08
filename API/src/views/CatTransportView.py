# -*- coding: utf-8 -*-
from flask import request, json, Response, Blueprint, g
from ..models.CatTransportModel import CatTransportModel, CatTransportSchema
from ..shared.Authentication import Auth

# from marshmallow import pprint

cattransp_api = Blueprint('cattransp_api', __name__)
cattransp_schema = CatTransportSchema()

@cattransp_api.route('/create', methods=['POST'])
@Auth.auth_required
def create() :
    """
    Create Catégorie for Dream Function
    """
    req_data = request.get_json()
    data, error = cattransp_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    cat_in_db = CatTransportModel.get_one_cat(data.get('name'))

    if cat_in_db:
        message = {
            'error': 'Cat already exist, please supply another categorie name'}
        return custom_response(message, 400)

    catTransp = CatTransportModel(data)
    catTransp.save()

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
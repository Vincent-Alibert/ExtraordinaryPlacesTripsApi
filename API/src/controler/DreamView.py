# -*- coding: utf-8 -*-
from flask import request, jsonify, json, Response, Blueprint, g
from ..models.DreamModel import DreamModel, DreamSchema
from ..models.CatDreamModel import CatDreamModel
from ..models.CatTransportModel import CatTransportModel
from ..shared.Authentication import Auth
from marshmallow import ValidationError

# from marshmallow import pprint

dream_api = Blueprint('dream_api', __name__)
dream_schema = DreamSchema()


@dream_api.route('/create', methods=['POST'])
@Auth.auth_required
def create():
    """
    Create Dream Function
    """
    req_data = request.get_json()
    if not req_data:
        return custom_response({'message': 'No input data provided'}, 400)

    req_data['ownerUser'] = g.user.get('id')
    data, error = dream_schema.load(req_data)

    catDream = req_data["catOfDream"]
    catTransp = req_data["catOfTransport"]

    if error:
        return custom_response(error, 400)

    if "catOfDream" in data:
        del data["catOfDream"]

    if "catOfTransport" in data:
        del data["catOfTransport"]

    dream = DreamModel(data)

    if "catOfDream" in req_data:
        for cat in req_data['catOfDream']:
            getCatDream = CatDreamModel.get_one_cat(cat["name"])
            # if catDream is None:
            #     # Create a new author
            #     catDream = CatDreamModel(cat)
            #     catDream.save()
            dream.catOfDream.append(getCatDream)
    data["catOfDream"] = catDream

    if "catOfTransport" in req_data:
        for cat in req_data['catOfTransport']:
            catTrans = CatTransportModel.get_one_cat(cat["name"])
            # if catTrans is None:
            #    # Create a new author
            #    catTrans = CatTransportModel(cat)
            #    catTrans.save()
            dream.catOfTransport.append(catTrans)

    data["catOfTransport"] = catTransp
    dream.save()
    data["idDream"] = dream.idDream
    return custom_response(data, 201)


@dream_api.route('/edit/<int:dream_id>', methods=['PUT'])
@Auth.auth_required
def update(dream_id):
    """
    Update A Blogpost
    """
    req_data = request.get_json()
    dream = DreamModel.get_one_dream(dream_id)

    if not dream:
        return custom_response({'error': 'dream not found'}, 404)

    data = dream_schema.dump(dream).data

    print("data")
    print(data)

    if data.get('ownerUser') != g.user.get('id'):
        return custom_response({'error': 'permission denied'}, 400)

    data, error = dream_schema.load(req_data, partial=True)

    print('*********')
    print(error)

    if error:
        return custom_response(error, 400)

    catDream = req_data["catOfDream"]
    catTransp = req_data["catOfTransport"]

    if "catOfDream" in data:
        del data["catOfDream"]

    if "catOfTransport" in data:
        del data["catOfTransport"]

    arrayValueCatDream = []
    arrayValueCatTravel=[]
    for catResq in req_data['catOfDream'] :
        arrayValueCatDream.append(catResq['name'])
    for catResq in req_data['catOfTransport'] :
        arrayValueCatDream.append(catResq['name'])

    if "catOfDream" in req_data:
        for cat in dream.catOfDream :
            if not cat.name in arrayValueCatDream :
                dream.catOfDream.remove(cat)

        for cat in req_data['catOfDream']:
            getCatDream = CatDreamModel.get_one_cat(cat["name"])
            # if catDream is None:
            #     # Create a new author
            #     catDream = CatDreamModel(cat)
            #     catDream.save()
            if not getCatDream in dream.catOfDream :
                dream.catOfDream.append(getCatDream)
    
    if "catOfTransport" in req_data:

        for cat in dream.catOfTransport :
            if not cat.name in arrayValueCatTravel :
                dream.catOfTransport.remove(cat)

        for cat in req_data['catOfTransport']:
            catTrans = CatTransportModel.get_one_cat(cat["name"])
            # if catTrans is None:
            #    # Create a new author
            #    catTrans = CatTransportModel(cat)
            #    catTrans.save()
            dream.catOfTransport.append(catTrans)
    
    dream.update(data)

    data = dream_schema.dump(dream).data
    return custom_response(data, 200)


@dream_api.route('/view/<int:dream_id>', methods=['GET'])
@Auth.auth_required
def get_a_dream(dream_id):
    """
    Get a single dream
    """
    dream = DreamModel.get_one_dream(dream_id)
    if dream.ownerUser != g.user.get('id') :
      return custom_response({'error': 'Not allowed, you can only access your dreams'}, 403)
    if not dream:
        return custom_response({'error': 'dream not found'}, 404)

    ser_dream = dream_schema.dump(dream).data
    return custom_response(ser_dream, 200)


@dream_api.route('/all', methods=['GET'])
@Auth.auth_required
def get_a_dream_by_user():
    """
    Get all dreams
    """
    dreams = DreamModel.get_dreams_user(g.user.get('id'))
    if not dreams:
        return custom_response({'error': 'dreams not found'}, 404)

    ser_dream = dream_schema.dump(dreams, many=True).data
    return custom_response(ser_dream, 200)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )

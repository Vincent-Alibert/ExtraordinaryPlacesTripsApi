from flask import request, json, Response, Blueprint, g
from ..models.DreamModel import DreamModel, DreamSchema
from ..models.CatDreamModel import CatDreamModel
from ..shared.Authentication import Auth

# from marshmallow import pprint

dream_api = Blueprint('dream_api', __name__)
dream_schema = DreamSchema()

@dream_api.route('/create', methods=['POST'])
# @Auth.auth_required
def create() :
    """
    Create Dream Function
    """
    req_data = request.get_json()
    print(req_data)
    # req_data['ownerUser'] = g.user.get('id')
    data, error = dream_schema.load(req_data)

    if error:
        print("*********************")
        print(dream_schema.load(req_data))
        print("*********************")
        return custom_response(error, 400)

    dream = DreamModel(data)

    for cat in req_data['catOfDream']:
        catDream = CatDreamModel.get_one_cat(cat)
        dream.catOfDream.append(catDream)
        
    dream.save()

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
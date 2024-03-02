import json

from flask_apispec import MethodResource, marshal_with, doc
from helper import response_message, RequestResponse
from model import User, Hackathon
from middleware import TokenRequired


class GetHackathonById(MethodResource):

    @doc(
        description='Get Hackathon by ID',
        params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }
        }
    )
    @marshal_with(RequestResponse)
    @TokenRequired
    def get(self, auth, **kwargs):
        # / hackathon / < int: id >
        id=kwargs.get('id')
        hackathon = Hackathon.query.filter_by(hackathon_id=id).first()
        if not hackathon:
            return response_message(404, 'fail', 'Hackathon does not exist.')
        data = hackathon.to_dict()
        return response_message(200, 'success', 'Successfully get session data.', data)

import json

from flask_apispec import MethodResource, marshal_with, doc
from helper import response_message, RequestResponse, Serializers
from model import User, Hackathon, Teams
from middleware import TokenRequired


class GetTeams(MethodResource):

    @doc(
        description='Get Teams',
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
        # get page_number
        page_number = kwargs.get('page_number')
        # get page_size
        page_size = kwargs.get('page_size')
        # use pagination
        teams = Teams.query.paginate(page_number, page_size, False)
        # convert to list
        teams = teams.items
        if not teams:
            return response_message(200, 'success', 'Successfully get session data.', [])
        return response_message(200, 'success', 'Successfully get session data.', [hack.to_dict() for hack in teams])

import json

from flask_apispec import MethodResource, marshal_with, doc
from helper import response_message, RequestResponse
from model import User, Hackathon,Teams
from middleware import TokenRequired


class GetTeamById(MethodResource):

    @doc(
        description='Get Team by ID',
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
        teams = Teams.query.filter_by(team_id=id).first()
        print(teams.to_dict())
        if not teams:
            return response_message(404, 'fail', 'Teams does not exist.')
        data = teams.to_dict()
        return response_message(200, 'success', 'Successfully get session data.', data)

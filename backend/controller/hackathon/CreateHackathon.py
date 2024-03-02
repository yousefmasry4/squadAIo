from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from helper import response_message, RequestResponse, RequestPost, Serializers
from model import User, Hackathon
from middleware import TokenRequired
from src import db


class CreateHackathonPost(RequestPost):
    fields_ = RequestPost.fields_
    hackathon_name = fields_.Str(required=True, description="Input Field for Team Name")
    hackathon_theme = fields_.Str(required=True, description="Input Field for Team Description")
    reg_start = fields_.DateTime(required=True, description="Input Field for Team Description")
    reg_end = fields_.DateTime(required=True, description="Input Field for Team Description")
    event_start = fields_.DateTime(required=True, description="Input Field for Team Description")
    event_end = fields_.DateTime(required=True, description="Input Field for Team Description")





class CreateHackathon(MethodResource):

    @doc(
        description='Create Hackathon Endpoint.'
    )
    @use_kwargs(CreateHackathonPost, location='json')
    @marshal_with(RequestResponse)
    @TokenRequired
    def post(self, auth, **kwargs):
        # get user info from token
        user = User.query.filter_by(username=auth['resp']['sub']['data']['username']).first()

        # add user to team
        try:
            hackathon = Serializers(kwargs).ValidatingCreateHackathon()
            db.session.add(hackathon)
            db.session.commit()
            return response_message(201, 'success', 'Successfully Create Hackathon.')
        except Exception as e:
            print(e, )
            return response_message(500, 'fail', f'Some error occurred. Please try again. {e}')



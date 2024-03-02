from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from helper import response_message, RequestResponse, RequestPost, Serializers
from model import User, challenges
from middleware import TokenRequired
from src import db


class CreateChallengePost(RequestPost):
    fields_ = RequestPost.fields_
    # challenge_name, challenge_description, hackathon_id):
    challenge_name = fields_.Str(required=True, description="Input Field for Challenge Name")
    challenge_description = fields_.Str(required=True, description="Input Field for Challenge Description")
    hackathon_id = fields_.Str(required=True, description="Input Field for Hackathon ID")





class CreateChallenge(MethodResource):

    @doc(
        description='Create Challenge Endpoint.'
    )
    @use_kwargs(CreateChallengePost, location='json')
    @marshal_with(RequestResponse)
    @TokenRequired
    def post(self, auth, **kwargs):
        # get user info from token
        user = User.query.filter_by(username=auth['resp']['sub']['data']['username']).first()
        # check if user is admin
        # if not user.user_type != 'admin':
        #     return response_message(401, 'fail', 'You are not authorized to perform this action.')

        # add user to team
        try:
            challenge = Serializers(kwargs).ValidatingCreateChallenge()
            db.session.add(challenge)
            db.session.commit()
            return response_message(201, 'success', 'Successfully Create challenge.')
        except Exception as e:
            print(e, )
            return response_message(500, 'fail', f'Some error occurred. Please try again. {e}')



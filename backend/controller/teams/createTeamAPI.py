from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from helper import response_message, RequestResponse, RequestPost, Serializers
from model import User,Teams, Hackathon, challenges
from middleware import TokenRequired
from src import db


class CreateTeamPost(RequestPost):
    fields_ = RequestPost.fields_
    team_name = fields_.Str(required=True, description="Input Field for Team Name")
    team_description = fields_.Str(required=True, description="Input Field for Team Description")
    hackathon_id = fields_.Str(required=True, description="Input Field for Hackathon ID")
    challenge_id = fields_.Str(required=True, description="Input Field for Challenge ID")






class CreateTeam(MethodResource):

    @doc(
        description='Create Team Endpoint.'
    )
    @use_kwargs(CreateTeamPost, location='json')
    @marshal_with(RequestResponse)
    @TokenRequired
    def post(self, auth, **kwargs):
        # get user info from token
        user = User.query.filter_by(username=auth['resp']['sub']['data']['username']).first()


        # add user to team
        try:
            # check if hackathon exist
            try:
                hackathon = Hackathon.query.filter_by(hackathon_id=kwargs.get('hackathon_id')).first()
                challenge_id = challenges.query.filter_by(challenge_id=kwargs.get('challenge_id')).first()
                # create team
                # (self, team_name, team_description, challenge_id, team_leader, hackathon_id, team_order
                #  =None, code_submissions=None):
                if not hackathon:
                    return response_message(404, 'fail', 'Hackathon does not exist.')
                if not challenge_id:
                    return response_message(404, 'fail', 'Challenge does not exist.')
            except Exception as e:
                return response_message(404, 'fail', f'Hackathon or challange does not exist.')
            team = Serializers(kwargs).ValidatingCreateTeam(
                team_leader=user.username,
            )
            db.session.add(team)
            db.session.commit()
            return response_message(201, 'success', 'Successfully Create Team.')
        except Exception as e:
            print(e, )
            return response_message(500, 'fail', f'Some error occurred. Please try again. {e}')



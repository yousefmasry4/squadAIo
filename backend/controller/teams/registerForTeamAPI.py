from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from helper import response_message, RequestResponse, RequestPost, Serializers
from model import User,Teams, Hackathon
from middleware import TokenRequired
from src import db


class RegisterForTeamPost(RequestPost):
    fields_ = RequestPost.fields_
    team_id = fields_.Str(required=True, description="Input Field for Team ID")






class RegisterForTeam(MethodResource):

    @doc(
        description='Register For Team Endpoint.'
    )
    @use_kwargs(RegisterForTeamPost, location='json')
    @marshal_with(RequestResponse)
    @TokenRequired
    def post(self, auth, **kwargs):
        # get user info from token with all relationships
        user = User.query.filter_by(username=auth['resp']['sub']['data']['username']).first()


        # add user to team
        try:
            try:
                team = Teams.query.filter_by(team_id=kwargs.get('team_id')).first()
                if not team:
                    return response_message(404, 'fail', 'Team does not exist.')

                if len(user.team) != 0:
                    return response_message(404, 'fail', 'You are already in a team. with team id: ' + str(user.team[0].team_id))
            #     check if user is not in the team
                if len(user.team) != 0 and user.team[0].team_id == team.team_id:
                    return response_message(404, 'fail', 'You are already in the team.')
                if len(user.team) != 0 and user.username == team.team_leader:
                    return response_message(404, 'fail', 'You are the team leader.')

            except Exception as e:
                return response_message(404, 'fail', f'Team does not exist, or you are already in the team. {e}')
            # check if user is not in the team
            user.team.append(team)
            db.session.add(user)
            db.session.commit()
            return response_message(201, 'success', 'Successfully added to the Team.')
        except Exception as e:
            print(e, )
            return response_message(500, 'fail', f'Some error occurred. Please try again. {e}')



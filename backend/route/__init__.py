from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

from flask_apispec import FlaskApiSpec
from werkzeug.utils import redirect
from flask_restful import Api

from helper import response_message

from controller import (
    app,
    RegisterAPI,
    LoginAPI,
    LogoutAPI,
    UpdateUserInformation,
    UpdatePassword,
    UpdateUsername,
    GetCurrentUser,
    GetUserByName,
    RefreshJWTToken,
    CreateTeam,
GetTeamById,
GetTeams,
GetHackathonById,
CreateHackathon,
RegisterForTeam,
GetHackathons,
    CreateChallenge
)

# check database create or not


app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Flask Authentication API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='3.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/docs/json',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/docs'  # URI to access UI of API Doc
})


@app.route('/', methods=['GET', 'POST', 'PATCH'])
@app.route('/api', methods=['GET', 'POST', 'PATCH'])
def redirect_to_json_api():
    return redirect('/docs/json')


ENDPOINT = app.config.get('APP_PREFIX')

api = Api(app)
docs = FlaskApiSpec(app)

# This error handler is necessary for usage with Flask-RESTful
@app.errorhandler(422)
def handle_request_parsing_error(err):
    exc = err.exc
    messages = exc.messages
    return response_message(422, 'error', 'Validation error', messages)

@app.errorhandler(404)
def resource_not_found(e):
    return response_message(404, 'error', 'Resource not found', str(e))


api.add_resource(RegisterAPI, f'{ENDPOINT}/auth/register', methods=['POST'])
docs.register(RegisterAPI)

api.add_resource(LoginAPI, f'{ENDPOINT}/auth/login', methods=['POST'])
docs.register(LoginAPI)

api.add_resource(LogoutAPI, f'{ENDPOINT}/auth/logout', methods=['POST'])
docs.register(LogoutAPI)

api.add_resource(GetCurrentUser, f'{ENDPOINT}/auth/user', methods=['GET'])
docs.register(GetCurrentUser)

api.add_resource(RefreshJWTToken, f'{ENDPOINT}/auth/refresh', methods=['GET'])
docs.register(RefreshJWTToken)

api.add_resource(UpdateUserInformation, f'{ENDPOINT}/auth/user', methods=['PATCH'])
docs.register(UpdateUserInformation)

api.add_resource(UpdatePassword, f'{ENDPOINT}/auth/user/password', methods=['PATCH'])
docs.register(UpdatePassword)

api.add_resource(UpdateUsername, f'{ENDPOINT}/auth/user/username', methods=['PATCH'])
docs.register(UpdateUsername)

api.add_resource(GetUserByName, f'{ENDPOINT}/user', methods=['GET'])
docs.register(GetUserByName)



# - team routes
# create team
api.add_resource(CreateTeam, f'{ENDPOINT}/team', methods=['POST'])
docs.register(CreateTeam)
# get team by id
api.add_resource(GetTeamById, f'{ENDPOINT}/team/<string:id>', methods=['GET'])
docs.register(GetTeamById)

# get list of teams
api.add_resource(GetTeams, f'{ENDPOINT}/teams/<int:page_number>/<int:page_size>', methods=['GET'])
docs.register(GetTeams)

# register for team
api.add_resource(RegisterForTeam, f'{ENDPOINT}/team/register', methods=['POST'])
docs.register(RegisterForTeam)




# - hackathon routes
# create hackathon
api.add_resource(CreateHackathon, f'{ENDPOINT}/hackathon', methods=['POST'])
docs.register(CreateHackathon)



# get list of hackathons
api.add_resource(GetHackathons, f'{ENDPOINT}/hackathons/<int:page_number>/<int:page_size>', methods=['GET'])
docs.register(GetHackathons)

# get hackathon by id where id is uuid
api.add_resource(GetHackathonById, f'{ENDPOINT}/hackathon/<string:id>', methods=['GET'])
docs.register(GetHackathonById)

# add challenge to hackathon
api.add_resource(CreateChallenge, f'{ENDPOINT}/hackathon/challenge', methods=['POST'])
docs.register(CreateChallenge)




# - code submission routes
# submit code
# api.add_resource(SubmitCode, f'{ENDPOINT}/code', methods=['POST'])

# get code by id
# api.add_resource(GetCodeById, f'{ENDPOINT}/code/<int:id>', methods=['GET'])

# get list of codes
# api.add_resource(GetCodes, f'{ENDPOINT}/codes', methods=['GET'])

# score code
# api.add_resource(ScoreCode, f'{ENDPOINT}/code/score', methods=['POST'])




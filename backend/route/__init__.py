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
    GetHeroName,
    ValidateReferralCode,
    GetCurrentUser,
    GetUserByName,
    CheckReferralCode,
    RefreshJWTToken
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

# get team by id

# get list of teams

# register for team

# get team members



# - hackathon routes
# create hackathon

# get hackathon by id

# get list of hackathons

# register for hackathon

# addchallenge to hackathon




# - code submission routes
# submit code

# get code by id

# get list of codes

# score code




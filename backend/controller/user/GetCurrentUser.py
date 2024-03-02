from flask_apispec import MethodResource, marshal_with, doc
from helper import response_message, RequestResponse
from model import User
from middleware import TokenRequired


class GetCurrentUser(MethodResource):

    @doc(
        description='Get Current Logged in User',
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
        user = User.query.filter_by(username=auth['resp']['sub']['data']['username']).first()
        data = {
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'referral_code': user.referral_code,
            'registered_on': user.registered_on,
            'user_type': user.user_type,
            'last_logged_in': user.last_logged_in,
            'last_logged_out': user.last_logged_out,
            'mobile': user.mobile,
            'auth_token': auth['auth_token'],
            'title': user.title
        }
        return response_message(200, 'success', 'Successfully get session data.', data)

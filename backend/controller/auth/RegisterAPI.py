import sys

from flask_apispec import MethodResource, marshal_with, doc, use_kwargs
from helper import response_message, Serializers, RequestResponse, RequestPost
from model import User
from controller import db
import logging
logging.basicConfig(level=logging.DEBUG)


class RegisterRequest(RequestPost):
    fields_ = RequestPost.fields_
    username = fields_.Str(required=True, description="Input Field for Username")
    password = fields_.Str(required=True, description="Input Field for Password len should be more than 6",validate=lambda x: len(x) > 6)
    email = fields_.Str(required=True, description="Input Field for Email",validate=lambda x: '@' in x)
    name = fields_.Str(required=True, description="Input Field for Name")
    title = fields_.Str(required=False, description="Required only if user_type is user")
    mobile = fields_.Str(required=False, description="Required only if user_type is user")
    # type is user or admin or superadmin
    user_type = fields_.Str(required=False, description="user_type is user or admin or superadmin",validate=lambda x: x in ['user', 'admin', 'superadmin'])



class RegisterAPI(MethodResource):

    @doc(
        description='Register Endpoint.'
    )
    @use_kwargs(RegisterRequest, location='json')
    @marshal_with(RequestResponse)
    def post(self, **kwargs):
        user = User.query.filter_by(username=kwargs.get('username')).first()
        print(Serializers(kwargs).data)
        try:
            if not user:
                try:
                    user = Serializers(kwargs).ValidatingRegister()
                    db.session.add(user)
                    db.session.commit()
                    return response_message(201, 'success', 'Successfully registered.')
                except Exception as e:
                    return response_message(401, 'fail', f'Some error occurred. Please try again. {e}')
            else:
                return response_message(202, 'already_exists', 'User already exists. Please Log in.')
        except Exception as e:
            print(e, file=sys.stderr)
            return response_message(500, 'fail', f'Some error occurred. Please try again. {e}')
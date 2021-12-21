
from ...helpers.response import sendSuccess, sendCreated, sendUnprocessableEntity, sendInternalServerError

from .validator import Validator

import json

def signUpValidation(function):
    def wrap(request, *args, **kwargs):

        # https://docs.python-cerberus.org/en/stable/usage.html

        # body = json.loads(request.body)

        # data = JSONParser().parse(request)

        # print('signUpValidation -> data', data)

        print('signUpValidation -> request', request)

        body = {}

        print('signUpValidation -> request', request.data)

        # print('signUpValidation -> data', request.data)
        # print('signUpValidation -> body', request.body)
        # print('signUpValidation -> POST', request.POST)

        # body = body['data']

        schema = {
            'name': {
                'type': 'string',
            }, 
            'age': {
                'type': 'integer', 
                'min': 10,
            },
        }
        # document = {
        #     'name': 'Little Joe', 
        #     'age': 15,
        # }
        # is_valid = Validator(document=body, schema=schema)
        # print('is_valid', is_valid)

        # data = json.dumps(data)
        # print('data', data)
        
        
        # print('request.body', request.body)

        if 1 == 1:
            request.entry = 'entry'
            return function(request, *args, **kwargs)
        else:
            return sendUnprocessableEntity(errors=['bus.getErrors()'])

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
from cerberus import Validator as cerberus_validator

# from rest_framework.decorators import parser_classes
# from rest_framework.parsers import JSONParser

# def validate(document, schema):
#     v = Validator()
#     return v.validate(document, schema)

class Validator():
    is_valid = False
    errors = []

    def __init__(self, *args, **kwargs):
        self.v = cerberus_validator()

        print('Validator -> __init__')

        print('kwargs', kwargs)

        # document = kwargs['document']

        # data = JSONParser().parse(document)

        # print('data', data)

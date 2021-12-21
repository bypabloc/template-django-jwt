from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from ..repository.UserRepository import UserList
from ..helpers.response import sendSuccess, sendCreated, sendUnprocessableEntity, sendInternalServerError

def user_is_entry_author(function):
    def wrap(request, *args, **kwargs):

        print('request', request)
        print('kwargs', kwargs)

        if 1 == 1:
            request.entry = 'entry'
            return function(request, *args, **kwargs)
        else:
            return sendUnprocessableEntity(errors=['bus.getErrors()'])

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

@api_view(['GET'])
@user_is_entry_author
@csrf_exempt
def list(request):

    print('request.entry', request.entry)

    try:
        data = {}
        buses = UserList()
        buses.request = request
        data['buses'] = buses.list()

        return sendSuccess(data=data)
    except Exception as ex:
        return sendInternalServerError(ex=ex)

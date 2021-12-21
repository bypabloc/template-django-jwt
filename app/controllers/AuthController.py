from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt

from ..forms.UserForm import SignUpForm
from ..serializers.UserSerializer import SignUpSerializer

from ..helpers.response import sendSuccess, sendCreated, sendUnprocessableEntity, sendInternalServerError

@api_view(['POST'])
@csrf_exempt
def signUp(request):

    try:
        data = {}

        sign_up_serializer = SignUpSerializer(data=request.data,context={'request': request})

        if sign_up_serializer.is_valid():

            data['user'] = sign_up_serializer.save()

            return sendCreated(data=data)
        else:
            return sendUnprocessableEntity(errors=sign_up_serializer.errors)

    except Exception as ex:
        return sendInternalServerError(ex=ex)

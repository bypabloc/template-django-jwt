from django import forms
from django.db.models import query
from ..models import User, Q, Exists, OuterRef

from .helpers import getErrorsFormatted, modelToJson
from ..helpers.pagination import paginate_queryset
from ..helpers.model_apply_sort import model_apply_sort
from ..helpers.model_apply_filter import model_apply_filter
from ..helpers.model_apply_pagination import model_apply_pagination

from datetime import date

class UserList():
    def list(self):
        return User.objects.all().values()

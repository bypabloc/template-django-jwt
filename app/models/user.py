from ..models import models, RawSQL

from django.dispatch import receiver
from datetime import datetime, timedelta

import uuid
import crypt

PROTECTED_ATTRIBUTES = ['password','last_ip_address']

class UserManager(models.Manager):
    def create(self, **kwargs):

        kwargs['created_at'] = datetime.now()
        kwargs['updated_at'] = datetime.now()
        kwargs['last_login_at'] = datetime.now()
        kwargs['last_ip_address'] = kwargs['last_ip_address'] if 'last_ip_address' in kwargs else ''
        kwargs['state'] = 1

        kwargs['uuid'] = str(uuid.uuid4())
        kwargs['password'] = crypt.crypt( kwargs['password'] )

        data = {}

        fields = self.model._meta.fields
        for field in fields:
            # print('create -> field', field.get_internal_type())
            if field.name != 'id':
                data[field.name] = kwargs[field.name]

        return super().create(**data)

class User(models.Model):

    nickname = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)

    uuid = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=150, blank=True)
    state = models.PositiveSmallIntegerField()

    last_login_at = models.DateTimeField()
    last_ip_address = models.CharField(max_length=20)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    objects = UserManager()

    class Meta:
        # db_table = 'app_user'
        ordering = [
            '-created_at',
        ]

    def toJSON(self, *args, **kwargs):

        data = {}
        for field in self._meta.fields:
            if field.name not in PROTECTED_ATTRIBUTES:
                if field.name != 'id':
                    data[field.name] = getattr(self, field.name)
                else:
                    data['id'] = getattr(self, field.name)
        
        if 'show_hidden_fields' in kwargs:
            if type(kwargs['show_hidden_fields']) is list:
                for field in PROTECTED_ATTRIBUTES:
                    data[field] = getattr(self, field)
        
        return { **data }

    # def __str__(self):
    #     return self.nickname

    # def __repr__(self):
    #     return self.nickname

    # def __unicode__(self):
    #     return self.nickname

    # def save(self, *args, **kwargs):
    #     if not self.uuid:
    #         self.uuid = str(uuid.uuid4())

    #     if not self.created_at:
    #         self.created_at = datetime.now()

    #     self.updated_at = datetime.now()

    #     super(User, self).save(*args, **kwargs)

    # @classmethod
    # def update(cls, **kwargs):
    #     if 'password' in kwargs:
    #         kwargs['password'] = crypt.crypt( kwargs['password'] )
    #     kwargs['updated_at'] = datetime.now()
    #     return cls.objects.update(**kwargs)

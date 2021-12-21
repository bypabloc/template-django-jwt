from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from datetime import datetime, timedelta
import crypt

from ..models import User

class SignUpSerializer(serializers.Serializer):
    # pk = serializers.Field(required=False)

    nickname = serializers.CharField(
        max_length=50,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        max_length=50,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    phone = serializers.CharField(
        max_length=50,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(max_length=50, required=True, write_only = True)
    password_confirmation = serializers.CharField(max_length=50, required=True, write_only = True)

    state = serializers.IntegerField(max_value=5, min_value=1, required=False)

    def validate(self, data):

        errors = {}

        if 'password' in data and 'password_confirmation' in data:
            if data['password'] != data['password_confirmation']:
                errors['password'] = 'The two password fields must match'
                errors['password_confirmation'] = 'The two password fields must match'
        
        if len(errors) != 0:
            raise serializers.ValidationError(errors)
        
        return data

    def create(self, validated_data):
        validated_data['last_ip_address'] = self.context.get('request').META.get('REMOTE_ADDR')

        user = User.objects.create(**validated_data)

        self.validated_data.clear()

        # fields = user._meta.fields
        # for field in fields:
        #     self.validated_data[field.name] = field.value_from_object(user)

        return user.toJSON()

    def update(self, instance, validated_data):
        instance.attributes = validated_data
        return instance

    def restore_object(self, attrs, instance=None):
        
        if instance:
            # Update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.code = attrs.get('code', instance.code)
            instance.linenos = attrs.get('linenos', instance.linenos)
            instance.language = attrs.get('language', instance.language)
            instance.style = attrs.get('style', instance.style)
            return instance

        # Create new instance
        return User(**attrs)

    class Meta:
        model = User
from ..models import models, RawSQL

# class SessionManager(models.Manager):
#     pass

class Session(models.Model):

    token = models.CharField(max_length=150, unique=True)
    user = models.ForeignKey(
        'User', 
        related_name='user', 
        on_delete=models.CASCADE, 
    )
    expired_at = models.DateTimeField()

    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField()

    # objects = SessionManager()

    # class Meta:
    #     db_table = 'app_user'
    #     ordering = [
    #         '-created_at',
    #     ]

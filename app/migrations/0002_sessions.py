from django.db import migrations, models
from ..helpers.date_time_without_tz_field import DateTimeWithoutTZField

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                ('token', models.CharField(max_length=150, unique=True)),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=models.deletion.DO_NOTHING,
                        to='app.user',
                    ),
                ),
                ('expired_at', models.DateTimeField()),

                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
            ],
        ),
    ]

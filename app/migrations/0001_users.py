from django.db import migrations, models
from ..helpers.date_time_without_tz_field import DateTimeWithoutTZField

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),

                ('phone', models.CharField(max_length=50, unique=True)),
                ('uuid', models.CharField(max_length=150, unique=True)),

                ('password', models.CharField(max_length=150)),

                ('state', models.PositiveSmallIntegerField()),

                ('last_login_at', models.DateTimeField()),
                ('last_ip_address', models.CharField(max_length=20)),

                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
            ],
        ),
    ]

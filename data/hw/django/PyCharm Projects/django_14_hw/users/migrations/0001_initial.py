# Generated by Django 4.0.2 on 2022-03-02 04:18

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=60, unique=True, verbose_name='phone-number')),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], verbose_name='Sex')),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(choices=[('STUDENT', 'Student'), ('WORKER', 'Worker'), ('JOBLESS', 'Jobless'), ('RETIRED', 'Retired'), ('FREELANCE', 'Freelance'), ('REMOTE', 'Remote')], max_length=80)),
                ('secret_pass', models.CharField(max_length=60, unique=True, verbose_name='maiden-name')),
                ('education', models.CharField(choices=[('BACHELOR', 'Bachelor'), ('MASTER', 'Master'), ('ENGINEER', 'Engineer')], max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

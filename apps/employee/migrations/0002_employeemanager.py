# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (b'employee', b'0001_initial'),
        (b'contenttypes', b'__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'EmployeeManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'employee', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                (b'manager', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

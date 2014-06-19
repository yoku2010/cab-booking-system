# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (b'contenttypes', b'__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'CabBooking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                (b'booking_type', models.CharField(max_length=10, verbose_name=b'Booking Type')),
                (b'date', models.CharField(max_length=20, verbose_name=b'Date')),
                (b'time', models.CharField(max_length=10, verbose_name=b'Time')),
                (b'start', models.CharField(max_length=32, verbose_name=b'Start')),
                (b'end', models.CharField(max_length=32, verbose_name=b'End')),
                (b'duration', models.CharField(max_length=20, verbose_name=b'Time')),
                (b'reason', models.CharField(max_length=100, verbose_name=b'Reason')),
                (b'status', models.SmallIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

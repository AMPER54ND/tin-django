# Generated by Django 3.0 on 2019-12-25 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate_beer', '0002_auto_20191212_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beer',
            old_name='creator',
            new_name='owner',
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0009_auto_20200222_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='available',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]

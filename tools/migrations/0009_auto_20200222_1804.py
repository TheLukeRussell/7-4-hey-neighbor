# Generated by Django 3.0.3 on 2020-02-22 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0008_tool_borrowed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='borrowed',
            new_name='Are_You_Sure',
        ),
    ]
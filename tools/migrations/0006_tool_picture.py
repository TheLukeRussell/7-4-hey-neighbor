# Generated by Django 3.0.3 on 2020-02-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_auto_20200220_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='picture',
            field=models.ImageField(default=True, upload_to='images/'),
            preserve_default=False,
        ),
    ]
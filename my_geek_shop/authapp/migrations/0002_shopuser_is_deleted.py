# Generated by Django 3.2.5 on 2021-08-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

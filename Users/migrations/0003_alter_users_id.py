# Generated by Django 5.1 on 2024-08-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_remove_users_email_alter_users_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

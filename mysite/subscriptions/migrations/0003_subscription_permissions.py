# Generated by Django 5.0 on 2024-12-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('subscriptions', '0002_subscription_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='permissions',
            field=models.ManyToManyField(to='auth.permission'),
        ),
    ]

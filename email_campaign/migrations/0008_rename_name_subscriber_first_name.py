# Generated by Django 4.2.5 on 2023-09-09 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_campaign', '0007_emailcampaign'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='name',
            new_name='first_name',
        ),
    ]

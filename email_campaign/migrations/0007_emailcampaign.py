# Generated by Django 4.2.5 on 2023-09-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_campaign', '0006_alter_subscriber_status_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('preview_text', models.TextField()),
                ('article_url', models.URLField()),
                ('html_content', models.TextField()),
                ('plain_text_content', models.TextField()),
                ('published_date', models.DateField()),
            ],
        ),
    ]

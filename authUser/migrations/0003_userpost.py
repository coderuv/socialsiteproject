# Generated by Django 3.2 on 2021-04-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authUser', '0002_auto_20210428_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='userpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
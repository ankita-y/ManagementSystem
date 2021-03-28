# Generated by Django 3.1.3 on 2021-03-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserManagementSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('emailId', models.EmailField(max_length=254)),
                ('contactno', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=150)),
                ('confirmpassword', models.CharField(max_length=150)),
            ],
        ),
    ]

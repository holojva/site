# Generated by Django 3.2.8 on 2023-05-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(default='./templates/images/q.gif', null=True, upload_to='./templates/images/')),
                ('status', models.BooleanField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-08 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('editorial', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
            ],
        ),
    ]

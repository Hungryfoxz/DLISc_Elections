# Generated by Django 5.1 on 2024-08-08 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('priority', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Voter Position List',
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('bio', models.TextField(max_length=300)),
                ('votes', models.IntegerField(default=0)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.positions')),
            ],
            options={
                'verbose_name_plural': 'Candidate List',
            },
        ),
        migrations.CreateModel(
            name='Voted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=60)),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.register')),
            ],
            options={
                'verbose_name_plural': 'Voted Student List',
            },
        ),
    ]

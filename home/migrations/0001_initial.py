# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 17:02
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_id', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('winner', models.CharField(default='0', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.BigIntegerField()),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=100)),
                ('wins', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool_number', models.IntegerField(default=1)),
                ('number_of_teams', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SportsSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_players', models.PositiveIntegerField()),
                ('sport', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matches_per_day', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('number_of_team', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(50)])),
                ('number_of_pool', models.IntegerField(default=1)),
                ('type', models.IntegerField()),
                ('available_days', models.IntegerField()),
                ('registration_ending', models.DateField()),
                ('starting_date', models.DateField()),
                ('sport', models.CharField(max_length=30)),
                ('category', models.CharField(default='Open to all', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserWrapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=40)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='login',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserWrapper'),
        ),
        migrations.AddField(
            model_name='team',
            name='login',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.UserWrapper'),
        ),
        migrations.AddField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.Tournament'),
        ),
        migrations.AddField(
            model_name='pool',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Tournament'),
        ),
        migrations.AddField(
            model_name='point',
            name='pool',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Pool'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='pool',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Pool'),
        ),
        migrations.AddField(
            model_name='googleuser',
            name='user_wrapper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserWrapper'),
        ),
    ]

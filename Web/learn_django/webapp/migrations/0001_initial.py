# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-10 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', null=True)),
                ('imdbid', models.BigIntegerField(blank=True, db_column='imdbId', null=True)),
                ('tmdbid', models.FloatField(blank=True, db_column='tmdbId', null=True)),
            ],
            options={
                'db_table': 'links',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('backdrop', models.TextField(blank=True, null=True)),
                ('movieid', models.TextField(blank=True, db_column='movieId', null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('poster', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('video', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('year', models.TextField(blank=True, null=True)),
                ('action', models.BigIntegerField(blank=True, db_column='Action', null=True)),
                ('adventure', models.BigIntegerField(blank=True, db_column='Adventure', null=True)),
                ('animation', models.BigIntegerField(blank=True, db_column='Animation', null=True)),
                ('children', models.BigIntegerField(blank=True, db_column='Children', null=True)),
                ('comedy', models.BigIntegerField(blank=True, db_column='Comedy', null=True)),
                ('crime', models.BigIntegerField(blank=True, db_column='Crime', null=True)),
                ('documentary', models.BigIntegerField(blank=True, db_column='Documentary', null=True)),
                ('drama', models.BigIntegerField(blank=True, db_column='Drama', null=True)),
                ('fantasy', models.BigIntegerField(blank=True, db_column='Fantasy', null=True)),
                ('film_noir', models.BigIntegerField(blank=True, db_column='Film_Noir', null=True)),
                ('horror', models.BigIntegerField(blank=True, db_column='Horror', null=True)),
                ('musical', models.BigIntegerField(blank=True, db_column='Musical', null=True)),
                ('mystery', models.BigIntegerField(blank=True, db_column='Mystery', null=True)),
                ('romance', models.BigIntegerField(blank=True, db_column='Romance', null=True)),
                ('sci_fi', models.BigIntegerField(blank=True, db_column='Sci_Fi', null=True)),
                ('thriller', models.BigIntegerField(blank=True, db_column='Thriller', null=True)),
                ('war', models.BigIntegerField(blank=True, db_column='War', null=True)),
                ('western', models.BigIntegerField(blank=True, db_column='Western', null=True)),
                ('unknown', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MoviesMapped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', null=True)),
                ('original_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movies_mapped',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NormalisedContentbasedfilteringData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('action', models.BigIntegerField(blank=True, db_column='Action', null=True)),
                ('adventure', models.BigIntegerField(blank=True, db_column='Adventure', null=True)),
                ('animation', models.BigIntegerField(blank=True, db_column='Animation', null=True)),
                ('children', models.BigIntegerField(blank=True, db_column='Children', null=True)),
                ('comedy', models.BigIntegerField(blank=True, db_column='Comedy', null=True)),
                ('crime', models.BigIntegerField(blank=True, db_column='Crime', null=True)),
                ('documentary', models.BigIntegerField(blank=True, db_column='Documentary', null=True)),
                ('drama', models.BigIntegerField(blank=True, db_column='Drama', null=True)),
                ('fantasy', models.BigIntegerField(blank=True, db_column='Fantasy', null=True)),
                ('film_noir', models.BigIntegerField(blank=True, db_column='Film_Noir', null=True)),
                ('horror', models.BigIntegerField(blank=True, db_column='Horror', null=True)),
                ('musical', models.BigIntegerField(blank=True, db_column='Musical', null=True)),
                ('mystery', models.BigIntegerField(blank=True, db_column='Mystery', null=True)),
                ('romance', models.BigIntegerField(blank=True, db_column='Romance', null=True)),
                ('sci_fi', models.BigIntegerField(blank=True, db_column='Sci_Fi', null=True)),
                ('thriller', models.BigIntegerField(blank=True, db_column='Thriller', null=True)),
                ('war', models.BigIntegerField(blank=True, db_column='War', null=True)),
                ('western', models.BigIntegerField(blank=True, db_column='Western', null=True)),
                ('unknown', models.BigIntegerField(blank=True, null=True)),
                ('normalised_key', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Normalised_ContentBasedFiltering_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NormalisedContentbasedfilteringMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('normalised_key', models.BigIntegerField(blank=True, null=True)),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', null=True)),
            ],
            options={
                'db_table': 'Normalised_ContentBasedFiltering_map',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NormalisedContentbasedfilteringSimilarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('number_0', models.BigIntegerField(blank=True, db_column='0', null=True)),
                ('number_1', models.BigIntegerField(blank=True, db_column='1', null=True)),
                ('number_2', models.BigIntegerField(blank=True, db_column='2', null=True)),
                ('number_3', models.BigIntegerField(blank=True, db_column='3', null=True)),
                ('number_4', models.BigIntegerField(blank=True, db_column='4', null=True)),
                ('number_5', models.BigIntegerField(blank=True, db_column='5', null=True)),
                ('number_6', models.BigIntegerField(blank=True, db_column='6', null=True)),
                ('number_7', models.BigIntegerField(blank=True, db_column='7', null=True)),
                ('number_8', models.BigIntegerField(blank=True, db_column='8', null=True)),
                ('number_9', models.BigIntegerField(blank=True, db_column='9', null=True)),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', null=True)),
            ],
            options={
                'db_table': 'Normalised_ContentBasedFiltering_similarity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('userid', models.BigIntegerField(blank=True, db_column='userId', null=True)),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', null=True)),
                ('rating', models.BigIntegerField(blank=True, null=True)),
                ('timestamp', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ratings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SimpleCollaborativefilteringItemRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('number_0', models.BigIntegerField(blank=True, db_column='0', null=True)),
                ('number_1', models.BigIntegerField(blank=True, db_column='1', null=True)),
                ('number_2', models.BigIntegerField(blank=True, db_column='2', null=True)),
                ('number_3', models.BigIntegerField(blank=True, db_column='3', null=True)),
                ('number_4', models.BigIntegerField(blank=True, db_column='4', null=True)),
                ('number_5', models.BigIntegerField(blank=True, db_column='5', null=True)),
                ('number_6', models.BigIntegerField(blank=True, db_column='6', null=True)),
                ('number_7', models.BigIntegerField(blank=True, db_column='7', null=True)),
                ('number_8', models.BigIntegerField(blank=True, db_column='8', null=True)),
                ('number_9', models.BigIntegerField(blank=True, db_column='9', null=True)),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', null=True)),
            ],
            options={
                'db_table': 'Simple_CollaborativeFiltering_item_recommendation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SimpleCollaborativefilteringSimilarUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('number_0', models.BigIntegerField(blank=True, db_column='0', null=True)),
                ('number_1', models.BigIntegerField(blank=True, db_column='1', null=True)),
                ('number_2', models.BigIntegerField(blank=True, db_column='2', null=True)),
                ('number_3', models.BigIntegerField(blank=True, db_column='3', null=True)),
                ('number_4', models.BigIntegerField(blank=True, db_column='4', null=True)),
                ('number_5', models.BigIntegerField(blank=True, db_column='5', null=True)),
                ('number_6', models.BigIntegerField(blank=True, db_column='6', null=True)),
                ('number_7', models.BigIntegerField(blank=True, db_column='7', null=True)),
                ('number_8', models.BigIntegerField(blank=True, db_column='8', null=True)),
                ('number_9', models.BigIntegerField(blank=True, db_column='9', null=True)),
                ('userid', models.BigIntegerField(blank=True, db_column='userId', null=True)),
            ],
            options={
                'db_table': 'Simple_CollaborativeFiltering_similar_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SimpleCollaborativefilteringUserRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('number_0', models.BigIntegerField(blank=True, db_column='0', null=True)),
                ('number_1', models.BigIntegerField(blank=True, db_column='1', null=True)),
                ('number_2', models.BigIntegerField(blank=True, db_column='2', null=True)),
                ('number_3', models.BigIntegerField(blank=True, db_column='3', null=True)),
                ('number_4', models.BigIntegerField(blank=True, db_column='4', null=True)),
                ('number_5', models.BigIntegerField(blank=True, db_column='5', null=True)),
                ('number_6', models.BigIntegerField(blank=True, db_column='6', null=True)),
                ('number_7', models.BigIntegerField(blank=True, db_column='7', null=True)),
                ('number_8', models.BigIntegerField(blank=True, db_column='8', null=True)),
                ('userid', models.BigIntegerField(blank=True, db_column='userId', null=True)),
            ],
            options={
                'db_table': 'Simple_CollaborativeFiltering_user_recommendation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SimpleContentbasedfiltering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('number_0', models.BigIntegerField(blank=True, db_column='0', null=True)),
                ('number_1', models.BigIntegerField(blank=True, db_column='1', null=True)),
                ('number_2', models.BigIntegerField(blank=True, db_column='2', null=True)),
                ('number_3', models.BigIntegerField(blank=True, db_column='3', null=True)),
                ('number_4', models.BigIntegerField(blank=True, db_column='4', null=True)),
                ('number_5', models.BigIntegerField(blank=True, db_column='5', null=True)),
                ('number_6', models.BigIntegerField(blank=True, db_column='6', null=True)),
                ('number_7', models.BigIntegerField(blank=True, db_column='7', null=True)),
                ('number_8', models.BigIntegerField(blank=True, db_column='8', null=True)),
                ('number_9', models.BigIntegerField(blank=True, db_column='9', null=True)),
                ('movieid', models.BigIntegerField(blank=True, db_column='movieId', null=True)),
            ],
            options={
                'db_table': 'Simple_ContentBasedFiltering',
                'managed': False,
            },
        ),
    ]

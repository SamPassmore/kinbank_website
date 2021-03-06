# Generated by Django 3.0.5 on 2020-04-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.TextField(blank=True, db_column='ID', primary_key=True, serialize=False)),
                ('local_id', models.IntegerField(blank=True, db_column='Local_ID', null=True)),
                ('language_id', models.TextField(blank=True, db_column='Language_ID', null=True)),
                ('parameter_id', models.TextField(blank=True, db_column='Parameter_ID', null=True)),
                ('value', models.TextField(blank=True, db_column='Value', null=True)),
                ('form', models.TextField(blank=True, db_column='Form', null=True)),
                ('segments', models.IntegerField(blank=True, db_column='Segments', null=True)),
                ('comment', models.TextField(blank=True, db_column='Comment', null=True)),
                ('source', models.TextField(blank=True, db_column='Source', null=True)),
                ('cognacy', models.IntegerField(blank=True, db_column='Cognacy', null=True)),
                ('loan', models.IntegerField(blank=True, db_column='Loan', null=True)),
            ],
            options={
                'db_table': 'forms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.TextField(blank=True, db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('glottocode', models.TextField(blank=True, db_column='Glottocode', null=True)),
                ('glottolog_name', models.TextField(blank=True, db_column='Glottolog_Name', null=True)),
                ('iso639p3code', models.TextField(blank=True, db_column='ISO639P3code', null=True)),
                ('macroarea', models.TextField(blank=True, db_column='Macroarea', null=True)),
                ('latitude', models.FloatField(blank=True, db_column='Latitude', null=True)),
                ('longitude', models.FloatField(blank=True, db_column='Longitude', null=True)),
                ('family', models.TextField(blank=True, db_column='Family', null=True)),
                ('label', models.TextField(blank=True, db_column='Label', null=True)),
                ('project', models.TextField(blank=True, db_column='Project', null=True)),
                ('projectfile', models.TextField(blank=True, db_column='ProjectFile', null=True)),
                ('projectname', models.IntegerField(blank=True, db_column='ProjectName', null=True)),
                ('entrydate', models.TextField(blank=True, db_column='EntryDate', null=True)),
                ('comment', models.TextField(blank=True, db_column='Comment', null=True)),
                ('link', models.TextField(blank=True, db_column='Link', null=True)),
            ],
            options={
                'db_table': 'languages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.TextField(blank=True, db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('concepticon_id', models.IntegerField(blank=True, db_column='Concepticon_ID', null=True)),
                ('concepticon_gloss', models.TextField(blank=True, db_column='Concepticon_Gloss', null=True)),
                ('parameter', models.TextField(blank=True, db_column='Parameter', null=True)),
                ('group', models.TextField(blank=True, db_column='Group', null=True)),
                ('dataset', models.TextField(blank=True, db_column='Dataset', null=True)),
            ],
            options={
                'db_table': 'parameters',
                'managed': False,
            },
        ),
    ]

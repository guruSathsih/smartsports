# Generated by Django 2.1.7 on 2019-03-28 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
            options={
                'db_table': 'series',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('series_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smartsport.Series')),
            ],
            options={
                'db_table': 'tournament',
            },
        ),
    ]

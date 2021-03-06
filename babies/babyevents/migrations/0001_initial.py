# Generated by Django 3.0.4 on 2020-04-25 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('bid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('pid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('etype', models.CharField(max_length=80)),
                ('time', models.TimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=500)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babyevents.Baby')),
            ],
        ),
        migrations.AddField(
            model_name='baby',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='babyevents.Parent'),
        ),
    ]

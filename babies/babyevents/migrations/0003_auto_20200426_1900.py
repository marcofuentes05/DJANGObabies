# Generated by Django 3.0.4 on 2020-04-26 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyevents', '0002_remove_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='bid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='eid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='parent',
            name='pid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

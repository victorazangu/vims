# Generated by Django 4.1.7 on 2023-03-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('program_name', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('contacts', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('venue', models.CharField(max_length=255)),
                ('starts', models.DateField()),
                ('ends', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]

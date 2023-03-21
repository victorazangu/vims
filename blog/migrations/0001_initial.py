# Generated by Django 4.1.7 on 2023-03-21 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=5000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
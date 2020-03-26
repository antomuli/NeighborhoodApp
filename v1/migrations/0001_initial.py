# Generated by Django 3.0.4 on 2020-03-26 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('hood_name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('occupants', models.IntegerField(default=0)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('assignee', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gravatar', models.URLField(default='https://www.gravatar.com/avatar/')),
                ('bio', models.TextField(default='')),
                ('neighborhood', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='v1.Hood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.Hood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('department_name', models.CharField(max_length=32)),
                ('description', models.TextField(default='')),
                ('phone_number', models.CharField(max_length=16)),
                ('is_active', models.BooleanField(default=True)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.Hood')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('business_name', models.CharField(max_length=32)),
                ('description', models.TextField(default='')),
                ('business_email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.Hood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

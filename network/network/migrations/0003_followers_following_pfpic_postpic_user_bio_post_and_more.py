# Generated by Django 4.0.1 on 2022-04-08 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pfpic',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('img', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postpic',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('img', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(max_length=1000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.postpic')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='fllowers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.followers'),
        ),
        migrations.AddField(
            model_name='user',
            name='fllowing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.following'),
        ),
        migrations.AddField(
            model_name='user',
            name='pfp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.pfpic'),
        ),
    ]
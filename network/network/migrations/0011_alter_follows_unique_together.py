# Generated by Django 4.0.1 on 2022-04-23 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_alter_post_poster'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follows',
            unique_together={('following', 'followers')},
        ),
    ]

# Generated by Django 2.2 on 2019-08-29 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190829_0718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='done',
            new_name='completed',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='label',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='username',
        ),
        migrations.AddField(
            model_name='todo',
            name='editing',
            field=models.BooleanField(default=False),
        ),
    ]

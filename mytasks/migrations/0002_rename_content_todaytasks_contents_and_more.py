# Generated by Django 4.0.3 on 2022-04-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todaytasks',
            old_name='content',
            new_name='contents',
        ),
        migrations.AddField(
            model_name='todaytasks',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytasks', '0002_rename_content_todaytasks_contents_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todaytasks',
            old_name='subject',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='todaytasks',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
# Generated by Django 3.1.3 on 2023-06-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0007_question_modify_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_count',
            field=models.IntegerField(default=0),
        ),
    ]
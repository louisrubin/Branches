# Generated by Django 3.2.9 on 2021-12-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20211221_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.CharField(max_length=255),
        ),
    ]
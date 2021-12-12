# Generated by Django 4.0 on 2021-12-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('fecha', models.DateTimeField()),
                ('es_borrador', models.BooleanField()),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
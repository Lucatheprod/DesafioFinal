# Generated by Django 4.1 on 2022-09-16 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppThatBeer', '0008_noticia_fecha_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha_posteo',
            field=models.DateField(),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipnoterapia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hipnoterapia',
            name='subcontenido1',
            field=models.TextField(max_length=150, verbose_name='SubContenido1'),
        ),
        migrations.AlterField(
            model_name='hipnoterapia',
            name='subcontenido2',
            field=models.TextField(max_length=150, verbose_name='SubContenido2'),
        ),
        migrations.AlterField(
            model_name='hipnoterapia',
            name='subcontenido3',
            field=models.TextField(max_length=150, verbose_name='SubContenido3'),
        ),
    ]

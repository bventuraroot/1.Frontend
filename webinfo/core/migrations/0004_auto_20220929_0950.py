# Generated by Django 3.2.15 on 2022-09-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220928_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='contenido',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='peliculas',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='tapas/'),
        ),
    ]

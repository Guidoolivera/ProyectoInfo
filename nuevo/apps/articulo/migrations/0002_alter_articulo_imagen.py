# Generated by Django 4.2.2 on 2023-07-17 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, default='articulo/default_articulo.jpg', null=True, upload_to='articulo'),
        ),
    ]

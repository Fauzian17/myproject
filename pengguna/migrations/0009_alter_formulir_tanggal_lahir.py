# Generated by Django 5.0.6 on 2024-05-31 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0008_alter_formulir_kabupaten_alter_formulir_prodi2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulir',
            name='tanggal_lahir',
            field=models.DateField(default=''),
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0005_formulir_prog3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pendaftar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('umur', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Pendaftaran',
        ),
        migrations.RemoveField(
            model_name='formulir',
            name='prog3',
        ),
        migrations.AlterField(
            model_name='formulir',
            name='jenis_kelamin',
            field=models.CharField(blank=True, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='kecamatan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='kelurahan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='kota',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='nama',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nama Lengkap'),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='nik',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='NIK'),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='no_hp',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Nomor HP'),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='no_hp_ortu',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Nomor HP Orang Tua'),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='prog1',
            field=models.CharField(blank=True, choices=[('IT', 'Information Technology'), ('CS', 'Computer Science'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering')], max_length=2, null=True, verbose_name='Program Studi 1'),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='prog2',
            field=models.CharField(blank=True, choices=[('IT', 'Information Technology'), ('CS', 'Computer Science'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering')], max_length=2, null=True, verbose_name='Program Studi 2'),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='tanggal_lahir',
            field=models.DateField(blank=True, null=True, verbose_name='Tanggal Lahir'),
        ),
        migrations.AlterField(
            model_name='formulir',
            name='tempat_lahir',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tempat Lahir'),
        ),
    ]
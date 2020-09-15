# Generated by Django 3.0.5 on 2020-09-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.BigIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('birthday', models.DateField()),
                ('aadhar', models.BigIntegerField()),
                ('file', models.FileField(upload_to='')),
                ('pan', models.CharField(max_length=15)),
                ('file1', models.FileField(upload_to='')),
                ('account', models.BigIntegerField()),
                ('ifsccode', models.CharField(max_length=20)),
            ],
        ),
    ]

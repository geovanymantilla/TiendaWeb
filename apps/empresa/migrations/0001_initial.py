# Generated by Django 3.1.2 on 2020-10-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('quienessomos', models.CharField(max_length=500, null=True)),
                ('emailcontacto', models.CharField(max_length=50, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('telefonocontacto', models.CharField(max_length=20, null=True)),
                ('facebook', models.CharField(max_length=100, null=True)),
                ('instagram', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'empresa',
            },
        ),
    ]
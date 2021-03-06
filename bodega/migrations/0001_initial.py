# Generated by Django 3.2.9 on 2022-01-19 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bodega',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=70)),
                ('detalle', models.TextField(default='')),
                ('valor', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='bodegaProducto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock', models.IntegerField(default=0)),
                ('idBodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodega.bodega')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodega.producto')),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2023-07-09 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200, null=True)),
                ('marca', models.CharField(max_length=100, null=True)),
                ('cantidad', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rut',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
    ]

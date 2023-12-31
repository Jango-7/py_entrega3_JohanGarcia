# Generated by Django 5.0 on 2023-12-31 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartsMod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artista', models.CharField(max_length=20)),
                ('cancion', models.EmailField(max_length=254)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MultitracksMod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artista', models.CharField(max_length=20)),
                ('cancion', models.EmailField(max_length=254)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProduccionesMod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('pedido', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='BluesArts',
        ),
        migrations.DeleteModel(
            name='JazzArts',
        ),
        migrations.DeleteModel(
            name='RockArts',
        ),
    ]

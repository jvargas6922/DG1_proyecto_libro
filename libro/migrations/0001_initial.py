# Generated by Django 5.1 on 2024-08-13 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
            ],
            options={
                'db_table': 'libros',
                'managed': False,
            },
        ),
    ]

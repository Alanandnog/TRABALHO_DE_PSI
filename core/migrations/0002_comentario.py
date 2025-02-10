# Generated by Django 5.1.6 on 2025-02-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('comentario', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

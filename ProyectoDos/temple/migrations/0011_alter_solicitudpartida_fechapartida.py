# Generated by Django 3.2.8 on 2022-01-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temple', '0010_rename_telefono_usuario_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudpartida',
            name='fechaPartida',
            field=models.DateField(help_text='fecha partida'),
        ),
    ]

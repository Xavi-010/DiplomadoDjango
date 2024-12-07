# Generated by Django 5.1.4 on 2024-12-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas_deportivas', '0005_remove_cancha_precio_hora_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='tipo_superficie',
            field=models.CharField(choices=[('Césped Natural', 'Césped Natural'), ('Césped Artificial', 'Césped Artificial'), ('Concreto', 'Concreto'), ('Arena', 'Arena')], max_length=50),
        ),
    ]
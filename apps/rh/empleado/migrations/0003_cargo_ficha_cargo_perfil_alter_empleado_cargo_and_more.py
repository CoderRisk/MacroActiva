# Generated by Django 5.0.2 on 2024-03-01 15:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0002_empleado_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='ficha',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cargo',
            name='perfil',
            field=models.CharField(default=1, max_length=3000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empleado',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.cargo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

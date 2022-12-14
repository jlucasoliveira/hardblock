# Generated by Django 4.1 on 2022-10-08 18:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0004_counter_is_constrained_by_queue'),
        ('attendant', '0002_alter_priority_id_alter_priority_units_ticket_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('DELETED', 'Removido'), ('DEACTIVATED', 'Desativado'), ('ACTIVATED', 'Ativado')], default='ACTIVATED', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='data de atualização')),
                ('counter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.counter', verbose_name='guichê')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendant.priority', verbose_name='prioridade')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.unit', verbose_name='unidade')),
            ],
            options={
                'verbose_name': 'fila',
            },
        ),
    ]

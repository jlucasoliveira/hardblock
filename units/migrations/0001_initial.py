# Generated by Django 4.1 on 2022-08-20 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('DELETED', 'Removido'), ('DEACTIVATED', 'Desativado'), ('ACTIVATED', 'Ativado')], default='ACTIVATED', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='data de atualização')),
                ('street', models.CharField(max_length=150, verbose_name='endereço')),
                ('number', models.CharField(max_length=20, verbose_name='número')),
                ('street_2', models.CharField(blank=True, max_length=150, verbose_name='complemento')),
                ('district', models.CharField(max_length=100, verbose_name='bairro')),
                ('city', models.CharField(max_length=150, verbose_name='cidade')),
                ('state', models.CharField(max_length=5, verbose_name='estado')),
                ('zip_code', models.CharField(max_length=15, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'endereço',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('DELETED', 'Removido'), ('DEACTIVATED', 'Desativado'), ('ACTIVATED', 'Ativado')], default='ACTIVATED', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='data de atualização')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='descrição')),
                ('phone_number', models.CharField(max_length=20, verbose_name='telefone')),
                ('integration_code', models.CharField(max_length=20, verbose_name='código de integração')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.address', verbose_name='endereço')),
            ],
            options={
                'verbose_name': 'unidade',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('DELETED', 'Removido'), ('DEACTIVATED', 'Desativado'), ('ACTIVATED', 'Ativado')], default='ACTIVATED', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='data de atualização')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.TextField(blank=True, verbose_name='descrição')),
                ('busy', models.BooleanField(default=True, verbose_name='ocupado')),
                ('shared', models.BooleanField(default=False, verbose_name='uso compartilhado')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.unit', verbose_name='unidade')),
            ],
            options={
                'verbose_name': 'ambiente',
            },
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('DELETED', 'Removido'), ('DEACTIVATED', 'Desativado'), ('ACTIVATED', 'Ativado')], default='ACTIVATED', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='data de atualização')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='descrição')),
                ('attendance_amount', models.PositiveSmallIntegerField(verbose_name='quantidade de atendimento')),
                ('shared', models.BooleanField(default=False, verbose_name='uso compartilhado')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.unit', verbose_name='unidade')),
            ],
            options={
                'verbose_name': 'guichê',
            },
        ),
    ]

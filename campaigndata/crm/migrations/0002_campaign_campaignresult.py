# Generated by Django 5.1.4 on 2024-12-15 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Inbound', 'Inbound'), ('Outbound', 'Outbound')], max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('Running', 'Running'), ('Paused', 'Paused'), ('Completed', 'Completed')], max_length=50)),
                ('agents', models.ManyToManyField(related_name='campaigns', to='crm.agent')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('cost', models.FloatField()),
                ('outcome', models.CharField(max_length=100)),
                ('call_duration', models.FloatField()),
                ('recording', models.URLField(blank=True, null=True)),
                ('summary', models.TextField()),
                ('transcription', models.TextField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='crm.campaign')),
            ],
        ),
    ]

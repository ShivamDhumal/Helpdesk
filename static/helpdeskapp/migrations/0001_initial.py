# Generated by Django 4.0.3 on 2023-04-04 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('contact_number', models.PositiveIntegerField(blank=True, null=True)),
                ('ticketType', models.CharField(max_length=100)),
                ('ticketSubType', models.CharField(max_length=100)),
                ('attachment', models.FileField(upload_to='files')),
                ('priority', models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], default='low', max_length=100, null=True)),
                ('department', models.CharField(blank=True, choices=[('HR', 'HR'), ('Admin', 'Admin'), ('Tech', 'Tech'), ('Devops', 'Devops'), ('AI', 'AI')], max_length=100, null=True)),
                ('status', models.CharField(blank=True, choices=[('open', 'open'), ('closed', 'closed'), ('working', 'working'), ('hold', 'hold'), ('resolve', 'resolve')], default='open', max_length=10, null=True)),
                ('assign_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_tickets', to=settings.AUTH_USER_MODEL)),
                ('raised_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tickets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicketHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('open', 'open'), ('closed', 'closed'), ('working', 'working'), ('hold', 'hold'), ('resolve', 'resolve')], max_length=10, null=True)),
                ('assigned_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('time_to_resolve', models.DurationField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets_assigned_by', to=settings.AUTH_USER_MODEL)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tickets_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='helpdeskapp.ticket')),
            ],
        ),
    ]
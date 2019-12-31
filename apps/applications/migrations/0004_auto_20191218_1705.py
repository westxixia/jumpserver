# Generated by Django 2.1.11 on 2019-12-18 09:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20191210_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseApp',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('type', models.CharField(choices=[('mysql', 'MySQL')], default='mysql', max_length=128, verbose_name='Type')),
                ('host', models.CharField(db_index=True, max_length=128, verbose_name='Host')),
                ('port', models.IntegerField(default=3306, verbose_name='Port')),
                ('database', models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='Database')),
                ('comment', models.TextField(blank=True, default='', max_length=128, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'DatabaseApp',
                'ordering': ('name',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='databaseapp',
            unique_together={('org_id', 'name')},
        ),
    ]
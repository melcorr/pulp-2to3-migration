# Generated by Django 2.2.9 on 2020-01-30 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pulp_2to3_migration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pulp2repository',
            name='pulp3_repository_version',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.RepositoryVersion'),
        ),
    ]
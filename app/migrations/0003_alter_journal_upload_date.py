# Generated by Django 4.1.5 on 2023-01-14 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_journal_upload_date_alter_journal_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='upload_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

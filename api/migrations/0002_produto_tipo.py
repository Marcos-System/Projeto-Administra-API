# Generated by Django 5.1.1 on 2024-09-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-30 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Framework', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frameworkmodel',
            options={'ordering': ['id'], 'verbose_name': 'Фреймворк', 'verbose_name_plural': 'Фреймворки'},
        ),
    ]

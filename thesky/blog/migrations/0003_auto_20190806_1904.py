# Generated by Django 2.2.3 on 2019-08-06 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190806_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_date',)},
        ),
    ]

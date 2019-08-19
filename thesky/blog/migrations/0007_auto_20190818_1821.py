# Generated by Django 2.2.3 on 2019-08-18 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190818_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.POST'),
        ),
        migrations.AlterField(
            model_name='project',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to='cover'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sample',
            field=models.FileField(blank=True, null=True, upload_to='chapters'),
        ),
    ]

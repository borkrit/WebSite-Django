# Generated by Django 3.1.5 on 2021-01-21 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20210121_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.country', verbose_name='Country'),
        ),
    ]

# Generated by Django 3.0 on 2020-01-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attapp', '0014_auto_20200103_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

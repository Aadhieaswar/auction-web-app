# Generated by Django 3.0.7 on 2020-11-02 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20201101_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bid',
            new_name='highest_bid',
        ),
        migrations.AlterField(
            model_name='bid',
            name='added',
            field=models.DateField(auto_now=True),
        ),
    ]

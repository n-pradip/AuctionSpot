# Generated by Django 4.2.6 on 2024-03-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_auction_winner_orderitem_finalorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalorder',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]

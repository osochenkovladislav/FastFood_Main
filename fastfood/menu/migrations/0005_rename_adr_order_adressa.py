# Generated by Django 4.0.4 on 2022-06-03 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_order_adr_alter_order_city_alter_order_state_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adr',
            new_name='adressa',
        ),
    ]

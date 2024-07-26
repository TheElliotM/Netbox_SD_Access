# Generated by Django 5.0.7 on 2024-07-25 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ipam", "0069_gfk_indexes"),
        ("netbox_sd_access", "0009_virtualnetwork"),
    ]

    operations = [
        migrations.AlterField(
            model_name="virtualnetwork",
            name="vrf",
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to="ipam.vrf"),
        ),
    ]

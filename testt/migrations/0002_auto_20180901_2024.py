# Generated by Django 2.0.8 on 2018-09-01 20:24

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('testt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='country',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='continent', on_delete=django.db.models.deletion.CASCADE, to='testt.Country'),
        ),
    ]
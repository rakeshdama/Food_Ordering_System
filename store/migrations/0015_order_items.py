# Generated by Django 3.1.3 on 2021-05-24 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210517_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.item'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-04 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('resource', '0006_auto_20191203_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='monitored',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Account'),
        ),
    ]

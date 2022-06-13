# Generated by Django 4.0.2 on 2022-02-17 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_user_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='planet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.planet'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-14 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0006_rename_leader_name_addproject_leadername'),
    ]

    operations = [
        migrations.CreateModel(
            name='Not',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='header.addleader')),
            ],
        ),
    ]

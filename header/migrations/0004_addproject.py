# Generated by Django 4.1.7 on 2023-03-14 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('header', '0003_addleader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='header.employee')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='header.addleader')),
            ],
        ),
    ]

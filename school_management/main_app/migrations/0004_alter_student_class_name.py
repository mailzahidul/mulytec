# Generated by Django 4.0.2 on 2023-03-09 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.class'),
        ),
    ]
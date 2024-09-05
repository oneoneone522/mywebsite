# Generated by Django 5.1 on 2024-08-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_clientinfo_contact_choice_clientinfo_web_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviece_type', models.CharField(max_length=50)),
                ('content', models.CharField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='clientinfo',
            name='ps',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]

# Generated by Django 2.2 on 2022-10-16 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='insurance_scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policyno', models.CharField(max_length=200, null=True)),
                ('insurancetype', models.CharField(max_length=200, null=True)),
                ('company', models.CharField(max_length=200, null=True)),
                ('policyDescription', models.CharField(max_length=200, null=True)),
                ('timelength', models.CharField(max_length=200, null=True)),
                ('insuranceamount', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]

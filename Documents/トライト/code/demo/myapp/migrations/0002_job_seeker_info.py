# Generated by Django 4.1.2 on 2022-12-19 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JOB_SEEKER_INFO',
            fields=[
                ('SEEKER_ID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('YEARS_OF_EXPERIENCE', models.IntegerField(null=True)),
                ('TYPE_OF_BUSINESS', models.CharField(max_length=2, null=True)),
                ('OCCUPATION', models.CharField(max_length=2, null=True)),
                ('HOLDING_QUALIFICATION', models.CharField(max_length=2, null=True)),
                ('UPD_USERNAME', models.CharField(max_length=20, null=True)),
                ('UPD_DATE', models.DateTimeField(auto_now_add=True)),
                ('UPD_COUNT', models.IntegerField(null=True)),
                ('ADD_USERNAME', models.CharField(max_length=20)),
                ('ADD_DATE', models.DateTimeField(auto_now_add=True)),
                ('ENT_KBN', models.CharField(default=1, max_length=1, null=True)),
                ('SK_ROUTSU_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.routsu_tbl')),
            ],
        ),
    ]

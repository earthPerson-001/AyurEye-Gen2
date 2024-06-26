# Generated by Django 5.0.4 on 2024-05-18 10:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='XRayImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img_file', models.ImageField(upload_to='images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('diagnosing_doctor', models.ForeignKey(limit_choices_to={'user_type': 'Dr'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='doctor_xray_image', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(limit_choices_to={'user_type': 'Pt'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_xray_image', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='XRayPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infection_type', models.CharField(max_length=255)),
                ('bounding_box_coordinates', models.JSONField(max_length=1000)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='predictions', to='inference_api.xrayimage')),
            ],
        ),
    ]

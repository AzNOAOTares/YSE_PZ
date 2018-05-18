# Generated by Django 2.0.4 on 2018-05-18 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('YSE_App', '0020_auto_20180502_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataQuality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dataquality_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dataquality_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='hostphotdata',
            name='dq',
        ),
        migrations.RemoveField(
            model_name='transientphotdata',
            name='dq',
        ),
        migrations.AddField(
            model_name='hostphotdata',
            name='data_quality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='YSE_App.DataQuality'),
        ),
        migrations.AddField(
            model_name='hostspectrum',
            name='data_quality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='YSE_App.DataQuality'),
        ),
        migrations.AddField(
            model_name='transientphotdata',
            name='data_quality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='YSE_App.DataQuality'),
        ),
        migrations.AddField(
            model_name='transientspectrum',
            name='data_quality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='YSE_App.DataQuality'),
        ),
    ]

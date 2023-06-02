# Generated by Django 4.1.7 on 2023-05-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahome', '0002_pjmanage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ibju',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('구분', models.CharField(max_length=20)),
                ('단지명', models.CharField(blank=True, max_length=50, null=True)),
                ('소재지', models.CharField(blank=True, max_length=50, null=True)),
                ('입주시기', models.DateTimeField(blank=True, null=True)),
                ('세대수', models.IntegerField()),
                ('매매시세', models.IntegerField()),
                ('평당분양가', models.IntegerField()),
                ('시공사', models.CharField(max_length=20)),
                ('시도', models.CharField(max_length=20)),
                ('자치구', models.CharField(max_length=20)),
                ('시도자치구', models.CharField(max_length=20)),
                ('기준월', models.DateTimeField(blank=True, null=True)),
                ('년', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='pjmanage',
            name='optcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pjmanage',
            name='pjname',
            field=models.TextField(blank=True, null=True),
        ),
    ]

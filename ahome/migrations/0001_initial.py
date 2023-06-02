# Generated by Django 4.1.7 on 2023-05-16 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('관리번호', models.BigIntegerField(blank=True, null=True)),
                ('모집공고일', models.DateField(blank=True, null=True)),
                ('단지명', models.TextField(blank=True, null=True)),
                ('주택구분', models.TextField(blank=True, null=True)),
                ('민영국민', models.TextField(blank=True, null=True)),
                ('분양구분', models.TextField(blank=True, null=True)),
                ('지역', models.TextField(blank=True, null=True)),
                ('자치구', models.TextField(blank=True, null=True)),
                ('주소지', models.TextField(blank=True, null=True)),
                ('세대수', models.BigIntegerField(blank=True, null=True)),
                ('계약시작일', models.DateField(blank=True, null=True)),
                ('계약종료일', models.DateField(blank=True, null=True)),
                ('건설사', models.TextField(blank=True, null=True)),
                ('시행사', models.TextField(blank=True, null=True)),
                ('입주시기', models.TextField(blank=True, null=True)),
                ('입주년도', models.BigIntegerField(blank=True, null=True)),
                ('모집공고월', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Adetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('관리번호', models.BigIntegerField(blank=True, null=True)),
                ('모집공고일', models.DateField(blank=True, null=True)),
                ('지역', models.TextField(blank=True, null=True)),
                ('단지명', models.TextField(blank=True, null=True)),
                ('세대수', models.BigIntegerField(blank=True, null=True)),
                ('타입', models.TextField(blank=True, null=True)),
                ('공급면적', models.TextField(blank=True, null=True)),
                ('평형', models.BigIntegerField(blank=True, null=True)),
                ('타입세대수', models.BigIntegerField(blank=True, null=True)),
                ('타입최고가', models.TextField(blank=True, null=True)),
                ('공급평당가', models.TextField(blank=True, null=True)),
                ('모집공고월', models.DateField(blank=True, null=True)),
                ('abase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ahome.abase')),
            ],
        ),
    ]

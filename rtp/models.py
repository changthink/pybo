from django.db import models

class Bunyang(models.Model):
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    아파트 = models.TextField(blank=True, null=True)
    전용면적 = models.BigIntegerField(blank=True, null=True)
    거래금액 = models.BigIntegerField(blank=True, null=True)
    층 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    거래유형 = models.TextField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)


class SaleSma(models.Model):
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    아파트 = models.TextField(blank=True, null=True)
    전용면적 = models.FloatField(blank=True, null=True)
    거래금액 = models.BigIntegerField(blank=True, null=True)
    층 = models.TextField(blank=True, null=True)
    건축년도 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    거래유형 = models.TextField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)


class SaleBig6(models.Model):
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    아파트 = models.TextField(blank=True, null=True)
    전용면적 = models.FloatField(blank=True, null=True)
    거래금액 = models.BigIntegerField(blank=True, null=True)
    층 = models.TextField(blank=True, null=True)
    건축년도 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    거래유형 = models.TextField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)


class SaleDodo(models.Model):
    광역시도 = models.TextField(blank=True, null=True)
    시자치구 = models.TextField(blank=True, null=True)
    법정동 = models.TextField(blank=True, null=True)
    아파트 = models.TextField(blank=True, null=True)
    전용면적 = models.FloatField(blank=True, null=True)
    거래금액 = models.BigIntegerField(blank=True, null=True)
    층 = models.TextField(blank=True, null=True)
    건축년도 = models.BigIntegerField(blank=True, null=True)
    년 = models.BigIntegerField(blank=True, null=True)
    월 = models.BigIntegerField(blank=True, null=True)
    전용 = models.BigIntegerField(blank=True, null=True)
    거래유형 = models.TextField(blank=True, null=True)
    기준월 = models.DateField(blank=True, null=True)

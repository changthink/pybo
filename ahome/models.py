# -*- coding: utf-8 -*-


from django.db import models

class Abase(models.Model):
    관리번호 = models.BigIntegerField(blank=True, null=True)
    모집공고일 = models.DateField(blank=True, null=True)
    단지명 = models.TextField(blank=True, null=True)
    주택구분 = models.TextField(blank=True, null=True)
    민영국민 = models.TextField(blank=True, null=True)
    분양구분 = models.TextField(blank=True, null=True)
    지역 = models.TextField(blank=True, null=True)
    자치구 = models.TextField(blank=True, null=True)
    주소지 = models.TextField(blank=True, null=True)
    세대수 = models.BigIntegerField(blank=True, null=True)
    계약시작일 = models.DateField(blank=True, null=True)
    계약종료일 = models.DateField(blank=True, null=True)
    건설사 = models.TextField(blank=True, null=True)
    시행사 = models.TextField(blank=True, null=True)
    입주시기 = models.TextField(blank=True, null=True)
    입주년도 = models.BigIntegerField(blank=True, null=True)
    모집공고월 = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.단지명


class Adetail(models.Model):
    관리번호 = models.BigIntegerField(blank=True, null=True)
    모집공고일 = models.DateField(blank=True, null=True)
    지역 = models.TextField(blank=True, null=True)
    단지명 = models.TextField(blank=True, null=True)
    세대수 = models.BigIntegerField(blank=True, null=True)
    타입 = models.TextField(blank=True, null=True)
    공급면적 = models.TextField(blank=True, null=True)
    평형 = models.BigIntegerField(blank=True, null=True)
    타입세대수 = models.BigIntegerField(blank=True, null=True)
    타입최고가 = models.TextField(blank=True, null=True)
    공급평당가 = models.TextField(blank=True, null=True)
    모집공고월 = models.DateField(blank=True, null=True)
    abase = models.ForeignKey(Abase, on_delete=models.CASCADE)

    # class Meta:
    #     managed = False
    #     db_table = 'applydetail'

    def __str__(self):
        return self.단지명 + self.타입

class Pjmanage(models.Model):
    pjcode = models.CharField(max_length=10)
    optcode = models.CharField(max_length=10,null=True, blank=True)
    pjname = models.TextField(null=True, blank=True)
    end_day = models.DateTimeField(null=True, blank=True)
    come_day = models.DateTimeField(null=True, blank=True)
    dead_day = models.DateTimeField(null=True, blank=True)
    first_rate = models.FloatField()
    finance_rate = models.FloatField()
    end_rate = models.FloatField()
    end_profit = models.IntegerField()
    diff_ing = models.FloatField()
    fund = models.IntegerField()
    pf_remain = models.IntegerField()
    cash_year = models.IntegerField()
    cash_all = models.IntegerField()


class Ibju(models.Model):
    구분 = models.CharField(max_length=20)
    단지명 = models.CharField(max_length=50,null=True, blank=True)
    소재지 = models.CharField(max_length=50, null=True, blank=True)
    입주시기 = models.DateTimeField(null=True, blank=True)
    세대수 = models.IntegerField()
    매매시세 = models.IntegerField()
    평당분양가 = models.IntegerField()
    시공사 = models.CharField(max_length=20)
    시도 = models.CharField(max_length=20)
    자치구 = models.CharField(max_length=20)
    시도자치구 = models.CharField(max_length=20)
    기준월 = models.DateTimeField(null=True, blank=True)
    년 = models.IntegerField()

class Onsale(models.Model):
    시도자치구 = models.CharField(max_length=20)
    시도 = models.CharField(max_length=20, null=True, blank=True)
    자치구 = models.CharField(max_length=20, null=True, blank=True)
    미분양 = models.IntegerField()
    기준월 = models.DateField(null=True, blank=True)


class Pop(models.Model):
    시도자치구 = models.CharField(max_length=20)
    시도 = models.CharField(max_length=20, null=True, blank=True)
    자치구 = models.CharField(max_length=20, null=True, blank=True)
    총인구수 = models.IntegerField()
    세대수 = models.IntegerField()
    기준월 = models.DateField(null=True, blank=True)

class Const(models.Model):
    기준월 = models.DateField(null=True, blank=True)
    지수 = models.IntegerField()

class Pjcode(models.Model):
    구분 = models.CharField(max_length=2, null=True, blank=True)
    코드 = models.CharField(max_length=5, null=True, blank=True)
    내역 = models.CharField(max_length=50, null=True, blank=True)


class Rtech(models.Model):
    시도 = models.CharField(max_length=20, null=True, blank=True)
    자치구 = models.CharField(max_length=20, null=True, blank=True)
    아파트 = models.CharField(max_length=50, null=True, blank=True)
    주소 = models.CharField(max_length=50, null=True, blank=True)
    평당가 = models.IntegerField()
    국평가격 = models.IntegerField()

# class Unit(models.Model):
#     brandname = models.CharField(max_length=50, null=True, blank=True)
#     urls = models.CharField(max_length=50, null=True, blank=True)
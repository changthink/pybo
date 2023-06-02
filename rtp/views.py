from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from rtp.models import Bunyang, SaleSma, SaleBig6, SaleDodo
from django.utils import timezone
from django.db.models import Q
import pandas as pd
import json


def search(request):
    return render(request, 'rtp/search_form.html')

def search_sma(request):
    return render(request, 'rtp/search_form_sma.html')

def search_big6(request):
    return render(request, 'rtp/search_form_big6.html')

def search_dodo(request):
    return render(request, 'rtp/search_form_dodo.html')


def bunyang_data(request):
    시도 = request.POST.get("city")
    if request.POST.get("county") == '전체':
        자치구 = ""
    else:
        자치구 = request.POST.get("county")
    조회시작 = request.POST.get("start")
    조회종료 = request.POST.get("end")
    전용B = request.POST.get("size_begin")
    전용E = request.POST.get("size_end")

    bunyang_list = Bunyang.objects.all()
    bunyang_list = bunyang_list.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월','-거래금액')

    context = {'data': bunyang_list }
    return render(request, 'rtp/bunyang_list.html', context)


def salesma_data(request):
    시도 = request.POST.get("city")
    if request.POST.get("county") == '전체':
        자치구 = ""
    else:
        자치구 = request.POST.get("county")
    조회시작 = request.POST.get("start")
    조회종료 = request.POST.get("end")
    전용B = request.POST.get("size_begin")
    전용E = request.POST.get("size_end")

    salesma_list = SaleSma.objects.all()
    salesma_list = salesma_list.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월','-거래금액')

    context = {'data': salesma_list }
    return render(request, 'rtp/salesma_list.html', context)

def salebig6_data(request):
    시도 = request.POST.get("city")
    if request.POST.get("county") == '전체':
        자치구 = ""
    else:
        자치구 = request.POST.get("county")
    조회시작 = request.POST.get("start")
    조회종료 = request.POST.get("end")
    전용B = request.POST.get("size_begin")
    전용E = request.POST.get("size_end")

    salebig6_list = SaleBig6.objects.all()
    salebig6_list = salebig6_list.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월','-거래금액')

    context = {'data': salebig6_list }
    return render(request, 'rtp/salebig6_list.html', context)


def saledodo_data(request):
    시도 = request.POST.get("city")
    if request.POST.get("county") == '전체':
        자치구 = ""
    else:
        자치구 = request.POST.get("county")
    조회시작 = request.POST.get("start")
    조회종료 = request.POST.get("end")
    전용B = request.POST.get("size_begin")
    전용E = request.POST.get("size_end")

    saledodo_list = SaleDodo.objects.all()
    saledodo_list = saledodo_list.filter(광역시도=시도, 시자치구__contains=자치구, 기준월__gte=조회시작, 기준월__lte=조회종료, 전용__gte=전용B, 전용__lte=전용E).order_by('-기준월','-거래금액')

    context = {'data': saledodo_list }
    return render(request, 'rtp/saledodo_list.html', context)
# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ahome.models import Abase, Adetail, Pjmanage, Ibju, Onsale, Pop, Const, Pjcode, Rtech
from django.utils import timezone
from django.db.models import Q
import pandas as pd
import json


# @login_required(login_url='common:login')
def apply_base(request):
    kw = request.GET.get('kw', '')
    abase = Abase.objects.order_by('-모집공고일')
    if kw:
        abase = abase.filter(
            Q(지역__icontains=kw) |
            Q(건설사__icontains=kw)
        ).distinct()
    context = {'abase': abase, 'kw': kw}
    return render(request, 'ahome/apply_base.html', context)


def apply_detail(request, abase_id):
    abase = Abase.objects.get(id=abase_id)
    details = abase.adetail_set.all()
    context = {
        'abase': abase,
        'details': details
    }
    return render(request, 'ahome/apply_detail.html', context)

def pj_list(request):
    lists = Pjmanage.objects.all()
    context = { 'pjlist' : lists }
    return render(request, 'ahome/pj_manage.html', context)

def ibju_data(request):
    kw = request.GET.get('kw', '')
    ibju_list = Ibju.objects.order_by('입주시기').filter(입주시기__gte='2023-03-31').values
    if kw:
        ibju_list = ibju_list.filter(
            Q(구분__icontains=kw) |
            Q(시도__icontains=kw) |
            Q(자치구__icontains=kw) |
            Q(시공사__icontains=kw)
        ).distinct()
    context = { 'ibju_list' : ibju_list, 'kw': kw }

    return render(request, 'ahome/ibju_list.html', context)

def onsale_data(request):
    kw = request.GET.get('kw', '')
    onsale_list = Onsale.objects.order_by('-미분양')
    if kw:
        onsale_list = onsale_list.filter(
            Q(시도__icontains=kw) |
            Q(자치구__icontains=kw)
        ).distinct()
    context = { 'onsale_list' : onsale_list, 'kw': kw }

    return render(request, 'ahome/onsale_list.html', context)

def pop_data(request):
    kw = request.GET.get('kw', '')
    pop_list = Pop.objects.order_by('-총인구수')
    if kw:
        pop_list = pop_list.filter(
            Q(시도__icontains=kw) |
            Q(자치구__icontains=kw)
        ).distinct()
    context = { 'pop_list' : pop_list, 'kw': kw }

    return render(request, 'ahome/pop_list.html', context)

def const_data(request):
    kw = request.GET.get('kw', '')
    const_list = Const.objects.order_by('-지수')
    if kw:
        const_list = const_list.filter(
            Q(기준월__icontains=kw)
        ).distinct()
    context = { 'const_list' : const_list, 'kw': kw }

    return render(request, 'ahome/const_list.html', context)

def pjcode_data(request):
    kw = request.GET.get('kw', '')
    pjcode_list = Pjcode.objects.all()
    if kw:
        pjcode_list = pjcode_list.filter(
            Q(내역__icontains=kw)
        ).distinct()
    context = { 'pjcode_list' : pjcode_list, 'kw': kw }

    return render(request, 'ahome/pjcode_list.html', context)


def rtech_data(request):
    kw = request.GET.get('kw', '')
    rtech_list = Rtech.objects.all()
    if kw:
        rtech_list = rtech_list.filter(
            Q(시도__icontains=kw)|
            Q(자치구__icontains=kw)
        ).distinct()
    context = { 'rtech_list' : rtech_list, 'kw': kw }

    return render(request, 'ahome/rtech_list.html', context)


def img_data(request):
    return render(request, 'ahome/divcard_card.html')


def table_data(request):
    df = pd.read_csv('static/csv/실거래가격지수.csv', sep='\t')
    df = df.sort_values(by=['구분'], ascending=False)
    json_data = df.to_json(orient='records')
    data=[]
    data=json.loads(json_data)
    context = { 'data' : data }
    return render(request, 'ahome/table_list.html', context)

def tbL_kb50(request):
    df = pd.read_csv('static/csv/선도50지수_2305.csv', sep='\t')
    df = df.sort_values(by=['년월'], ascending=False)
    json_data = df.to_json(orient='records')
    data=[]
    data=json.loads(json_data)
    context = { 'data' : data }
    return render(request, 'ahome/tbl_kb50.html', context)


def tbl_pir(request):
    df = pd.read_csv('static/csv/pir_2303.csv', sep='\t')
    json_data = df.to_json(orient='records')
    data=[]
    data=json.loads(json_data)
    context = { 'data' : data }
    return render(request, 'ahome/tbl_pir.html', context)

def tbl_floorarea(request):
    df = pd.read_csv('static/csv/용적률.csv', sep='\t')
    json_data = df.to_json(orient='records')
    data=[]
    data=json.loads(json_data)
    context = { 'data' : data }
    return render(request, 'ahome/tbl_floorarea.html', context)

def rtp_bunyang(request):
    df = pd.read_csv('k:/django/pj_pybo/static/csv/bunyang.csv', sep=';')
    df = df.sort_values(by='기준월', ascending=False)
    json_data = df.to_json(orient='records')
    data = []
    data = json.loads(json_data)
    context = {'data': data[:500]}
    return render(request, 'ahome/rtp_bunyang.html', context)


def tbl_allpj(request):
    df = pd.read_csv('static/csv/all_pj.csv', sep='\t')
    json_data = df.to_json(orient='records')
    data=[]
    data=json.loads(json_data)
    context = { 'data' : data }
    return render(request, 'ahome/tbl_allpj.html', context)
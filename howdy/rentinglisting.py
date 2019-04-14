# -*- coding: utf-8 -*-
import MySQLdb
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging
logger = logging.getLogger(__name__)


conn = MySQLdb.connect(host='localhost',
                       user='fxreal',
                       password='abcd0123',
                       db='fangxiongreal',
                       charset='utf8mb4')

cursor = conn.cursor()

def get_article(request):

    cursor.execute("select id, url, ask_title from mitbbs_car where 1")

    col_names = ['id', 'url', 'ask_title']
    result = []
    articles_list = cursor.fetchmany(50)
    for row in articles_list:
        row_dict = dict(zip(col_names, row))
        result.append(row_dict)
    context = {'articles': result}
    return render(request, 'articlelist.html', context)
    # cursor.close()
    # conn.close()
def rentingrooms(request):

    cursor.execute("SELECT id, url, ask_title FROM mitbbs_car WHERE ask_title NOT LIKE '[]' ")

    col_names = ['id', 'url', 'ask_title']
    result = []
    articles_list = cursor.fetchmany(20)
    for row in articles_list:
        row_dict = dict(zip(col_names, row))
        result.append(row_dict)
    context = {'articles': result}
    return render(request, 'rentingrooms.html', context)

def newhomes(request):

    cursor.execute("SELECT id, url, ask_title FROM mitbbs_car WHERE ask_title NOT LIKE '[]' ")

    col_names = ['id', 'url', 'ask_title']
    result = []
    articles_list = cursor.fetchmany(20)
    for row in articles_list:
        row_dict = dict(zip(col_names, row))
        result.append(row_dict)
    context = {'articles': result}
    return render(request, 'newhomes.html', context)

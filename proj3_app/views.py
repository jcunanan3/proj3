import json
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
import requests
from proj3_app.models import Report


def home(request):
    # data = Report.objects.values('date', 'category').annotate(total=Count('incident')).order_by('-date','category')
    # return render_to_response("home.html", {'data': data})

    return render(request, 'home.html')


def crimeinfo(request):
    assault_date=[]
    assault_total=[]
    data = Report.objects.filter(category='ASSAULT').values('date', 'category').annotate(total=Count('incident')).order_by('-date','category')

    for i in data:
        assault_date.append(i['date'].strftime('%m/%d/%Y'))
        assault_total.append(i['total'])
    print(assault_date,assault_total)
        # print (i['date'],i['total'])


    return HttpResponse(json.dumps(assault_date), content_type='application/json')

def test(request):
    return render(request, 'test.html')

def test2(request):
    return render(request, 'test2.html')

def crime_date(request):
    assault_date=[]
    data = Report.objects.filter(category='ASSAULT').values('date', 'category').annotate(total=Count('incident')).order_by('date','category')

    for i in data:
        assault_date.append(i['date'].strftime('%m/%d/%Y'))
    print(assault_date)
    return HttpResponse(json.dumps(assault_date), content_type='application/json')

def assault_count(request):
    assault=[]
    data = Report.objects.filter(category='ASSAULT').values('date', 'category').annotate(total=Count('incident')).order_by('date','category')

    for i in data:
        assault.append(i['total'])
    print(assault)
    return HttpResponse(json.dumps(assault), content_type='application/json')

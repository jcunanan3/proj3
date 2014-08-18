import json
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
import requests
from proj3_app.models import Report


def home(request):
    data = Report.objects.values('date', 'category').annotate(total=Count('incident')).order_by('-date','category')
    return render_to_response("home.html", {'data': data})


def crimeinfo(request):
    
    data = Report.objects.values('date', 'category').annotate(total=Count('incident')).order_by('-date','category')


    return HttpResponse(json.dumps(data), content_type='application/json')


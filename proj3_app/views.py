import json
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
# from helper import cat_regression

# Create your views here.
import numpy
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
    return HttpResponse(json.dumps(assault_date), content_type='application/json')


def test(request):
    return render(request, 'test.html')


def test2(request):
    return render(request, 'test2.html')


def test3(request):
    return render(request, 'test3.html')


def crime_date(request):
    assault_date = []
    data = Report.objects.filter(category='ASSAULT').values('date', 'category').annotate(total=Count('incident')).order_by('date','category')

    for i in data:

        assault_date.append(i['date'].strftime('%m/%d/%Y'))
    print(assault_date)
    return HttpResponse(json.dumps(assault_date), content_type='application/json')


def category_count(request, cat):
    cat_array = []
    if cat == 'theft':
        # The forward slash requires special management since it causes the URL append to fail.
        cat = 'LARCENY/THEFT'
    if cat == 'drugs':
        # The forward slash requires special management since it causes the URL append to fail.
        cat = 'DRUG/NARCOTIC'
    if cat == 'gta':
        # The space requires special management since it causes the URL append to fail.
        cat = 'VEHICLE THEFT'
    data = Report.objects.filter(category=cat).values('date', 'category').annotate(total=Count('incident')).order_by('date','category')

    for i in data:
        cat_array.append(i['total'])
    print('category count', cat, cat_array)
    return HttpResponse(json.dumps(cat_array), content_type='application/json')


def cat_regression(request, cat):
    from numpy import arange
    from scipy import stats
    import numpy
    if cat == 'theft':
        # The forward slash requires special management since it causes the URL append to fail.
        cat = 'LARCENY/THEFT'
    if cat == 'drugs':
        # The forward slash requires special management since it causes the URL append to fail.
        cat = 'DRUG/NARCOTIC'
    if cat == 'gta':
        # The space requires special management since it causes the URL append to fail.
        cat = 'VEHICLE THEFT'
    data = Report.objects.filter(category=cat).values('date', 'category').annotate(total=Count('incident')).order_by('date','category')
    crime = []
    for i in data:
        crime.append(i['total'])
    old = numpy.array([])
    np_assault = numpy.append(old, crime)
    l = len(crime)
    xi = arange(0, l)
    # a = array([xi,ones(l)])
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi, np_assault)
    print 'r value', r_value
    print 'p_value', p_value
    print 'standard deviation', std_err
    print 'slope ',slope
    print 'intercept ',intercept
    data = {}
    data['slope']=slope
    data['intercept']=intercept
    data['r_value']=r_value
    data['p_value']=p_value
    data['std_err']=std_err

    regression_array = []

    for x in range(0, l):
        y = slope*x+intercept
        regression_array.append(y)

    print regression_array
    return HttpResponse(json.dumps(regression_array), content_type='application/json')






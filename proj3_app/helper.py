import json
from django.db.models import Count
from django.http import HttpResponse
from proj3_app.models import Report

__author__ = 'joaquincunanan'

def cat_regression(request,cat):
    from numpy import arange
    from scipy import stats
    import numpy
    data = Report.objects.filter(category=cat).values('date', 'category').annotate(total=Count('incident')).order_by('date','category')
    assault = []
    for i in data:
        assault.append(i['total'])
    old = numpy.array([])
    np_assault = numpy.append(old, assault)
    l = len(assault)
    xi = arange(0, l)
    # a = array([xi,ones(l)])
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi, np_assault)
    print 'r value', r_value
    print  'p_value', p_value
    print 'standard deviation', std_err
    print 'slope ',slope
    print 'intercept ',intercept
    data={}
    data['slope']=slope
    data['intercept']=intercept
    data['r_value']=r_value
    data['p_value']=p_value
    data['std_err']=std_err
    x=0
    regression_array=[]
    for i in assault:
        x=x+1
        y=slope*x+intercept
        regression_array.append(y)


    return HttpResponse(json.dumps(regression_array), content_type='application/json')
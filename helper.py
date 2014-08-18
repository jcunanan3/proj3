from proj3_app.models import Report
import csv
from datetime import datetime


with open('/Users/joaquincunanan/Downloads/sfpd_incident_all_csv 2/sfpd_incident_2014.csv', 'rb') as csvfile:
    crime_reader = csv.reader(csvfile, delimiter=',')
    index = 0
    for row in crime_reader:
        if index != 0:
            Report.objects.create(incident=row[0], category=row[1], description=row[2], dayofweek=row[3], date=datetime.strptime(row[4],'%m/%d/%Y'), time=row[5], precinct=row[6], resolution=row[7], location=row[8], lat=row[9], long=row[10])
        index += 1



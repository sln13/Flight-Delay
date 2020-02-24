import urllib2
import json
i=0
url='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=8637d4fb63364d6b9c5132548172803&q=ORD&format=json&date=2015-01-01&enddate=2015-01-31&tp=1'
obj=urllib2.urlopen(url)
data=json.load(obj)
for l in range(0,1000):
	print data['data']['weather'][32]['date'],data['data']['weather'][0]['hourly'][i]['time'],data['data']['weather'][0]['hourly'][i]['winddirDegree'],data['data']['weather'][0]['hourly'][i]['windspeedKmph'],data['data']['weather'][0]['hourly'][i]['visibility'],data['data']['weather'][0]['hourly'][i]['precipMM'],data['data']['weather'][0]['hourly'][i]['weatherCode']


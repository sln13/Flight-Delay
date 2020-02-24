wwapi='8637d4fb63364d6b9c5132548172803'

from dateutil.relativedelta import relativedelta
import urllib2
import json
import datetime
url=''
s='2011-01-01'
date1='2011-01-01'
date='2011-02-28'
code=['ATL','LAX', 'ORD', 'DFW','DEN','JFK','SFO','CLT','LAS','PHX']
code1=['10397','12892','13232','11298','11292','12478','14771','11057','12889','14107']
d=datetime.datetime.strptime(s,'%Y-%m-%d')
d1=datetime.datetime.strptime(date,'%Y-%m-%d')

for j in range(0,10):
	for z in range(1,13):
			d=datetime.datetime.strptime(s,'%Y-%m-%d')+ relativedelta(month=1)
			if z in [1,3,5,7,8,10,12]:
				k=31
			if z in [4,6,9,11]:
				k=30
			if z==2:
				k=28
			url='http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=8637d4fb63364d6b9c5132548172803&q='+code[j]+'&format=json&date=2011-'+str(z)+'-01&enddate=2011-'+str(z)+'-'+str(k)+'&tp=1' 	
			obj=urllib2.urlopen(url)
			data=json.load(obj)
			for l in range(0,k):
				for i in range(0,24):
					print code1[j],d.year,z,l+1,data['data']['weather'][l]['date'], data['data']['weather'][l]['hourly'][i]['time'],data['data']['weather'][l]['hourly'][i]['winddirDegree'],data['data']['weather'][l]['hourly'][i]['windspeedKmph'],data['data']['weather'][l]['hourly'][i]['visibility'],data['data']['weather'][l]['hourly'][i]['precipMM'],data['data']['weather'][l]['hourly'][i]['weatherCode']	
				s=d
				s=s.strftime('%Y-%m-%d')

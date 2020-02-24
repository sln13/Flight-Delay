import csv
import pandas as pd
path3='dataweather2015.csv'
output = open (path3,'a')
x=pd.read_csv("data2015f.csv")
y=pd.read_csv("weather2015f.csv")
if  y['TIME'][6]==(x['DEP_TIME'][0]-x['DEP_TIME'][0]%60):
	print 'hello'

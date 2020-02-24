
import csv
d=['10397','12892','13232','11298','11292','12478','14771','11057','12889','14107']
path1='weather2013.csv'
path2='weather2013f.csv'
outdata=[]
i=open(path1,'rb')
o=open(path2,'a')
reader=csv.reader(i,delimiter=',')
writer=csv.writer(o,delimiter=',')
for row in reader:
	row[4]=int(row[4])/100.0
	b=row[4]%1
	c=row[4]//1
	row[4]=b*100+c*60
        outdata.append([row[0], row[1],row[2], row[3], str(row[4]), str(row[5]), row[6],str( row[7]),row[8],row[9]])

writer.writerows(outdata)

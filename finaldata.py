import csv
path1="data2015f.csv"
path2='weather2015f.csv'
path3='dataweather2015.csv'
outdata=[]
count=0
i= open(path1,'r')
i1=open(path2,'r')
output = open (path3,'a')
r=csv.reader(i, delimiter=',')
r1=csv.reader(i1, delimiter=',')
writer=csv.writer(output,delimiter=',')
for row in r:
	for row1 in r1:
		
		a=int(row[5])
		b=int(row1[4])	
		if int(row1[0])==int(row[3]) and int(row1[2])==int(row[1]) and int(row1[3])==int(row[2]) and b==(a-a%60):
	      		outdata.append([row1[0], row[0],row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8],row1[5],row1[6],row1[7],row1[8],row1[9]])
			count=count+1
			print count
			break
	i1=open(path2,'r')
	r1=csv.reader(i1, delimiter=',')
	if count%5000==0:
		print 'hello'
writer.writerows(outdata)

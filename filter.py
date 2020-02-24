import csv
month=['jan2013.csv','feb2013.csv','mar2013.csv','apr2013.csv','may2013.csv','jun2013.csv','jul2013.csv','aug2013.csv','sep2013.csv','oct2013.csv','nov2013.csv','dec2013.csv']
k_range=range(0,12)
for k in k_range:
	path1=month[k]
	path2='data2013.csv'
	outdata = []
	b=''
	inp = open(path1,'rb')
	output = open (path2,'a')
	a=[ '10397','12892','13232','11298','11292','12478','14771','11057','12889','14107']
	reader=csv.reader(inp, delimiter=',')
	writer=csv.writer(output,delimiter=',')
	for row in reader:
 		if row[3] in a and row[4] in a and not(b in row[4:9]):
			 	outdata.append([row[0], row[1], row[2],row[3], row[4], row[5], row[6], row[7], row[8]])
	writer.writerows(outdata)
		

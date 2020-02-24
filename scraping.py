import requests
from BeautifulSoup import BeautifulSoup
url='https://www.wunderground.com/history/airport/KORD/2016/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2016&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo='
response=requests.get(url)
html=response.content
soup=BeautifulSoup(html)
table=soup.find('tbody')
for row in table.findAll('tr'):
	for cell in row.findAll('td'):	
		print soup.prettify()

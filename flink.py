# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html "
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Lilly.html"

count = raw_input('Enter count: ')
pos = raw_input('Enter position: ')

for i in range(1, int(count)+1):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	# Retrieve all of the anchor tags
	tags = soup('a')
	print str(i) + '-Retrieving: ' + url
	my_pos = int(pos)
	for tag in tags:
		my_pos = my_pos - 1
		if(my_pos == 0):
	   		url = tag.get('href', None)

print str(i) + '-Last Url: ' + url
	   		
	   	
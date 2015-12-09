# get json form url
import json
import urllib

url = raw_input('Enter url: ')
if len(url) < 1 : exit

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: info = json.loads(str(data))
except: info = None
#print json.dumps(info, indent=4)

sum = 0
num = 0
for item in info["comments"]:
    count =  item["count"]
    num = num + 1
    sum = sum + int(count)

print "Count: ", num
print "Sum: ", sum


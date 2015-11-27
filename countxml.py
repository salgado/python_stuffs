import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter url: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    
    
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')

    sum = 0
    for count in counts:
        sum = sum + int(count.text)

    print "Count:", len(counts)
    print "Sum:", sum

    #results = tree.findall('result')
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

    break
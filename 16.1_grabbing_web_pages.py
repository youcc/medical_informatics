import urllib2
req = urllib2.Request('http://www.julesberman.info/factoids/batch.htm')
try:
    response = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code: ', e.code
except urllib2.URLError, e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason
else:
    print urllib2.urlopen(req).read()
req = urllib2.Request('http://www.julesberman.info/factoids/xxxxx.htm')
try:
    response = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print 'The server couldn\’t fulfill the request.'
    print 'Error code: ', e.code
except urllib2.URLError, e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason
else:
    print urllib2.urlopen(req).read()    
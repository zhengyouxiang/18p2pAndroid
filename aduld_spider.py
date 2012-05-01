import urllib2
import urllib
import httplib

#data=urllib.urlencode({'formhash':'80bfd6e5','referer':'/index','cookietime':'315360000','username': 'yuan910108','password':'910108'})
h=httplib.HTTPConnection('www.18p2p.com')
h.request('GET','/forum/viewthread.php?tid=4277830&extra=page%3D1')
r=h.getresponse()

s=r.read()
#s=urllib2.urlopen("http://www.18p2p.com/forum/logging.php?action=login").read()

s= s.decode('Big5')
print type(s)
print s
#s=s.encode('GB2312')
# print type(s)
# print s

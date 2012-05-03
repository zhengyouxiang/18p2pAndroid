import cookielib,urllib2,urllib,re
from pyquery import PyQuery as pq
from sgmllib import SGMLParser
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
#data=urllib.urlencode({'formhash':'80bfd6e5','referer':'/index','cookietime':'315360000','username': 'yuan910108','password':'910108'})


home=opener.open('http://18p2p.com/forum/logging.php?action=login&1',data="username=yuan910108&password=910108&formhash=80bfd6e5&referer=http://18p2p.com/forum/index.php&cookietime=2592000&loginfield=username&questionid=0&answer=&loginsubmit=%B7%7C%AD%FB%B5n%A4J")
#print home.read().decode('Big5')
print cj
fuck=opener.open('http://18p2p.com/forum/forumdisplay.php?fid=126')
#print fuck.read().decode('Big5')
i=fuck.read().decode('Big5')
directions=re.findall(r'viewthread.php\?tid=\d{7}&extra=page%3D1',i)
wait_list={}.fromkeys(directions).keys()
#directions=re.findall(r'viewthread.php?tid',i)
for archor in wait_list:
    print archor
#print  type(i)

#print type(i)

#d=pq(i)
#p=d(".altbg2")
#p= p.find('a')


#print  p
#parse=SGMLParser()
#parse.feed(i)



import urllib2
req=urllib2.Request("http://18p2p.com/forum/viewthread.php?tid=4277880&extra=page%3D1")
req.add_header('Cookie','cdb_sid=QXiXwZ; cdb_cookietime=315360000; cdb_auth=NV5hS6xcFXkdLGYSJU8JDfNVTyeLkhVHMgobluT5EroEP6bnDGCuJBcfwyTz3O2IJw; cdb_visitedfid=126;')
req.add_header('Referer','http://18p2p.com/forum/forumdisplay.php?fid=126')

res=urllib2.urlopen(req)
html=res.read()
print html.decode('Big5')
res.close()

# -*- coding: utf-8 -*-
test='asdasdadasdhttp://abc.jpg'
import re
collections=re.findall(r'http://\w*.jpg',test)
for collection in collections:
    print collection



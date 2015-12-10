# -*- coding: UTF-8 -*-

import re
print(re.search('www','www.cunoob.com').span())# 在起始位置匹配
print(re.search('com','www.cunoob.com').span())# 不在起始位置匹配

line = "Cats are smarter than dogs";

searchObj=re.search(r'(.*) are (.*?) .*',line,re.M|re.I)  #re.I：忽略大小写  re.M：多行模式

if searchObj:
    print "searchObj.group(): ",searchObj.group()
    print "searchObj.group(1): ",searchObj.group(1)
    print "searchObj.group(2): ",searchObj.group(2)
else:
    print "Nothing found!"
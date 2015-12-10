# -*- coding: UTF-8 -*-

#match:
import re
print(re.match('www','www.runoob.com').span())# 在起始位置匹配
print(re.match('com','www.runoob.com'))# 不在起始位置匹配


line="Cats are smarter than dogs"
matchObj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)  #re.I：忽略大小写  re.M：多行模式

if matchObj:
    print "matchObj.group(): ",matchObj.group()
    print "matchObj.group(1): ",matchObj.group(1)
    print "matchObj.group(2): ",matchObj.group(2)
else:
    print "No match!"
# -*- coding:utf-8 -*-  
#按页删除人人网状态程序

import urllib
import urllib2
import cookielib
import re

#初始化一个CookieJar来处理Cookie的信息#  
cookie = cookielib.CookieJar()

#创建一个新的opener来使用我们的CookieJar#  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

#提交用户名密码
postdata = urllib.urlencode({
    'email':'',
    'password':'',

#模拟登录
req = urllib2.Request(
    url = 'http://m.renren.com/login.do',
    data = postdata

)
result = opener.open(req).read()

#获取sid,rtk
resultsid = re.findall(r'sid=(.*?)&',result)

renrensid = resultsid[0]
print renrensid
resultrtk = re.findall(r'_rtk=(.*?)&',result)
renrenrtk = resultrtk[0]
print renrenrtk

#获取状态页
statusurl = 'http://3g.renren.com/status/getdoing.do?&sid='+renrensid
statuspage = opener.open(statusurl).read()
print statuspage

#获取状态ID：
resultname = re.findall(r'a name..(\d*?).>',statuspage)
print resultname

postdel = urllib.urlencode({
    'sid':renrensid,
    '_rtk':renrenrtk,
    
})

for renrenname in resultname:
    print renrenname
    statusurll = 'http://3g.renren.com/status/wdelstatus.do?id='+renrenname
    reqdel = urllib2.Request(
        url = statusurll,
        data = postdel

    )
    print reqdel
    resultdel = opener.open(reqdel).read()

  
    



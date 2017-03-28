import re
url1 = 'http://qd.fang.anjuke.com/loupan/415720.html?from=loupan_tab'
url2 = 'http://qd.fang.anjuke.com/loupan/canshu-415720.html?from=loupan_tab'
num = re.findall(r'\d+', url1)[0]
url3 = url1.replace(num, 'canshu-'+num)
print(url3 == url2)
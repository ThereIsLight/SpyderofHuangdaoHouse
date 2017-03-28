import re

url = """"
{
2017-09-09"totalPage":,"curPage":} 1234.349090909 ,456, 121231. ,2017-09-09
"""
int_num = re.compile(r'\d+')
float_num = re.compile(r'\d+\.?\d*')  #缺点是121231. 这种数字也能匹配
time = re.compile(r"\d{4}-\d{1,2}-\d{1,2}")  # 匹配日期，格式为XXXX-XX-XX。

print(re.findall(int_num, url))
print(re.findall(float_num, url))
print(re.findall(r"\d{4}-\d{1,2}-\d{1,2}", url))
print(re.findall(time, url))
import re


str = '123.123㎡'
# temp = re.findall(r'\d+.?\d*', str)
temp = str.strip('㎡')
print(temp)
print(double(temp))
# print(number + 1)
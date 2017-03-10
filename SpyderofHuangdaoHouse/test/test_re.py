import re

url = """"
{"totalPage":446584121,315465486545,"curPage":}
"""
print(re.findall(r"\d+", url))
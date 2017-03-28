import re
"""
总结提取到的开盘时间与交房时间的格式
1.尚未公开(没有任何数字)
2.明确的年月日 格式为XXXX-XX-XX。
3.只有年份 格式为XXXX
4.有明确的年月日，但是还包含其他的信息。例如2017-05-31  （预计2017年5月交付）
5.只有年份月份，没有日期。XXXX-XX
"""
list = [
    "2017",
    "2016-09-09",
    "尚未公开",
    "2017-05-31  （预计2017年5月交付）",
    "2016-03-12   （6#加推）",
    "2017-06"
]


def get_correct_time(str):

    res = re.findall(r"\d{4}-\d{1,2}-\d{1,2}", str)
    if not res:
        res = re.findall(r"\d{4}-\d{1,2}", str)
        if not res:
            res = re.findall(r"\d{4}", str)
            if not res:
                return str  # 直接返回尚无数据
            else:
                return res[0] + '-12' + '-30'  # 直接返回年+月份12+日期30
        else:
            return res[0] + "-01"  # 直接返回年月+日期为01
    else:
        return res[0]  # 直接返回年月日
for str in list:
    print(get_correct_time(str))
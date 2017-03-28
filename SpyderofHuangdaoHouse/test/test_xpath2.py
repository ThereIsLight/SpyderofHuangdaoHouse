import lxml.etree as etree
html = """
<ul id="parameter2" class="p-parameter-list">
 <li title='养生堂天然维生素E软胶囊'>商品名称：养生堂天然维生素E软胶囊</li>
 <li title='720135'>商品编号：720135</li>
 <li title='养生堂'>品牌：<a>养生堂</a></li>
 <li title='养生堂'><a>养生堂</a></li>
</ul>
"""
tree = etree.HTML(html)
property_list_reg = '//ul[@id="parameter2"]//li'
property_lst = tree.xpath(property_list_reg)
for e in property_lst:
    print(e.xpath('string(.)'))
    # print(e.xpath('text()'))
print(len(property_lst))
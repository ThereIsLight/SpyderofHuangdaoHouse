import lxml.etree as etree
html = """
<ul id="parameter2" class="p-parameter-list">
 <li title='养生堂天然维生素E软胶囊'>商品名称：养生堂天然维生素E软胶囊</li>
 <li title='720135'>商品编号：720135</li>
 <li title='养生堂'>品牌：<a>养生堂<span>小小养生堂</span></a><a>养生堂2</a><a>养生堂3</a></li>
</ul>
"""

tree = etree.HTML(html)

property_list_reg = '//ul[@id="parameter2"]/li'


def tryFindChild(element):
    children = element.getchildren()  # getchildren()只能会的一级子标签，不能会的二级子标签。
    if len(children):
        print(children, len(children))
        return element.text + " " + children[0].text
    else:
        return element.text

property_lst = tree.xpath(property_list_reg)
for e in property_lst:
    print(tryFindChild(e))

print(len(property_lst))
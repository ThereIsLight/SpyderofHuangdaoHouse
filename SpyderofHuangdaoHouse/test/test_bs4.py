from bs4 import BeautifulSoup
html = """
<li>
    <span class="hello"> Hello</span>
    World
</li>
"""

soup = BeautifulSoup(html, "lxml")
a = soup.find('li').find('span').get_text().extract()
# a = soup.find('li').find('li').get_text().extract()
print(a)
from bs4 import BeautifulSoup
html = """
<li>
    <span class="hello"> Hello</span>
    World
</li>
"""
soup = BeautifulSoup(html, "lxml")
a = BeautifulSoup(html, "lxml").find('li').contents
# a = soup.find('li')
# print(a.contents[-1].strip())
print(a)
# print(b)
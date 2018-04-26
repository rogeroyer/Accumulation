import urllib.request
import urllib.parse
import re

response = urllib.request.urlopen('http://jwzx.cqupt.edu.cn/jwzxtmp/showBjStu.php?bj=04121709')
html = response.read().decode('utf-8')
print(type(html))
print(html)

# pattern1 = r'<tr><td>/d{,2}</td><td>/d{10}</td><td>\w?</td><td>[男女]</td><td>04121709'
# pattern1 = r'<td>[男女]</td>'
# pattern1 = r'<td>[0-28]</td>'
# pattern1 = r'<td>[0-9]</td>'
pattern1 = u'</td><td>([\u4e00-\u9fa5]+)</td><td>[男女]</td><td>04121709'
pattern2 = r'韦鑫桥'
# print(re.search(pattern1, html, re.M))
print(re.search(pattern1, html, re.M).group())
print(re.search(pattern2, html, re.M).group())

# namelist = re.findall(pattern1, html)
# for name in namelist:
#     print(name)

# <tr><td>2</td><td>2017211978</td><td>努尔比耶·图拉克</td><td>女</td><td>04121709</td>

# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """
<p>　<a href="http://www.xza.edu.cn">西藏农牧学院</a> <small>林芝市 </small>,　<a title="西藏教育厅：edu.xizang.gov.cn" href="http://www.utibet.edu.cn">西藏大学</a> <small>拉萨市 </small>,　<a href="http://www.xzmu.edu.cn">西藏民族大学</a> <small>咸阳市 </small>,　<a href="http://www.ttmc.edu.cn">西藏藏医药大学</a> <small>拉萨市 </small>	<br><br>	高职大专3所：<small>　<a href="http://www.tpa.net.cn">西藏警官高等专科学校</a> 🛂拉萨市 ,　<a href="http://www.xzlssf.org">拉萨师范高等专科学校</a>  ,　<a href="http://www.xzgzy.cn">西藏职业技术学院</a> 拉萨市 </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>

"""


soup = BeautifulSoup(html_str, 'html.parser')

result = []
for a in soup.find_all('a'):
    link = a.get('href')
    name = a.get_text()
    addr = a.find_next_sibling('small')
    if addr is not None:
        addr = addr.get_text()
    else:
        addr = ""
    result.append({'link': link, 'name': name, 'addr': addr})


json_result = json.dumps(result, ensure_ascii=False)

print(json_result)

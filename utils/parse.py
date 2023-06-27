# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """
<p>　<a href="http://www.qhu.edu.cn">青海大学</a> <small>西宁市 </small>,　<a href="http://www.qhnu.edu.cn">青海师范大学</a> <small>西宁市 </small>,　<a href="http://www.qhmu.edu.cn">青海民族大学</a> <small>西宁市 </small>,　¥ 青海大学<a title="新域名" href="http://klc.qhu.edu.cn">昆仑学院</a> <small>西宁市 </small>	<br><br>	高职大专8所：<small>　<a href="http://www.qhwszy.edu.cn">青海卫生职业技术学院</a> 西宁市 ,　<a href="https://www.qhjyedu.com/">青海警官职业学院</a> 🛂西宁市 ,　<a href="http://www.qhxmzy.cn">青海农牧科技职业学院</a> 西宁市 ,　<a href="http://www.qhctc.edu.cn">青海交通职业技术学院</a> 西宁市 ,　<a href="http://www.qhnews.com/bdt/jt/jzxy/">青海建筑职业技术学院</a> 西宁市 ,　<a href="http://www.xncy.edu.cn">西宁城市职业技术学院</a>  ,　<a href="http://www.qhvtc.edu.cn">青海高等职业技术学院</a> 海东市 ,　<a href="http://61.133.238.121">青海柴达木职业技术学院</a> 海西州 </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>

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

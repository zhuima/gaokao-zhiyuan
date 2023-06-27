# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """<p>　<a href="http://www.hainu.edu.cn">海南大学</a> <small>海口市 </small>,　<a href="http://www.hntou.edu.cn">海南热带海洋学院</a> <small>三亚市 </small>,　<a href="http://www.hainnu.edu.cn">海南师范大学</a> <small>海口市 </small>,　<a href="http://www.hainmc.edu.cn">海南医学院</a> <small>海口市 </small>,　<a href="http://www.qtnu.edu.cn">琼台师范学院</a> <small>海口市 </small>,　境外自贸港<a title="2023新本科" href="http://www.hsbi.de">海南比勒费尔德应用科学大学</a> <small>陵水黎族自治县 </small>,　¥ <a href="http://www.hkc.edu.cn">海口经济学院</a>,　¥ <a href="http://www.sanyau.edu.cn">三亚学院</a>,　¥ <a href="http://www.hnkjedu.cn">海南科技职业大学</a> <small>海口市 </small>	<br><br>	高职大专13所：<small>　<a href="http://www.hcvt.cn">海南职业技术学院</a> 海口市 ,　<a href="http://www.hnspi.edu.cn">海南软件职业技术学院</a> 琼海市 ,　<a href="http://www.hnplc.com">海南政法职业学院</a> ⚖️海口市 ,　<a href="http://www.hnflvc.com">海南外国语职业学院</a> 文昌市 ,　<a href="http://www.hnjmc.com">海南经贸职业技术学院</a> 海口市 ,　<a href="http://www.hnstx.com">海南体育职业技术学院</a> 🏃海口市 ,　<a href="http://www.hnhvc.edu.cn">海南卫生健康职业学院</a> 海口市 ,　¥ <a href="http://www.sycsxy.cn">三亚城市职业学院</a>  ,　¥ <a href="http://www.hntbc.edu.cn">海南工商职业学院</a> 海口市 ,　¥ <a href="http://www.hnasatc.com">三亚航空旅游职业学院</a>  ,　¥ <a href="http://www.ucsanya.com">三亚理工职业学院</a>  ,　¥ <a title="%挑网络" href="http://www.his.edu.cn">三亚中瑞酒店管理职业学院</a>  ,　¥ <a href="http://www.hainhmc.edu.cn">海南健康管理职业技术学院</a> 海口市 </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>"""


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

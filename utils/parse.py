# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """
<p>　<sup>国家民委</sup>❕<a href="http://www.nwsni.edu.cn"><b>北方民族大学</b></a> <small>银川市 </small>,　<a href="http://www.nxu.edu.cn">宁夏大学</a> <small>银川市 </small>,　<a href="http://www.nxmu.edu.cn">宁夏医科大学</a> <small>银川市 </small>,　<a title="新域名" href="http://www.nxnu.edu.cn">宁夏师范学院</a> <small>固原市 </small>,　¥ <a href="http://www.nxist.com">宁夏理工学院</a> <small>石嘴山市 </small>,　¥ 宁夏大学<a href="http://xinhua.nxu.edu.cn">新华学院</a> <small>银川市 </small>,　¥ <a href="http://www.ycu.com.cn">银川能源学院</a>,　¥ <a href="http://www.ycust.edu.cn">银川科技学院</a>	<br><br>	高职大专13所：<small>　<a href="http://www.nxmzy.com">宁夏民族职业技术学院</a> 吴忠市 ,　<a>宁夏工业职业学院</a> 4164012837 银川市 原ip停服：61.133.209.245，<a href="https://www.smenx.com.cn/rcgnk/yxxx/451529.shtml">地方平台</a>,　<a href="http://www.nxtc.edu.cn">宁夏职业技术学院</a> 银川市 ,　<a href="http://www.nxjm.com">宁夏工商职业技术学院</a> 银川市 ,　<a href="http://www.nxcy.edu.cn">宁夏财经职业技术学院</a> 银川市 ,　<a href="http://www.nsjy.com.cn">宁夏警官职业学院</a> 🛂银川市 ,　<a href="http://www.nxjy.edu.cn">宁夏建设职业技术学院</a> 银川市 ,　<a href="http://www.nxfszs.cn">宁夏葡萄酒与防沙治沙职业技术学院</a> 银川市 ,　<a>宁夏幼儿师范高等专科学校</a> 4164014498 银川市 <a href="https://jyj.yinchuan.gov.cn/xwgk/xxgkxx/202010/t20201020_2261197.htm">政府介绍</a>,　<a>宁夏艺术职业学院</a> 4164014522 银川市 <a href="https://www.smenx.com.cn/rcgnk/yxxx/375315.shtml">地方信息</a>,　<a href="http://www.nxtzy.com.cn">宁夏体育职业学院</a> 🏃银川市 ,　<a href="http://www.nxszsgm.com">石嘴山工贸职业技术学院</a>  ,　<a>宁夏卫生健康职业技术学院</a> 4164014804 石嘴山市 </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>


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

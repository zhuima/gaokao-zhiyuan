# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """
<p>　<sup>教育部</sup>❕<a href="http://www.lzu.edu.cn"><b>兰州大学</b></a> <small> <a href="https://ir.lzu.edu.cn/community-list">机构知识库</a></small>,　<sup>国家民委</sup>❕<a href="http://www.xbmu.edu.cn"><b>西北民族大学</b></a> <small>兰州市 </small>,　<a title="新域名" href="http://www.lut.edu.cn">兰州理工大学</a>,　<a href="http://www.lzjtu.edu.cn">兰州交通大学</a>,　<a href="http://www.gsau.edu.cn">甘肃农业大学</a> <small>兰州市 </small>,　<a href="http://www.gszy.edu.cn">甘肃中医药大学</a> <small>兰州市 </small>,　<a href="http://www.nwnu.edu.cn">西北师范大学</a> <small>兰州市 </small>,　<a href="http://www.lzcu.edu.cn">兰州城市学院</a>,　<a href="http://www.ldxy.edu.cn">陇东学院</a> <small>庆阳市 </small>,　<a href="http://www.tsnc.edu.cn">天水师范学院</a>,　<a href="https://www10.hxu.edu.cn/">河西学院</a> <small>张掖市 </small>,　<a href="http://www.lzufe.edu.cn">兰州财经大学</a>,　<a href="http://www.gsupl.edu.cn">甘肃政法大学</a> <small>⚖️兰州市 </small>,　<a href="http://www.gnun.edu.cn">甘肃民族师范学院</a> <small>甘南藏族自治州 </small>,　<a href="http://www.luas.edu.cn">兰州文理学院</a>,　<a href="http://www.gsmc.edu.cn">甘肃医学院</a> <small>平凉市 </small>,　<a title="域名失效：www.lzit.edu.cn">兰州工业学院</a> 4162011807 <small> <a href="http://lzptc.fanya.chaoxing.com/portal">超星教学</a></small>,　<a href="http://www.lzpcc.edu.cn">兰州石化职业技术大学</a>,　<a href="http://www.lzre.edu.cn">兰州资源环境职业技术大学</a>,　¥ <a href="http://www.lanzhoutbc.cn">兰州工商学院</a>,　¥ <a href="http://www.bowenedu.cn">兰州博文科技学院</a>,　¥ <a href="http://www.lzxk.edu.cn">兰州信息科技学院</a>	<br><br>	高职大专28所：<small>　<a href="http://www.lntc.edu.cn">陇南师范高等专科学校</a>  ,　<a href="http://www.dxatc.cn">定西师范高等专科学校</a>  ,　<a href="http://www.gcvtc.gsedu.cn">甘肃建筑职业技术学院</a> 兰州市 ,　<a href="http://www.jqzy.com">酒泉职业技术学院</a>  ,　<a href="http://www.lvu.edu.cn">兰州职业技术学院</a>  ,　<a href="http://www.gs-police.com">甘肃警察职业学院</a> 🛂兰州市 ,　<a href="http://www.gsfc.edu.cn">甘肃林业职业技术学院</a> 天水市 ,　<a href="http://www.gsipc.gsedu.cn">甘肃工业职业技术学院</a> 天水市 ,　<a href="http://www.wwoc.cn">武威职业学院</a>  ,　<a href="http://www.gsjtxy.edu.cn">甘肃交通职业技术学院</a> 兰州市 ,　<a href="http://www.gnzy.gssedu.cn">甘肃农业职业技术学院</a> 兰州市 ,　<a href="http://www.xmgcxy.gsedu.cn">甘肃畜牧工程职业技术学院</a> 武威市 ,　<a href="http://www.gsgtzy.cn">甘肃钢铁职业技术学院</a> 嘉峪关市 ,　<a href="http://www.gsjdxy.com">甘肃机电职业技术学院</a> 天水市 ,　<a href="http://www.gsysyj.org">甘肃有色冶金职业技术学院</a> 金昌市 ,　<a href="http://www.byjsxy.com">白银矿冶职业技术学院</a>  ,　<a href="http://www.gswx.com.cn">甘肃卫生职业学院</a> 兰州市 ,　<a href="http://www.qyvtc.com">庆阳职业技术学院</a>  ,　<a href="http://www.lxxdzy.com">临夏现代职业学院</a>  ,　<a href="http://www.lzmvc.edu.cn">兰州现代职业学院</a>  ,　<a href="http://www.plvtc.cn">平凉职业技术学院</a>  ,　<a href="http://www.plzyxy.com">培黎职业学院</a> 张掖市 ,　<a href="http://60.165.53.253/">兰州航空职业技术学院</a>  ,　<a href="http://www.gscmxy.edu.cn">甘肃财贸职业学院</a> 兰州市 ,　<a>定西职业技术学院</a> 4162014823  ,　¥ <a href="http://www.lzwyedu.com">兰州外语职业学院</a>  ,　¥ <a href="http://www.lzkjedu.com">兰州科技职业学院</a>  ,　¥ <a title="%Fx" href="http://byhvatc.com">白银希望职业技术学院</a>  </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>


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

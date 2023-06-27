# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """
<p>　<a href="http://www.ynu.edu.cn">云南大学</a> <small>昆明市 </small>,　<a href="http://www.kmust.edu.cn">昆明理工大学</a>,　<a href="http://www.ynau.edu.cn">云南农业大学</a> <small>昆明市 </small>,　<a href="http://www.swfc.edu.cn">西南林业大学</a> <small>昆明市 </small>,　<a href="http://www.kmmu.edu.cn">昆明医科大学</a>,　<a href="http://www.dali.edu.cn">大理大学</a>,　<a href="http://www.ynutcm.edu.cn">云南中医药大学</a> <small>昆明市 </small>,　<a href="http://www.ynnu.edu.cn">云南师范大学</a> <small>昆明市 </small>,　<a href="http://www.ztu.edu.cn">昭通学院</a>,　<a href="http://www.qjnu.edu.cn">曲靖师范学院</a>,　<a href="http://www.peuni.cn">普洱学院</a>,　<a href="http://www.bsnc.cn">保山学院</a>,　<a href="http://www.uoh.edu.cn">红河学院</a>,　<a href="http://www.ynufe.edu.cn">云南财经大学</a> <small>昆明市 </small>,　<a href="http://www.ynart.edu.cn">云南艺术学院</a> <small>昆明市 </small>,　<a href="http://www.ynni.edu.cn">云南民族大学</a> <small>昆明市 </small>,　<a href="http://www.yxtc.edu.cn">玉溪师范学院</a>,　<a href="http://www.cxtc.edu.cn">楚雄师范学院</a>,　<a href="http://www.ynpsc.edu.cn">云南警官学院</a> <small>🛂昆明市 </small>,　<a href="http://www.kmu.edu.cn">昆明学院</a>,　<a title="网站疑似故障？" href="http://www.wsu.edu.cn">文山学院</a>,　<a href="http://www.wynu.edu.cn">滇西科技师范学院</a> <small>临沧市 </small>,　<a href="http://www.wyuas.edu.cn">滇西应用技术大学</a> <small>大理白族自治州 </small>,　¥ <a href="http://www.ynjgy.com">云南经济管理学院</a> <small>昆明市 </small>,　¥ 云南大学<a href="http://dcxy.ynu.edu.cn">滇池学院</a> <small>昆明市 </small>,　¥ <a href="http://lywhxy.com">丽江文化旅游学院</a>,　¥ 昆明理工大学<a href="http://www.oxbridge.cn">津桥学院</a>,　¥ <a title="原云南师范大学商学院" href="http://www.kmcc.edu.cn">昆明城市学院</a>,　¥ <a href="http://www.caskm.cn">昆明文理学院</a>,　¥ 昆明医科大学<a href="http://www.kyhyxy.com">海源学院</a>,　¥ 云南艺术学院<a href="http://whxy.ynart.edu.cn">文华学院</a> <small>昆明市 </small>,　¥ <a title="重新定义高校住宿文化" href="https://www.ytbu.edu.cn">云南工商学院</a> <small>昆明市 </small>	<br><br>	高职大专56所：<small>　<sup>应急管理部</sup>❕<a>公安消防部队高等专科学校</a> 4153014534 昆明市 ,　<a href="http://www.ynny.cn">云南能源职业技术学院</a> 曲靖市 ,　<a title="云南开放大学" href="http://www.ynou.edu.cn">云南国防工业职业技术学院</a> 昆明市 ,　¥ <a href="http://ynxzy.com">云南新兴职业学院</a> 昆明市 ,　<a href="http://www.kmyz.edu.cn">昆明冶金高等专科学校</a>  ,　<a href="http://www.yngtxy.net">云南国土资源职业学院</a> 昆明市 ,　<a href="http://www.yncs.edu.cn">云南交通职业技术学院</a> 昆明市 ,　<a href="http://www.kmvtc.net">昆明工业职业技术学院</a>  ,　<a href="http://www.ynavc.com">云南农业职业技术学院</a> 昆明市 ,　<a href="http://www.yncpu.net">云南司法警官职业学院</a> 🛂昆明市 ,　<a href="http://www.ynarts.cn">云南文化艺术职业学院</a> 昆明市 ,　<a href="http://www.ynasc.com">云南体育运动职业技术学院</a> 🏃昆明市 ,　<a href="http://www.xsbnzy.com">西双版纳职业技术学院</a>  ,　<a href="http://www.yxnzy.net/">玉溪农业职业技术学院</a>  ,　<a href="http://www.ynmec.com">云南机电职业技术学院</a> 昆明市 ,　<a href="http://www.ynftc.cn">云南林业职业技术学院</a> 昆明市 ,　<a href="http://www.qjyz.org">曲靖医学高等专科学校</a>  ,　<a href="http://www.cxmtc.net">楚雄医药高等专科学校</a>  ,　<a href="http://www.ynbsyz.cn">保山中医药高等专科学校</a>  ,　<a href="http://www.lj-edu.cn">丽江师范高等专科学校</a>  ,　<a href="http://www.yndhec.net">德宏师范高等专科学校</a>  ,　<a href="https://www.ytvtc.com/">云南锡业职业技术学院</a> 红河州 ,　<a href="http://www.yndhvc.com">德宏职业学院</a>  ,　<a>云南现代职业技术学院</a> 4153014373 楚雄彝族自治州 ,　<a href="http://ynctv.edu.cn">云南旅游职业学院</a> 昆明市 ,　<a href="http://www.hhwzy.edu.cn">红河卫生职业学院</a>  ,　<a href="http://www.dlafc.com">大理农林职业技术学院</a>  ,　<a href="http://www.ynczy.edu.cn">云南财经职业学院</a> 昆明市 ,　<a href="http://www.kmtdzy.cn">昆明铁道职业技术学院</a>  ,　<a href="http://www.ztwzy.cn">昭通卫生职业学院</a>  ,　<a href="http://www.DLHLzyxy.edu.cn">大理护理职业学院</a>  ,　<a title="旧域名停用：ynszy.net" href="http://ynwater.edu.cn">云南水利水电职业学院</a> 昆明市 ,　<a href="http://ynqfzyxy.cn">云南轻纺职业学院</a> 昆明市 ,　<a href="http://www.yntjzy.cn">云南特殊教育职业学院</a> 昆明市 ,　<a href="http://www.ynit.edu.cn">云南工贸职业技术学院</a> 昆明市 ,　<a href="http://www.ynvct.com">云南交通运输职业学院</a> 昆明市 ,　<a href="https://www.kmyesf.cn">昆明幼儿师范高等专科学校</a>  ,　<a href="http://www.qjzyxy.com">曲靖职业技术学院</a>  ,　<a href="http://www.hhvtc.cn">红河职业技术学院</a>  ,　<a>玉溪职业技术学院</a> 4153014782  ,　<a>保山职业学院</a> 4153014783  ,　<a>昭通职业学院</a> 4153014784  ,　<a>文山职业技术学院</a> 4153014801  ,　<a>丽江职业技术学院</a> 4153014802  ,　<a>香格里拉职业学院</a> 4153014803 迪庆藏族自治州 ,　¥ <a href="http://www.ynkexin.cn">云南科技信息职业学院</a> 昆明市 ,　¥ <a href="http://www.kmac.org.cn">昆明艺术职业学院</a>  ,　¥ <a href="http://www.yncjxy.com">云南城市建设职业学院</a> 昆明市 ,　¥ <a href="http://www.sailingedu.com">云南工程职业学院</a> 昆明市 ,　¥ <a href="http://www.ynjw.net">云南经贸外事职业学院</a> 昆明市 ,　¥ <a href="http://www.ynsxzy.com">云南三鑫职业技术学院</a> 文山州 ,　¥ <a href="http://www.ynswzyxy.com">云南商务职业学院</a> 昆明市 ,　¥ <a href="http://www.kmhvc.cn">昆明卫生职业学院</a>  ,　¥ <a href="http://www.FAFL.cn">云南外事外语职业学院</a> 昆明市 ,　¥ <a href="http://www.ynmhc.com">云南医药健康职业学院</a> 昆明市 ,　¥ <a href="http://ynlgzy.com">云南理工职业学院</a> 昆明市 </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>


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

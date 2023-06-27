# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """
<p>　<a href="http://www.gzu.edu.cn">贵州大学</a> <small>贵阳市 </small>,　<a href="http://www.gmc.edu.cn">贵州医科大学</a> <small>贵阳市 </small>,　<a href="http://www.zmu.edu.cn">遵义医科大学</a>,　<a href="http://www.gzy.edu.cn">贵州中医药大学</a> <small>贵阳市 </small>,　<a href="http://www.gznu.edu.cn">贵州师范大学</a> <small>贵阳市 </small>,　<a href="http://www.zync.edu.cn">遵义师范学院</a>,　<a href="http://www.gztrc.edu.cn">铜仁学院</a>,　<a href="http://www.qxntc.edu.cn">兴义民族师范学院</a> <small>黔西南州 </small>,　<a href="http://www.asu.edu.cn">安顺学院</a>,　<a href="http://www.gues.edu.cn">贵州工程应用技术学院</a> <small>毕节市 </small>,　<a title="新域名" href="http://www.kluniv.edu.cn">凯里学院</a> <small>黔东南州 </small>,　<a href="http://www.sgmtu.edu.cn">黔南民族师范学院</a>,　<a href="http://www.gufe.edu.cn">贵州财经大学</a> <small>贵阳市 </small>,　<a href="http://www.gzmu.edu.cn">贵州民族大学</a> <small>贵阳市 </small>,　<a href="http://www.gyu.cn">贵阳学院</a>,　<a href="http://www.lpssz.edu.cn">六盘水师范学院</a>,　<a href="http://www.gzcc.edu.cn">贵州商学院</a> <small>贵阳市 </small>,　<a href="http://gzpc.edu.cn">贵州警察学院</a> <small>🛂贵阳市 </small>,　<a href="http://www.gynvc.edu.cn">贵阳康养职业大学</a>,　<a href="http://www.gzhnc.edu.cn">贵州师范学院</a> <small>贵阳市 </small>,　<a href="http://www.git.edu.cn">贵州理工学院</a> <small>贵阳市 </small>,　¥ 贵州中医药大学<a href="http://www.gzyszxy.cn">时珍学院</a> <small>贵阳市 </small>,　¥ <a title="原贵州财经大学商务学院" href="http://qnxy.hope55.com">贵州黔南经济学院</a> <small>黔南州 </small>,　¥ <a href="http://www.gzucst.com">贵州黔南科技学院</a> <small>黔南州 </small>,　¥ <a title="新域名" href="http://www.gyiist.edu.cn">贵阳信息科技学院</a>,　¥ <a title="未查得网址">贵阳人文科技学院</a> 4152013651,　¥ 遵义医科大学<a href="http://mts.zmu.edu.cn">医学与科技学院</a>,　¥ 贵州医科大学<a title="贵医大无连接">神奇民族医药学院</a> 4152013676 <small>贵阳市 </small>,　¥ <a href="http://mtxy.edu.cn">茅台学院</a> <small>遵义市 </small>	<br><br>	高职大专48所：<small>　<a href="http://www.qnmc.cn">黔南民族医学高等专科学校</a>  ,　<a href="http://www.gzjtzy.net">贵州交通职业技术学院</a> 贵阳市 ,　<a href="http://www.gzhtzy.com">贵州航天职业技术学院</a> 遵义市 ,　<a href="http://www.gzeic.cn">贵州电子信息职业技术学院</a> 黔东南州 ,　<a href="http://www.asotc.cn">安顺职业技术学院</a>  ,　<a href="http://www.qdnpt.com">黔东南民族职业技术学院</a>  ,　<a href="http://www.qnzy.net">黔南民族职业技术学院</a>  ,　<a href="http://www.zyzy.gov.cn">遵义职业技术学院</a>  ,　<a href="http://www.gzky.edu.cn">贵州工业职业技术学院</a> 贵阳市 ,　<a href="http://www.csgedu.com">贵州电力职业技术学院</a> 贵阳市 ,　<a href="http://www.lpszy.cn">六盘水职业技术学院</a>  ,　<a href="http://www.trzy.cn">铜仁职业技术学院</a>  ,　<a href="http://www.qxnzy.net">黔西南民族职业技术学院</a>  ,　<a href="http://www.gzqy.cn">贵州轻工职业技术学院</a> 贵阳市 ,　<a href="http://www.zunyiyizhuan.com">遵义医药高等专科学校</a>  ,　<a href="http://www.gyvtc.cn">贵阳职业技术学院</a>  ,　<a href="http://www.gzbjzy.edu.cn">毕节职业技术学院</a>  ,　<a href="http://www.gzvti.com">贵州职业技术学院</a> 贵阳市 ,　<a href="http://www.gypec.edu.cn/list.jsp?itemId=2">贵阳幼儿师范高等专科学校</a>  ,　<a href="http://www.trpec.edu.cn">铜仁幼儿师范高等专科学校</a>  ,　<a href="http://www.qnyzh.cn">黔南民族幼儿师范高等专科学校</a>  ,　<a href="http://www.bijiemc.cn">毕节医学高等专科学校</a>  ,　<a href="http://www.gzjszy.cn">贵州建设职业技术学院</a> 贵阳市 ,　<a href="http://www.gzbjyz.com">毕节幼儿师范高等专科学校</a>  ,　<a href="http://www.gznyzyxy.cn">贵州农业职业学院</a> 贵阳市 ,　<a href="http://www.gzsdzy.cn">贵州水利水电职业技术学院</a> 贵阳市 ,　<a href="http://www.gzsdzy.cn">贵州电子商务职业技术学院</a> 贵阳市 ,　<a href="http://www.gzdzxy.cn">贵州电子科技职业学院</a> 贵阳市 ,　<a href="http://www.gzzbzy.cn">贵州装备制造职业学院</a> 贵阳市 ,　<a href="http://www.gzjkzy.edu.cn">贵州健康职业学院</a> 铜仁市 ,　<a href="http://www.gzspzy.cn">贵州食品工程职业学院</a> 贵阳市 ,　<a title="域名停服：gzjmzy.cn">贵州经贸职业技术学院</a> 4152014616 黔南州 ,　<a href="http://www.gznvc.com">贵州护理职业技术学院</a> 黔南州 ,　<a href="http://LPSyz.cn">六盘水幼儿师范高等专科学校</a>  ,　<a href="http://www.bjgzy.cn">毕节工业职业技术学院</a>  ,　<a href="http://www.gztcme.cn">贵州机电职业技术学院</a> 黔南州 ,　<a href="http://www.gzcjzyxy.cn">贵州财经职业学院</a> 贵阳市 ,　<a href="http://www.gzwhlyzy.cn/intro/7.html">贵州文化旅游职业学院</a> 贵阳市 ,　<a href="http://www.gzhkzy.cn">贵州航空职业技术学院</a> 贵阳市 ,　<a>贵州体育职业学院</a> 4152014799 贵阳市 ,　¥ <a href="http://www.gzcsxy.cn">贵州城市职业学院</a> 贵阳市 ,　¥ <a title="%Fx" href="http://www.forerunnercollege.com">贵州盛华职业学院</a> 黔南州 ,　¥ <a href="http://www.gzgsc.edu.cn">贵州工商职业学院</a> 贵阳市 ,　¥ <a href="http://www.gzieu.com">贵州工程职业学院</a> 铜仁市 ,　¥ <a href="http://www.gzgmzyxy.cn">贵州工贸职业学院</a> 毕节市 ,　¥ <a title="%Fx" href="http://www.gzyyxy.com">贵州应用技术职业学院</a> 黔南州 ,　¥ <a href="http://www.gzmhxy.cn">贵州民用航空职业学院</a> 安顺市 ,　¥ <a>贵州铜仁数据职业学院</a> 4152014800 铜仁市 </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>



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

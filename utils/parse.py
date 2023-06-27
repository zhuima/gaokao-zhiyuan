# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """<p>　<sup>教育部</sup>❕<a href="http://cqu.edu.cn"><b>重庆大学</b></a> <small>沙坪坝区 </small>,　<sup>教育部</sup>❕<a href="http://www.swu.edu.cn"><b>西南大学</b></a> <small>北碚区 </small>,　<a href="http://www.cqupt.edu.cn">重庆邮电大学</a> <small>南岸区 </small>,　<a href="http://www.cquc.edu.cn">重庆交通大学</a> <small>南岸区 </small>,　<a href="http://www.cqmu.edu.cn">重庆医科大学</a> <small>渝中区 </small>,　<a href="http://www.cqnu.edu.cn">重庆师范大学</a> <small>沙坪坝区 </small>,　<a title="网站504错误" href="http://www.cqwu.edu.cn">重庆文理学院</a> <small>永川区 </small>,　<a title="新域名" href="http://www.sanxiau.edu.cn">重庆三峡学院</a> <small>万州区 </small>,　<a href="http://www.yznu.cn">长江师范学院</a> <small>涪陵区 </small>,　<a title="网站支持22种外语！" href="http://www.sisu.edu.cn">四川外国语大学</a> <small>沙坪坝区 </small>,　<a href="http://www.swupl.edu.cn">西南政法大学</a> <small>⚖️沙坪坝区 </small>,　<a href="http://www.scfai.edu.cn">四川美术学院</a> <small>🎨沙坪坝区 </small>,　<a title="旧域名失效：www.cqust.cn" href="http://www.cqust.edu.cn">重庆科技学院</a> <small>沙坪坝区 </small>,　<a href="http://www.cqut.edu.cn">重庆理工大学</a> <small>巴南区/渝北区 </small>,　<a href="http://www.ctbu.edu.cn">重庆工商大学</a> <small>南岸区 </small>,　<a href="http://www.cqpc.edu.cn">重庆警察学院</a> <small>🛂沙坪坝区 </small>,　<a href="http://www.cque.edu.cn">重庆第二师范学院</a> <small>南岸区 </small>,　<a title="2023新本科" href="http://www.cqctcm.edu.cn">重庆中医药学院</a>,　¥ <a href="http://www.cqvtu.edu.cn">重庆机电职业技术大学</a> <small>璧山区 </small>,　¥ <a href="http://www.cqie.edu.cn">重庆工程学院</a> <small>巴南区 </small>,　¥ <a href="http://cqucc.cqu.edu.cn">重庆城市科技学院</a> <small>永川区 </small>,　¥ <a href="http://www.cqrk.edu.cn">重庆人文科技学院</a> <small>合川区 </small>,　¥ <a href="http://www.cqifs.edu.cn">重庆外语外事学院</a> <small>渝北区 </small>,　¥ <a href="http://www.ccibe.edu.cn">重庆对外经贸学院</a> <small>合川区 </small>,　¥ <a href="http://www.cfec.edu.cn">重庆财经学院</a> <small>巴南区 </small>,　¥ 重庆工商大学<a href="http://paisi.edu.cn">派斯学院</a> <small>合川区 </small>,　¥ <a title="号称ABC民办大学榜单第一" href="http://www.cqyti.com">重庆移通学院</a> <small>合川区 </small>	<br><br>	高职大专44所：<small>　<a href="http://www.cqsxedu.com">重庆三峡职业学院</a> 万州区 ,　<a href="http://www.cqepc.cn">重庆航天职业技术学院</a> 江北区 ,　<a href="http://www.cqepc.com.cn">重庆电力高等专科学校</a> 九龙坡区 ,　<a title="旧域名放弃www.cqipc.net" href="http://www.cqipc.edu.cn">重庆工业职业技术学院</a> 渝北区 ,　<a href="http://www.cqgmy.cn">重庆工贸职业技术学院</a> 涪陵区 ,　<a href="http://www.cqcet.com">重庆电子工程职业学院</a> 沙坪坝区 ,　<a href="http://www.cswu.cn">重庆城市管理职业学院</a>  ,　<a href="http://www.cqvie.edu.cn">重庆工程职业技术学院</a>  ,　<a href="http://www.cqcvc.com.cn">重庆城市职业学院</a>  ,　<a href="http://www.cqslzy.com">重庆水利电力职业技术学院</a>  ,　<a href="http://www.cqtbi.edu.cn">重庆工商职业学院</a>  ,　<a href="http://www.sxyyc.net">重庆三峡医药高等专科学校</a>  ,　<a href="http://www.cqyygz.com">重庆医药高等专科学校</a>  ,　<a href="http://www.cqqzy.cn">重庆青年职业技术学院</a>  ,　<a href="http://www.cqcfe.com">重庆财经职业学院</a>  ,　<a href="http://www.cctc.cq.cn">重庆建筑工程职业学院</a>  ,　<a href="http://www.cqswxy.cn/index.php">重庆商务职业学院</a>  ,　<a href="http://www.cqhgzy.com">重庆化工职业学院</a>  ,　<a href="http://www.cqvit.com">重庆旅游职业学院</a>  ,　<a title="网站维护：www.cqvist.net">重庆安全技术职业学院</a> 4150014365  ,　<a href="http://www.cqyz.edu.cn">重庆幼儿师范高等专科学校</a>  ,　<a href="http://www.cqca.edu.cn/index.php?c=category&amp;id=25">重庆文化艺术职业学院</a>  ,　<a title="铁路校、工业校" href="http://www.cqiivc.com">重庆工信职业学院</a>  ,　<a href="http://www.cq51.cn">重庆五一职业技术学院</a> 巴南区 ,　¥ <a href="http://www.cqhl.net.cn">重庆海联职业技术学院</a> 渝北区 ,　¥ <a href="http://www.cqeec.com">重庆信息技术职业学院</a> 万州区 ,　¥ <a href="http://cqcmxy.com:81/">重庆传媒职业学院</a> 铜梁区 ,　¥ <a href="http://cqrec.edu.cn">重庆建筑科技职业学院</a>  ,　¥ <a href="http://www.cqyyzy.com">重庆应用技术职业学院</a>  ,　¥ <a href="http://www.cqie.cn">重庆科创职业学院</a>  ,　¥ <a href="https://www.cqdxxy.edu.cn/">重庆电讯职业学院</a>  ,　¥ <a href="http://www.cqny.net">重庆能源职业学院</a>  ,　¥ <a href="http://www.cqjky.com">重庆交通职业学院</a>  ,　¥ <a href="http://www.cqgyzy.com">重庆公共运输职业学院</a>  ,　¥ <a href="http://www.cqysxy.com">重庆艺术工程职业学院</a>  ,　¥ <a title="网站502错误：www.cqivc.com">重庆轻工职业学院</a> 4150014368  ,　¥ <a href="http://www.cqtc.edu.cn">重庆电信职业学院</a>  ,　¥ <a href="http://www.cqvcet.com/channel_2.html">重庆经贸职业学院</a>  ,　¥ <a href="http://www.cqkjzyxy.com">重庆科技职业学院</a>  ,　¥ <a href="http://www.cqzhxy.cn">重庆资源与环境保护职业学院</a>  ,　¥ <a title="由重庆医科大学附属第一医院全额出资举办" href="http://www.cqnvc.com">重庆护理职业学院</a>  ,　¥ <a>重庆理工职业学院</a> 4150014725  ,　¥ <a href="http://www.cqai.vip">重庆智能工程职业学院</a>  ,　¥ <a href="http://www.cqhve.cn">重庆健康职业学院</a>  </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>"""


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

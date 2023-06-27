# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """<p>　<sup>教育部</sup>❕<a href="http://www.scu.edu.cn"><b>四川大学</b></a> <small>成都市 江姐纪念馆、<a href="https://wcums.scu.edu.cn/">华西医学中心</a>、<a href="https://ccsas.scu.edu.cn/">南亚研究中心</a></small>,　<sup>教育部</sup>❕<a href="http://www.swjtu.edu.cn"><b>西南交通大学</b></a> <small>成都市 </small>,　<sup>教育部</sup>❕<a href="http://www.uestc.edu.cn"><b>电子科技大学</b></a> <small>成都市 </small>,　<sup>交通部/民航局</sup>❕<a href="http://www.cafuc.edu.cn"><b>中国民用航空飞行学院</b></a> <small>德阳市 </small>,　<sup>教育部</sup>❕<a href="http://www.swufe.edu.cn"><b>西南财经大学</b></a> <small>成都市 </small>,　<sup>国家民委</sup>❕<a href="http://www.swun.edu.cn"><b>西南民族大学</b></a> <small>成都市 </small>,　<a href="http://www.swpu.edu.cn">西南石油大学</a> <small>成都市 </small>,　<a href="http://www.cdut.edu.cn">成都理工大学</a>,　<a href="http://www.swust.edu.cn">西南科技大学</a> <small>绵阳市 </small>,　<a href="http://www.cuit.edu.cn">成都信息工程大学</a>,　<a href="http://www.suse.edu.cn">四川轻化工大学</a> <small>自贡市 </small>,　<a href="http://www.xhu.edu.cn">西华大学</a> <small>成都市 </small>,　<a href="http://www.sicau.edu.cn">四川农业大学</a> <small>雅安市 </small>,　<a title="新域名" href="http://xcc.edu.cn">西昌学院</a> <small>凉山彝族自治州 </small>,　<a href="http://www.swmu.edu.cn">西南医科大学</a> <small>泸州市 </small>,　<a href="http://www.cdutcm.edu.cn">成都中医药大学</a>,　<a href="http://www.nsmc.edu.cn">川北医学院</a> <small>南充市 </small>,　<a href="http://www.sicnu.edu.cn">四川师范大学</a> <small>成都市 </small>,　<a href="http://www.cwnu.edu.cn">西华师范大学</a> <small>南充市 </small>,　<a href="http://www.mnu.cn">绵阳师范学院</a>,　<a href="http://www.njtc.edu.cn">内江师范学院</a>,　<a title="新域名" href="http://www.yibinu.edu.cn">宜宾学院</a>,　<a href="http://www.sasu.edu.cn">四川文理学院</a> <small>达州市 </small>,　<a href="http://www.abtu.edu.cn">阿坝师范学院</a>,　<a title="修正域名错误" href="http://www.lsnu.edu.cn">乐山师范学院</a>,　<a href="http://www.cdsu.edu.cn">成都体育学院</a> <small>🏃 </small>,　<a href="http://www.sccm.cn">四川音乐学院</a> <small>🎵成都市 </small>,　<a href="http://www.cdu.edu.cn">成都大学</a>,　<a href="http://www.cdtu.edu.cn">成都工业学院</a>,　<a href="http://www.pzhu.edu.cn">攀枝花学院</a>,　<a href="http://www.sctu.edu.cn">四川旅游学院</a> <small>成都市 </small>,　<a href="http://www.scun.edu.cn">四川民族学院</a> <small>甘孜藏族自治州 </small>,　<a href="http://www.scpolicec.edu.cn">四川警察学院</a> <small>🛂泸州市 </small>,　<a href="http://www.cmc.edu.cn">成都医学院</a>,　<a href="http://www.cdnu.edu.cn">成都师范学院</a>,　¥ <a title="旧域名停用：www.ccniit.com" href="http://nsu.edu.cn">成都东软学院</a>,　¥ <a href="http://www.cdau.edu.cn">成都艺术职业大学</a>,　¥ 电子科技大学<a title="修正域名错误" href="http://www.cduestc.cn">成都学院</a> <small>成都市 </small>,　¥ 成都理工大学<a href="http://www.cdutetc.cn">工程技术学院</a> <small>乐山市 </small>,　¥ <a href="http://www.scmc.edu.cn">四川传媒学院</a> <small>成都市 </small>,　¥ <a href="http://www.gingkoc.edu.cn">成都银杏酒店管理学院</a>,　¥ <a title="原四川师范大学文理学院" href="http://www.cdcas.edu.cn">成都文理学院</a>,　¥ <a href="http://www.stbu.edu.cn">四川工商学院</a> <small>成都市 </small>,　¥ 四川外国语大学<a href="http://cisisu.edu.cn">成都学院</a> <small>成都市 </small>,　¥ <a href="http://www.scit.edu.cn">四川工业科技学院</a> <small>德阳市 </small>,　¥ <a title="原四川大学锦城学院" href="http://www.scujcc.edu.cn">成都锦城学院</a>,　¥ 西南财经大学<a href="http://www.tf-swufe.net">天府学院</a> <small>绵阳市 </small>,　¥ 四川大学<a title="新域名" href="http://www.scujj.edu.cn">锦江学院</a> <small>眉山市 </small>,　¥ <a href="http://www.sca.edu.cn">四川文化艺术学院</a> <small>绵阳市 </small>,　¥ <a title="原西南科技大学城市学院" href="http://www.mycc.edu.cn">绵阳城市学院</a>,　¥ 西南交通大学<a href="http://www.swjtuhc.cn">希望学院</a> <small>南充市 </small>,　¥ <a href="http://www.scftvc.com">四川电影电视学院</a> <small>成都市 </small>,　¥ <a title="前身为北京吉利大学" href="http://cd.guc.edu.cn">吉利学院</a> <small>成都市 </small>	<br><br>	高职大专84所：<small>　<a href="http://www.cdtc.edu.cn">成都纺织高等专科学校</a>  ,　<a href="http://www.cavtc.net">成都航空职业技术学院</a>  ,　<a href="http://www.kc.sc.sgcc.com.cn/www">四川电力职业技术学院</a> 成都市 ,　<a href="http://www.cdvtc.com">成都职业技术学院</a>  ,　<a href="http://www.sccvtc.cn">四川化工职业技术学院</a> 泸州市 ,　<a href="http://www.swcvc.net.cn">四川水利职业技术学院</a> 成都市 ,　<a href="http://www.nczy.com">南充职业技术学院</a>  ,　<a href="http://www.njvtc.cn">内江职业技术学院</a>  ,　<a href="http://www.sacvt.com">四川航天职业技术学院</a> 成都市 ,　<a href="http://www.sptpc.com">四川邮电职业技术学院</a> 成都市 ,　<a href="http://www.scemi.com">四川机电职业技术学院</a> 攀枝花市 ,　<a href="http://www.myvtc.edu.cn">绵阳职业技术学院</a>  ,　<a href="http://www.svtcc.edu.cn">四川交通职业技术学院</a> 成都市 ,　<a href="http://www.sctbc.net">四川工商职业技术学院</a> 成都市 ,　<a href="http://www.scetc.net">四川工程职业技术学院</a> 德阳市 ,　<a href="http://www.scatc.net">四川建筑职业技术学院</a> 德阳市 ,　<a href="http://www.dzzjy.com">达州职业技术学院</a>  ,　<a href="http://www.cdnkxy.com">成都农业科技职业学院</a>  ,　<a href="http://www.ybzy.cn">宜宾职业技术学院</a>  ,　<a href="http://www.lzy.edu.cn">泸州职业技术学院</a>  ,　<a href="http://www.msvtc.net">眉山职业技术学院</a>  ,　<a href="http://www.scvtc.com">四川职业技术学院</a> 遂宁市 ,　<a href="http://www.lszyxy.com">乐山职业技术学院</a>  ,　<a href="http://www.yazjy.com">雅安职业技术学院</a>  ,　<a href="http://www.scsw.net.cn">四川商务职业学院</a> 成都市 ,　<a href="http://www.sjpopc.net">四川司法警官职业学院</a> 🛂德阳市 ,　<a href="http://www.gavtc.cn">广安职业技术学院</a>  ,　<a href="http://www.scitc.com.cn">四川信息职业技术学院</a> 广元市 ,　<a href="http://www.scrc.edu.cn">四川铁道职业学院</a> 成都市 ,　<a href="http://www.scapi.cn">四川艺术职业学院</a> 成都市 ,　<a href="http://www.scctcm.cn">四川中医药高等专科学校</a> 绵阳市 ,　<a href="http://www.scvcci.cn">四川文化产业职业学院</a> 成都市 ,　<a href="http://www.scpcfe.cn">四川财经职业学院</a> 成都市 ,　<a href="http://www.scyesz.com">四川幼儿师范高等专科学校</a> 绵阳市 ,　<a title="www.cbyz.edu.cn">川北幼儿师范高等专科学校</a> 4151014393 广元市 ,　<a title="www.svchr.edu.cn">四川卫生康复职业学院</a> 4151014409 自贡市 ,　<a title="www.cnyz.edu.cn">川南幼儿师范高等专科学校</a> 4151014496 内江市 ,　<a href="http://www.cnsnvc.edu.cn">四川护理职业学院</a> 德阳市 ,　<a href="http://www.cdivtc.com">成都工业职业技术学院</a>  ,　<a href="http://www.cdgmxy.edu.cn">成都工贸职业技术学院</a>  ,　<a href="http://www.xcmzyz.edu.cn">西昌民族幼儿师范高等专科学校</a> 凉山彝族自治州 ,　<a href="http://www.abvc.edu.cn">阿坝职业学院</a>  ,　<a href="http://dzcmc.com">达州中医药职业学院</a>  ,　<a href="http://www.njnhvc.edu.cn">内江卫生与健康职业学院</a>  ,　<a href="http://www.ncvcct.com">南充文化旅游职业学院</a>  ,　<a href="http://www.scgzzyxy.com">甘孜职业学院</a>  ,　<a href="http://www.scsc.edu.cn">四川体育职业学院</a> 🏃成都市 ,　¥ <a href="http://sctianyi.net">民办四川天一学院</a> 成都市 ,　¥ <a href="http://www.scetop.com">四川托普信息技术职业学院</a> 成都市 ,　¥ <a href="http://pivotpoint.edu.cn">四川国际标榜职业学院</a> 成都市 ,　¥ <a href="http://www.svccc.net">四川文化传媒职业学院</a> 成都市 ,　¥ <a href="http://www.schxmvc.com">四川华新现代职业学院</a> 成都市 ,　¥ <a href="http://www.scstc.cn">四川科技职业学院</a> 成都市 ,　¥ <a href="http://www.scuvc.com">四川城市职业学院</a> 成都市 ,　¥ <a href="http://www.scmvc.cn">四川现代职业学院</a> 成都市 ,　¥ <a href="http://www.sccvc.com">四川长江职业学院</a> 成都市 ,　¥ <a href="http://www.scshpc.com">四川三河职业学院</a> 泸州市 ,　¥ <a href="http://www.scavtc.com">四川汽车职业技术学院</a> 绵阳市 ,　¥ <a href="http://bzvtc.edu.cn">巴中职业技术学院</a>  ,　¥ <a href="http://www.qicheedu.com">四川希望汽车职业学院</a> 资阳市 ,　¥ <a href="http://www.scemvtc.com">四川电子机械职业技术学院</a> 绵阳市 ,　¥ <a href="http://www.scwxzyxy.cn">四川文轩职业学院</a> 成都市 ,　¥ <a href="http://www.xnhkxy.edu.cn">四川西南航空职业学院</a> 成都市 ,　¥ <a href="http://www.scasc.cn">四川应用技术职业学院</a> 凉山彝族自治州 ,　¥ <a title="全省最大中医药博物馆" href="http://www.msykxy.cn">眉山药科职业学院</a>  ,　¥ <a href="http://www.tficedu.com">天府新区信息职业学院</a> 眉山市 ,　¥ <a href="http://www.dcurt.cn">德阳城市轨道交通职业学院</a>  ,　¥ <a href="http://www.dvctt.com">德阳科贸职业学院</a>  ,　¥ <a href="http://jyccc.cn">江阳城建职业学院</a> 泸州市 ,　¥ <a href="http://www.tfhk.edu.cn">天府新区航空旅游职业学院</a> 眉山市 ,　¥ <a title="2018年创建" href="http://www.ausedu.cn">天府新区通用航空职业学院</a> 眉山市 ,　¥ <a href="http://www.nstc.edu.cn">南充科技职业学院</a>  ,　¥ <a href="http://www.pzhpxzyxy.com">攀枝花攀西职业学院</a>  ,　¥ <a title="中国牙谷？" href="http://zykqxy.com">资阳口腔职业学院</a>  ,　¥ <a href="https://117.176.18.152">资阳环境科技职业学院</a>  ,　¥ <a href="http://ncdyxy.com">南充电影工业职业学院</a>  ,　¥ <a title="VFCM" href="http://www.topflying.com.cn/Page_1478.html">绵阳飞行职业学院</a>  ,　¥ <a href="http://dynky.cn">德阳农业科技职业学院</a>  ,　¥ <a href="http://www.lzylqx.cn">泸州医疗器械职业学院</a>  ,　¥ <a href="http://zgzyjsxy.com/xyg/xyjj.html">自贡职业技术学院</a>  ,　¥ <a title="域名失效：nivtc.com">广元中核职业技术学院</a> 4251050881  ,　¥ <a>遂宁能源职业学院</a> 4151014834  ,　¥ <a>遂宁工程职业学院</a> 4151014835  ,　¥ <a>遂宁职业学院</a> 4151014836  </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>"""


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

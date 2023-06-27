# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """<p>　<a href="http://www.gxu.edu.cn">广西大学</a> <small>南宁市 </small>,　<a href="http://www.gxust.edu.cn">广西科技大学</a> <small>柳州市 </small>,　<a href="http://www.gliet.edu.cn">桂林电子科技大学</a>,　<a href="http://www.glite.edu.cn">桂林理工大学</a>,　<a href="http://www.gxmu.edu.cn">广西医科大学</a> <small>南宁市 </small>,　<a title="修正" href="http://www.ymun.edu.cn">右江民族医学院</a> <small>百色市 </small>,　<a href="http://www.gxtcmu.edu.cn">广西中医药大学</a> <small>南宁市 </small>,　<a href="http://www.glmc.edu.cn">桂林医学院</a>,　<a href="http://www.gxnu.edu.cn">广西师范大学</a> <small>桂林市 </small>,　<a href="http://www.nnnu.edu.cn">南宁师范大学</a>,　<a title="网站疑似故障？" href="http://www.gxnun.edu.cn">广西民族师范学院</a> <small>崇左市 </small>,　<a href="http://www.hcnu.edu.cn">河池学院</a>,　<a href="http://www.ylu.edu.cn">玉林师范学院</a>,　<a href="http://www.gxau.edu.cn">广西艺术学院</a> <small>南宁市 </small>,　<a href="http://www.gxun.edu.cn">广西民族大学</a> <small>南宁市 </small>,　<a title="网站疑似故障？" href="http://www.bsuc.edu.cn">百色学院</a>,　<a href="http://www.gxuwz.edu.cn">梧州学院</a>,　<a href="http://www.gxstnu.edu.cn">广西科技师范学院</a> <small>来宾市 </small>,　<a title="新域名" href="http://www.gxufe.edu.cn">广西财经学院</a> <small>南宁市 </small>,　<a href="http://www.bbgu.edu.cn">北部湾大学</a> <small>钦州市 </small>,　<a href="http://www.guat.edu.cn">桂林航天工业学院</a>,　<a href="http://www.gltu.edu.cn">桂林旅游学院</a>,　<a title="网站维护中" href="http://www.hzxy.edu.cn">贺州学院</a>,　<a href="http://www.gxjcxy.com">广西警察学院</a> <small>🛂南宁市 </small>,　<a href="http://www.gxnzd.edu.cn">广西农业职业技术大学</a> <small>南宁市 </small>,　<a href="http://www.gxvnu.edu.cn">广西职业师范学院</a> <small>南宁市 </small>,　¥ <a title="网站疑似故障？" href="http://nnxy.cn">南宁学院</a>,　¥ <a href="http://www.sszss.com">北海艺术设计学院</a>,　¥ <a href="http://www.lzhit.edu.cn">柳州工学院</a>,　¥ 广西民族大学<a href="http://xshxy.gxun.edu.cn">相思湖学院</a> <small>南宁市 </small>,　¥ <a title="原广西师范大学漓江学院" href="http://www.gxljcollege.cn">桂林学院</a>,　¥ 南宁师范大学<a href="http://www.gxsy.edu.cn">师园学院</a>,　¥ 广西中医药大学<a title="Science？" href="http://www.gxzyxysy.com">赛恩斯新医药学院</a> <small>南宁市 </small>,　¥ <a href="http://guit.edu.cn">桂林信息科技学院</a>,　¥ <a title="原桂林理工大学博文管理学院" href="http://web.bwgl.cn">南宁理工学院</a> <small>桂林市 </small>,　¥ <a title="新域名" href="http://gxufl.edu.cn">广西外国语学院</a> <small>南宁市 </small>,　¥ 北京航空航天大学<a title="限校内访问" href="http://bhc.buaa.edu.cn">北海学院</a> <small>北海市 </small>,　¥ <a href="http://www.gxcvuedu.com">广西城市职业大学</a> <small>崇左市 </small>	<br><br>	高职大专49所：<small>　¥ <a href="http://www.peixianedu.cn">广西培贤国际职业学院</a> 百色市 ,　<a href="http://www.gxcme.edu.cn">广西机电职业技术学院</a> 南宁市 ,　<a href="http://www.gxtznn.com">广西体育高等专科学校</a> 🏃南宁市 ,　<a href="http://www.ncvt.net">南宁职业技术学院</a>  ,　<a href="http://www.gxsdxy.cn">广西水利电力职业技术学院</a> 南宁市 ,　<a href="http://www.glnc.edu.cn">桂林师范高等专科学校</a>  ,　<a href="http://www.gxzjy.com">广西职业技术学院</a> 南宁市 ,　<a href="http://www.lzzy.net">柳州职业技术学院</a>  ,　<a href="http://www.gxstzy.cn">广西生态工程职业技术学院</a> 柳州市 ,　<a href="http://www.gxjzy.com">广西交通职业技术学院</a> 南宁市 ,　<a href="http://www.gxic.net">广西工业职业技术学院</a> 南宁市 ,　<a href="http://www.gxibvc.net">广西国际商务职业技术学院</a> 南宁市 ,　<a href="http://www.lztdzy.com">柳州铁道职业技术学院</a>  ,　<a href="http://www.gxjsxy.cn">广西建设职业技术学院</a> 南宁市 ,　<a href="http://www.gxxd.net.cn">广西现代职业技术学院</a> 河池市 ,　<a href="http://www.bhzyxy.net">北海职业学院</a>  ,　<a href="http://www.gxjmzy.com">广西经贸职业技术学院</a> 南宁市 ,　<a href="http://www.gxgsxy.com">广西工商职业技术学院</a> 南宁市 ,　<a href="http://www.gxdlxy.com">广西电力职业技术学院</a> 南宁市 ,　<a href="http://www.lcvc.cn">柳州城市职业学院</a>  ,　<a href="http://www.bszyxy.cn">百色职业学院</a>  ,　<a href="http://www.wzzyedu.com">梧州职业学院</a>  ,　<a href="http://www.gxyesf.com">广西幼儿师范高等专科学校</a> 南宁市 ,　<a href="http://www.gxwgy.com.cn">广西卫生职业技术学院</a> 南宁市 ,　<a title="广西银行学校" href="http://www.gxjrxy.com">广西金融职业技术学院</a> 南宁市 ,　<a href="http://www.gxaqzy.cn/ltgk/xyjj.html">广西安全工程职业技术学院</a> 南宁市 ,　<a href="http://www.gxnrvtc.edu.cn">广西自然资源职业技术学院</a> 崇左市 ,　<a href="http://www.qzyz.edu.cn">钦州幼儿师范高等专科学校</a>  ,　<a>广西制造工程职业技术学院</a> 4145014722 南宁市 <a href="http://www.maiyuesoft.com/zbh/xygk/xxjj.htm">企业信息</a>,　<a href="http://gxlvtc.edu.cn">广西物流职业技术学院</a> 贵港市 ,　<a href="http://www.fcgzy.edu.cn">防城港职业技术学院</a>  ,　<a title="广西开放大学" href="http://www.gxuie.cn">广西信息职业技术学院</a> 南宁市 ,　<a href="http://www.gxngy.cn">广西农业工程职业技术学院</a> 崇左市 ,　<a href="http://www.gxczyesf.com">崇左幼儿师范高等专科学校</a>  ,　<a>广西质量工程职业技术学院</a> 4145014821 南宁市 ,　¥ <a href="http://www.glhic.com">桂林生命与健康职业技术学院</a>  ,　¥ <a href="http://www.guolianweb.com">桂林山水职业学院</a>  ,　¥ <a href="http://www.gxart.cn">广西演艺职业学院</a> 南宁市 ,　¥ <a href="http://www.tic-gx.com">广西英华国际职业学院</a> 钦州市 ,　¥ <a href="http://www.gxgcedu.com">广西工程职业学院</a> 百色市 ,　¥ <a href="http://www.gxlgxy.com">广西理工职业技术学院</a> 崇左市 ,　¥ <a href="http://www.gxevc.com">广西经济职业学院</a> 南宁市 ,　¥ <a href="http://www.gxkjzy.com">广西科技职业学院</a> 崇左市 ,　¥ <a>广西中远职业学院</a> 4145014546 崇左市 ,　¥ <a href="http://www.yczyxy-edu.cn">玉柴职业技术学院</a> 玉林市 ,　¥ <a href="http://www.gxltu.edu.cn">广西蓝天航空职业学院</a> 来宾市 ,　¥ <a title="旧域名停用：www.wuzmc.edu.cn" href="http://www.gxwzyz.com">梧州医学高等专科学校</a>  ,　¥ <a title="%Fx" href="http://www.bhkyxy.com">北海康养职业学院</a>  ,　¥ <a>桂林信息工程职业学院</a> 4145014822  </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>"""


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

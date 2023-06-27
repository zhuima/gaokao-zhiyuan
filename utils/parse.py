# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json

html_str = """
<p>　<a href="http://www.xju.edu.cn">新疆大学</a> <small>乌鲁木齐市 </small>,　<a title="兵团主管" href="http://www.taru.edu.cn">塔里木大学</a> <small>阿拉尔市 </small>,　<a href="http://www.xjau.edu.cn">新疆农业大学</a> <small>乌鲁木齐市 </small>,　<a title="兵团主管" href="http://www.shzu.edu.cn">石河子大学</a>,　<a href="http://www.xjmu.edu.cn">新疆医科大学</a> <small>乌鲁木齐市 </small>,　<a href="http://www.xjnu.edu.cn">新疆师范大学</a> <small>乌鲁木齐市 </small>,　<a href="http://www.ksu.edu.cn">喀什大学</a>,　<a href="http://www.ylnu.edu.cn">伊犁师范大学</a>,　<a href="http://www.xjufe.edu.cn">新疆财经大学</a> <small>乌鲁木齐市 </small>,　<a href="http://www.xjart.edu.cn">新疆艺术学院</a> <small>乌鲁木齐市 </small>,　<a href="http://www.xjie.edu.cn">新疆工程学院</a> <small>乌鲁木齐市 </small>,　<a href="http://219.247.64.111/">昌吉学院</a>,　<a title="域名失效：www.xjpcedu.cn">新疆警察学院</a> 4165012734 <small>🛂乌鲁木齐市 </small>,　<a href="https://xjit.edu.cn/">新疆理工学院</a> <small>阿克苏地区 </small>,　<a href="http://www.xjsmc.edu.cn">新疆第二医学院</a> <small>克拉玛依市 </small>,　<a href="http://www.xjust.edu.cn">新疆科技学院</a> <small>巴音郭楞蒙古自治州 </small>,　<a title="兵团主管" href="http://www.xjzfu.edu.cn">新疆政法学院</a> <small>⚖️图木舒克市 </small>,　¥ 新疆农业大学<a title="域名疑似停服：www.xjstc.net">科学技术学院</a> 4165013559 <small>乌鲁木齐市 </small>,　¥ <a href="http://www.xjtsxy.cn">新疆天山职业技术大学</a> <small>乌鲁木齐市 </small>	<br><br>	高职大专43所：<small>　<a href="http://www.htszedu.cn">和田师范专科学校</a>  ,　<a href="http://www.xjnzy.edu.cn">新疆农业职业技术学院</a> 昌吉回族自治州 ,　<a href="http://www.uvu.edu.cn">乌鲁木齐职业大学</a>  ,　<a href="http://www.xjumc.cn">新疆维吾尔医学专科学校</a> 和田地区 ,　<a href="http://www.kzjsxy.net">克拉玛依职业技术学院</a>  ,　<a href="http://www.xjjd.com.cn">新疆机电职业技术学院</a> 乌鲁木齐市 ,　<a href="http://www.xjqg.edu.cn">新疆轻工职业技术学院</a> 乌鲁木齐市 ,　<a href="http://www.cjpt.cn">昌吉职业技术学院</a>  ,　<a href="http://www.ylzyjs.cn">伊犁职业技术学院</a>  ,　<a href="http://www.akszy.com">阿克苏职业技术学院</a>  ,　<a href="http://www.xjbyxy.cn">巴音郭楞职业技术学院</a>  ,　<a href="http://www.xjjszy.net/">新疆建设职业技术学院</a> 乌鲁木齐市 ,　<a href="http://www.xjjtedu.com">新疆交通职业技术学院</a> 乌鲁木齐市 ,　<a title="兵团主管" href="http://www.xjshzzy.com">新疆石河子职业技术学院</a> 石河子市 ,　<a href="http://www.xjvu.edu.cn">新疆职业大学</a> 乌鲁木齐市 ,　<a>新疆体育职业技术学院</a> 4165014416 🏃乌鲁木齐市 ,　<a href="http://www.xjyyedu.cn">新疆应用职业技术学院</a> 伊犁哈萨克自治州 ,　<a title="新疆教育学院" href="http://www.xjei.edu.cn">新疆师范高等专科学校</a> 乌鲁木齐市 ,　<a href="http://www.xjtzy.net">新疆铁道职业技术学院</a> 乌鲁木齐市 ,　<a title="兵团主管" href="http://btc.edu.cn">新疆生产建设兵团兴新职业技术学院</a> 乌鲁木齐市 ,　<a href="http://www.hmzyedu.cn">哈密职业技术学院</a>  ,　<a title="域名失效：www.tlfzj.com">吐鲁番职业技术学院</a> 4165014585  ,　<a title="网站维护中" href="http://www.betltc.cn">博尔塔拉职业技术学院</a>  ,　<a href="http://www.htpt.edu.cn">和田职业技术学院</a>  ,　<a title="兵团主管" href="http://www.shzvce.cn">石河子工程职业技术学院</a>  ,　<a>喀什职业技术学院</a> 4165014677  ,　<a href="http://www.kzvtc.edu.cn">克孜勒苏职业技术学院</a> 克州 ,　<a href="http://www.altzyxy.com">阿勒泰职业技术学院</a>  ,　<a>塔城职业技术学院</a> 4165014740  ,　<a title="兵团主管" href="http://1.13.3.19/">塔里木职业技术学院</a> 阿拉尔市 ,　<a>新疆工业职业技术学院</a> 4265051060 乌鲁木齐市 ,　<a title="兵团主管" href="http://www.tmgxy.edu.cn">铁门关职业技术学院</a>  ,　<a>新疆司法警官职业学院</a> 4165014805 乌鲁木齐市 ,　<a>阿克苏工业职业技术学院</a> 4165014806  ,　<a>喀什理工职业技术学院</a> 4165014824  ,　<a>图木舒克职业技术学院</a> 4165014825  ,　<a>可克达拉职业技术学院</a> 4165014826  ,　<a>新星职业技术学院</a> 4165014827  ,　<a>昆玉职业技术学院</a> 4165014828  ,　¥ <a href="http://www.xjnyedu.com">新疆能源职业技术学院</a> 乌鲁木齐市 ,　¥ <a title="域名失效：www.xjxiandai.net">新疆现代职业技术学院</a> 4165013726 乌鲁木齐市 ,　¥ <a title="中文域名！" href="http://新疆科技职业技术学院.com">新疆科技职业技术学院</a> 五家渠市 ,　¥ <a href="http://www.kxedu.net">新疆科信职业技术学院</a> 乌鲁木齐市 </small>　　<a href="#mulu" target="_top" title="回各省索引">▲</a></p>

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

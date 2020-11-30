# MOOCCube 数据集说明

[data source](http://moocdata.cn/data/MOOCCube)

**Notice 以下文件均为jsonl格式**

## Meaning of fields
### entities
#### concept.json
字段名  | 说明
------  | ----
id      | 名称
name    | 概念名称
en      | 概念英文名
explanation | 所属学科，定义，见载

* Example

id|name|en|explanation
---|---|---|---|
K_《三国史记》_世界历史|《三国史记》|History of Three States in Ancient Korea|学科：世界历史_古代中世纪_东北亚 定义：朝鲜现存的最古史书，1145年高丽王朝的学者金富轼(1075-1151)用古汉语撰成，记述了新罗、高句丽和百济三国的史事。 见载：《世界历史名词》第一版
K_《三国遗事》_世界历史|《三国遗事》|San Guo Yi Shi|学科：世界历史_古代中世纪_东北亚 定义：朝鲜古书名称，为新罗、百济、高句丽三国遗事逸闻的汇集，晚于《三国史记》，二者合成朝鲜古代史书的双璧。 见载：《世界历史名词》第一版

#### course.json
字段名  | 说明
------  | ----
id      | 课程id
name    | 课程名称
prerequisites | 先修知识
about   | 详细介绍(包含课程目录)
core_id | 课程id
video_order | 视频的顺序(视频id号)
display_name | 视频名称(同上一行的视频id对应)
charpter    | ？

* Example

id|name|prerequisites|about|core_id|video_order|display_name|charpter
---|---|---|---|---|---|---|---
C_course-v1:TsinghuaX+THESIS2015X+2015_T1|2015年清华大学研究生学位论文答辩（二）|无先修要求|\<p>学位论文答辩环节是研究生培养的重要环节，为了充分发挥该环节的育人作用，搭建学术交流的平台，进一步保障和提高研究生培养质量，清华大学研究生院从2014年开始，从申请学位的博士、硕士研究生中选取了部分具有代表性的学位论文答辩进行录像，并首次将答辩视频上传学堂在线，获得了社会各界的认可和积极反响。\</p>\<p>2015年，清华大学将继续这一形式，遴选不同专业的博士、硕士研究生的学位论文答辩视频，继续以MOOC形式共享呈现给大家，以使更多的人能够分享这些资源，搭建更为广阔的学术交流平台。\</p><p>如果这些视频能对您的学术研究有所帮助和启发，则是我们十分期待并愿意看到的事。\</p>|C_course-v1:TsinghuaX+THESIS2015X+2015_T1|["V_de0371575a9f4b5391c89ad16d68b5c2","V_d632034fd0b043aea25712ab5d7e18ac","V_054ef8aa6574419484e0d2f48fe37247","V_f36405771d9b49c09267a21619b7b8c4","V_3d91b580eb7949419f6aca03c9a6fca1","V_2c3ff8579bce4b448ef0829085c827f7","V_e834c537dbc14e858ea3afc5f05d8f2b","V_2b052748d7854fe29ba48b0b8d693990","V_5a7f68c8c37f4172bb687f47838a6ef6","V_7ee887a937414e5888f9f0a785535845","V_316c645ac100495bbd5c9b0292e5a31f","V_dfd189596d3448bd814bc16bb61436cc","V_dbab68ccabbd42e3add9229b86baaad9","V_642849b5634a4005ae4410daae8e9d36","V_4daf97bf54a74cc8a6d0e0f115bb91f9",......],| ["答辩陈述","答辩陈述","问答及答辩结果","答辩陈述","问答及答辩结果","答辩陈述","问答及答辩结果","答辩陈述","问答及答辩结果","导师点评","个人感言","答辩陈述","问答及答辩结果"......]| ["01.01.03.01","01.02.03.01","01.02.04.01","01.03.03.01","01.03.04.01","01.04.03.01","01.04.04.01","01.05.03.01","01.05.04.01","01.05.05.01","01.05.06.01","01.06.03.01","01.06.04.01","01.07.03.01","01.07.04.01","01.07.05.01","01.07.06.01","02.01.03.01","02.01.04.01","02.02.03.01","02.02.04.01","02.02.05.01","02.02.06.01","02.03.03.01","02.03.04.01","02.04.03.01","02.04.04.01",......]

*notice：字段video_order、display_name和charpter因内容过长不便于显示，用......代替*

#### paper.json
字段名 | 说明
------ | ----
id      | paperid
name    | paper名称
abstract | paper摘要
authors | 作者信息，包含作者id和作者名(id, name)
doi     | ?
lang    | 语言
num_citation   | 引用次数
pages   | ？
pdf     | ？
sourcetype | ？
title   | paper题目
urls    |
venue   | ？
year    | 发表时间

* Example
  
id|name|abstract|authors|doi|lang|num_citation|pages|pdf|sourcetype|title|urls|venue|year
---|---|---|---|---|---|---|---|---|---|---|---|---|---
P_53e9a3c7b7602d9702cd6212| | |[{"id": "53f42758dabfaeb22f3ca5f6","name": "Sf Altschul"},{"id": "53f431fbdabfaec09f14e89e","name": "Tl Madden"},{"id": "53f4d495dabfaef34bf809be","name": "Aa Schaffer"},{"id": "53f66247dabfaebd90189718","name": "J Zhang"},{"id": "5604f90345cedb339650b96e","name": "Z Zhang"},{"id": "5448c256dabfae87b7e74d80","name": "W Miller"},{"id": "53f438c8dabfaee43ec467f1","name": "Dj Lipman"}]| |en|66779| | |publication|Gapped BLAST and PSI-BLAST: a new generation of protein database search pro-grams| |{"info": {"name": "Nucleic Acids Research"},"issue": "","volume": ""}| 1992
P_53e9aa48b7602d97033b7da1| |We present Greedy Perimeter Stateless Routing (GPSR), a novel routing protocol for wireless datagram networks that uses the positions of routers and a packet's destination to make packet forwarding decisions. GPSR makes greedy forwarding decisions using only information about a router's immediate neighbors in the network topology. When a packet reaches a region where greedy forwarding is impossible, the algorithm recovers by routing around the perimeter of the region. By keeping state only about the local topology, GPSR scales better in per-router state than shortest-path and ad-hoc routing protocols as the number of network destinations increases. Under mobility's frequent topology changes, GPSR can use local topology information to find correct new routes quickly. We describe the GPSR protocol, and use extensive simulation of mobile wireless networks to compare its performance with that of Dynamic Source Routing. Our simulations demonstrate GPSR's scalability on densely deployed wireless networks.|{"id": "53f43a9fdabfaee4dc7aac6d","name": "Brad Karp"},{"id": "53f46e93dabfaee4dc86e94b","name": "H. T. Kung"}|10.1145/345910.345953|en|9390|{"end": "254","start": "243"}|//static.aminer.org/pdf/PDF/000/505/674/gpsr_greedy_perimeter_stateless_routing_for_wireless_networks.pdf|publication|GPSR: greedy perimeter stateless routing for wireless networks|["http://dx.doi.org/10.1145/345910.345953","http://doi.acm.org/10.1145/345910.345953","https://static.aminer.org/pdf/20170130/pdfs/index.txt"]|{"info": {"name": "MobiCom"},"issue": "","volume": ""}|2000

#### school.json
字段名 | 说明
------ | ----
id      | 学校英文缩写
name    | 学校中文名全称
about   | 简介

* Example
  
id|name|about
---|---|---
S_UESTC|电子科技大学|电子科技大学（University of Electronic Science and Technology of China）坐落于四川省会成都市，直属中华人民共和国教育部，由教育部、工业和信息化部、四川省和成都市共建。位列“世界一流大学和一流学科”、“985工程”、“211工程”，入选2011计划、111计划、卓越工程师教育培养计划、国家建设高水平大学公派研究生项目、中国政府奖学金来华留学生接收院校、全国深化创新创业教育改革示范高校，两电一邮成员。是一所完整覆盖整个电子类学科，以电子信息科学技术为核心，以工为主，理工渗透，理、工、管、文、医协调发展的多科性研究型全国重点大学，被誉为“中国电子类院校的排头兵”。
S_ustc|中国科学技术大学|中国科学技术大学（University of Science and Technology of China），简称“中国科大”，位于安徽省合肥市，由中国科学院直属，中央直管副部级建制，位列“双一流”、“211工程”、“985工程”，入选“珠峰计划”、“111计划”、“2011计划”、“中国科学院知识创新工程”


#### teacher.json
字段名 | 说明
------ | ----
id      | 老师姓名，例如：T_方维奇
name    | 老师姓名，例如：方维奇
about   | 老师简介

* Example
  
id|name|about
---|---|---
T_陈薇|T_陈薇|博士，教授，现任世界中医药学会联合会循证中医药再评价专家委员会副主委，中国中西医结合学会循证医学专业委员会委员, 中国医师协会循证医学专业委员会委员，中华中医药学会亚健康分会及精准医学分会委员，中国老年学学会医药保健康复委员会委员，国际Cochrane协作组织‘病人报告结局(PRO)’方法组、‘神经肌肉疾病’、‘肝胆疾病’协作评价小组成员。多个国际杂志特约审稿专家。主要从事循证医学及临床科研方法学研究。主持国家自然科学基金1项，主持北京市青年骨干个人项目1项，参与国家级科研课题5项，省部级科研课题4项。共发表专业学术论文40篇。发表SCI收录英文论文21篇，国内核心期刊专业学术论文17篇。参与编写专著11部。
T_耿华|耿华|博士，副教授。2008年于清华大学自动化系获博士学位，2008-2010，在加拿大Ryerson大学LEDAR实验室从事博士后研究工作，2010至今，在清华大学自动化系工作，主讲《模拟电子技术基础》。主要从事电力电子及新能源发电技术的相关研究，在本领域的权威性杂志发表学术论文60余篇，获中国电源学会2013“青年奖”，入选2013北京高等学校青年英才计划。

#### user.json
字段名 | 说明
------ | ----
id      | 用户ID
name    | 用户名
course_order    | 课程学习顺序
enroll_time     | 课程的注册时间，与course_order对应


* Example

id|name|course_order|enroll_time
---|---|---|---
U_7001215|李喜锋|["C_course-v1:TsinghuaX+00740043_2x_2015_T2+sp","C_course-v1:TsinghuaX+30240184+sp","C_course-v1:TsinghuaX+00740043X_2015_T2+sp","C_course-v1:TsinghuaX+10421094X_2015_2+sp","C_course-v1:TsinghuaX+30240184_2X+sp"]|["2017-05-01 11:07:53","2017-05-17 10:07:17","2017-05-01 11:09:21","2017-11-30 14:14:40","2017-08-18 21:21:32"]
U_7193771|阙俊语| ["C_course-v1:TsinghuaX+30240243X+sp","C_course-v1:NJU+C1026+2016_T2"]|["2017-08-01 22:13:58","2017-07-31 22:37:50"]

#### vedio.json

字段名 | 说明
------ | ----
id      | 视频ID
name    | 视屏名称
start   | ?
end     | ?
text    | 视频字幕

* Example

id|name|start|end|text
---|---|---|---|---
V_c20d824ce5f440b4bfc7ac7c4146735a|4-1协商解除劳动合同的操作|[39460,43010,45060,48690,50780,53170,55460,61780,64720,69940,74220,76980,88340,89460,92500,98880,103730,106770,......]|[43010,45060,48690,50780,53170,55460,61780,64720,69940,73930,76980,80920,89460,92500,......]|["刘老师，解除劳动合同是在劳动合同订立后","又没有全部履行完毕以前","由于某种原因导致劳动合同一方或双方当事人","提前消灭劳动关系的法律行为","那协商解除劳动合同有什么特点呢","恩，协商解除劳动合同","就是指用人单位和劳动者在完全自愿的情况下，经过平等协商","达成一致提前终止劳动合同","那么这种方式适用的范围广、风险低、成本小、影响好","那么在实践中被广泛采用","下面，我们就一起来看一下","关于协商解除劳动合同的相关的情景案例","喂，你好","喂，小政啊，你好我是人力资源部的小玫","经公司决定，由于业务调整准备对你所在的采购部进行重组","我知道的，我们部门的人基本上都走光了，现在只剩下我们四个人了","现在公司想与你协商解除劳动合同","方案的有效期是一个星期，就是下个星期的这个时候","那公司有什么条件吗","如果大家书面同意与公司协商解除劳动合同的",......]
V_d290e25363644cb8aae46890b7f3382f|任务1唐诗赏析软件设计|[705,2983,5460,9002,14622,16571,20474,23856,28072,30857,33972,38383,44604,48258,51620,54148,59500,64359,70872,75436,......]|[1500,4792,8398,11980,16372,20132,23181,26594,31216,34032,38137,44379,47703,51304,......]|["今天我们要完成的任务是","“唐诗赏析软件”设计","程序运行之后显示如下界面","该界面显示了一首唐诗：静夜思","通过这个任务我们可以","学习到：第一：TextView的使用方法","第二：线性布局技术的使用方法","下面我们来完成这个任务","首先，创建一个安卓项目","命名为poetryappreciation","第二步",......]
*notice：字段start、end和text因内容过长不便于显示，用......代替*
        
### additional information

#### concept_information.json
字段名 | 说明
------ | ----
name    | 概念名称
wiki_abstract   | 维基百科
baidu_abstract  | 百度百科
baidu_snippet_zh    | title，URL，snippet， score(?)  
google_translation  | 谷歌翻译
properties  | 性质，不同的概念性质所含有的属性不同

* Example

name|wiki_abstract|baidu_abstract|baidu_snippet_zh|google_translation|properties
---|---|---|---|---|---
一向宗暴动| | 15世纪后半叶至16世纪80年代 ，以一向宗运动形式出现的 日本农民反封建武装斗争。一向宗是日本佛教新宗派净土真宗（简称真宗）的别称。其教理强调人们只要在世俗生活中坚持专修念佛，坚信佛力，就可往生极乐并获得现世幸福，因而获得众多农民的信仰。\n|[{"title": "日本简史——一向宗暴动_日本历史_文化娱乐_新世界日语","url": "http://www.baidu.com/link?url=H7RxCbWpyNNjcqSeAKkzsPQAawlPhJnGILqiJuBSvHzoEERWPiXPVJ0-jl12dKWOOsIWcuyTinaeXkgc3jXGPq","snippet": "2009年7月8日 - 新世界日语网是免费的学习资讯网站,日本简史——一向宗暴动的问题信息,包含日本简史——一向宗暴动的问题的相关学习资料、单词测试、评论、学习推荐等...","score": 1.0},{"title": "请翻译一句日语_百度知道","url": "http://www.baidu.com/link?url=Of6SLyzzW_Jc_yYg0ZohanngoiwIFGTjHkCaMjTUQOixbikn93je_DdNOkk5l64h8lIoH5PnwedLQ78icJRAL3koUIYB9Sp3zm26L7_5RLK","snippet": "最佳答案: 全句翻译: 上杉谦信征讨能登国,联合了本愿寺和一向宗发动暴乱,在手取川与织田军作战。 词语翻译: 谦信:上杉谦信。日本战国的大名,能征善战,号称“...更多关于一向宗暴动的问题>>","score": 1.0},{"title": "一向宗农民暴动_百度百科","url": "http://www.baidu.com/link?url=JLF2g9W_7QVJzfsh155QGJ6z7lGt1ErslWhJbK_aIhXkm9KsIbl1W3Gy40Qnh6e5LzQDTEB4Prv-udBjV40-0cANZeXkl8du05Bag6cp4Xqsw5xfxi2WWt3qIsPnEDKZ5jO26s0M3_6gLwlsaB-aCK", "snippet": "2018年10月22日 - 一向宗农民暴动,日本战国时代以净土真宗门徒为核心掀起的农民暴动。净土真宗俗称一向宗,是镰仓中期亲鸾开创的新教派。亲鸾认为皈依阿弥陀佛,任何人都...", "score": 0.5},{"title": "【谋求独立】一向宗暴乱,家康软处理感化叛军", "url": "http://www.baidu.com/link?url=2KGvRvNRho07al0SLgzn52_eaNGD0G2ga9WTIe9uGEmQOdYdkhkxP_1LGn1edztklxCI0HmZi1Pkq-WG-BAqMa","snippet": "2019年6月21日 - 家康经历的暴乱史称三河一向宗暴乱与1563年9月爆发到第二年的2月结束前后持续半年时间。 这对于在森和立足未稳的家康来说,是致命的肘、腋之变。...","score": 0.38888888888888884}]| | 
昆塔尔会议| |1916年4月2430日在 瑞士伯尔尼附近昆塔尔村召开的国际社会主义者第2次代表会议。又称第2次齐美尔瓦尔德会议。出席会议的有来自俄、意、英、波、罗、保、葡和瑞士等国社会主义组织的代表44人。..列宁也参加了会议。\n|[{"title": "昆塔尔会议是什么意思?词语昆塔尔会议怎么解释?什么是昆塔尔会议?...","url": "http://www.baidu.com/link?url=JndomJ7I3_Ex3oyEfLBFJMH40a4agw6hrc1SmehQGqR1fib9iHwiFq39BvkrxZyBHNFYLAJcyqMYXLVktdWaR_d1wk3_-DbaO3O76EFaR0Ezlr54rcMy3ZRHKvMNvp1j","snippet": "词语昆塔尔会议:词语昆塔尔会议解释:第一次世界大战期间举行的国际社会党人第二次代表会议。1916年4月在瑞士昆塔尔村召开,又称第二次齐美尔瓦尔得会议。会上,列宁...","score": 1.0},{"title": "国际社会党第二次代表会议(昆塔尔会议)文献._百度文库","url": "http://www.baidu.com/link?url=U3rbP8yYherLJBdpSIJSDHrHUo5En9EV_Na7FougkxrVoc_2mfgxsQVO1fJsPDZeZi-cMOVKDaM50Frm_Anc_tk1quGdLoouLk_UkfevzJiqNGDF-E1wXxnN6VIJu0JW","snippet": "2019年7月11日 - 国际社会党第二次代表会议(昆塔尔会议)文献. - 国际社会党第二次代表会议(昆塔尔会议)文献 【副标题】 【英文标题】 【作者】列宁/中共中央马克思、恩...","score": 1.0},{"title": "【昆塔尔会议】英语怎么说_在线翻译_有道词典","url": "http://www.baidu.com/link?url=vET16QWc_tF4nKffcd2YRk4Y8325oZrrXHPSfa-C8toO2QM3ywXSPDh2p_3GY3DQC7DF0AHuDGahkjJvRLmPM3b_JSJr7MPnPpR3OI0qy_EZS-3zmJcoB6MK183gjK8d","snippet": "1916年4月2430日在瑞士伯尔尼附近昆塔尔村召开的国际社会主义者第2次代表会议。又称第2次齐美尔瓦尔德会议。出席会议的有来自俄、意、英、波、罗、保、葡和瑞士等...","score": 1.0}]|Quintal Conference| {"外文名": "Kiental","时间": "1916年4月","内容": "无产阶级对和平的态度问题","中文名": "昆塔尔会议"}
       

#### prerequisite_prediction.json
字段名 | 说明
------ | ----
c1  |
c2  |
label|
predict|


* Example

c1|c2|label|predict
---|---|---|---
B树|IP地址|-1|[0.9997708380222321, 0.0002291518361744238]
B树|一元函数|-1|[0.9844805479049683, 0.015519446431426331]

#### user_video_act.json
字段名 | 说明
------ | ----
id  | 用户ID
activity    | 包含多个活动记录。course_id，video_id，watching_count，video_duration，local_watching_time，video_start_time，video_end_time，local_start_time，local_end_time 
  
* Example

id|activity
---|---
U_8650752|[{"course_id": "C_course-v1:TsinghuaX+00740043X_2015_T2+sp","video_id": "V_00a75596b54a48778482dc8cd002d3c4","watching_count": 12,"video_duration": 419.0,"local_watching_time": 386,"video_progress_time": 475.3400101661682,"video_start_time": 0.0,"video_end_time": 419.0,"local_start_time": "2018-03-14 19:45:45","local_end_time": "2018-03-14 20:00:36"},{"course_id": "C_course-v1:TsinghuaX+30640014X+sp","video_id": "V_011003392bc342578883877198a6c2dd","watching_count": 5,"video_duration": 507.0,"local_watching_time": 565,"video_progress_time": 589.0229949951173,"video_start_time": 0.0,"video_end_time": 507.0,"local_start_time": "2018-03-11 23:33:47","local_end_time": "2018-03-12 19:36:10"},{"course_id": "C_course-v1:TsinghuaX+00740043X_2015_T2+sp","video_id": "V_021e36f80cd446ad831fb27081ec973f","watching_count": 2,"video_duration": 202.0,"local_watching_time": 162,"video_progress_time": 201.8800048828125,"video_start_time": 0.0,"video_end_time": 202.0,"local_start_time": "2018-03-15 16:14:35","local_end_time": "2018-03-15 16:17:32"},......]

*notice：字段activity因内容过长不便于显示，用......代替*

## MOOCCube_DS

#### concept_map.json

字段名 | 说明
------ | ----
concept | 
post    |
pre     |
up      |
down    |
rel     |
attributes |

* Example

concept|post|pre|up|down|rel|attributes
---|---|---|---|---|---|---
节点|[]|[]|["图"]|["叶节点","关节点"]|["叶","树结构","出度","顶点","兄弟","连通性","入度","深度优先搜索","连通图","迪杰斯特拉算法","无向图","前驱","哈密顿回路问题","子树"]|["关键码","子树","高度","树根","叶","分支","步","右子","定义","数值","深度","左子","次序"]
线性阵列|[]|[]|[]|[]|[]|[]

## Analysis

TBA

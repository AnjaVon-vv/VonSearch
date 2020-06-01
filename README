# Python编写简单搜索引擎之搜索引擎搭建篇（以pagerank值排名）
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;爬取[电玩巴士](https://www.tgbus.com)部分文章作为后台数据。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;具体是学习Mooc网bobby老师的课程，个人总结教程之后再写。<font color=#9055A2><b>(多么鲜艳的Flag) </font>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[<font color=#fbd14b> 爬虫项目指路 </font>](https://github.com/AnjaVon-vv/ArticleSpider)

## 技术栈
- Python3
	- virtualenv、virtualenvwrapper（不必要,但建议使用，[<font color=#fbd14b> 安装教程 </font>](https://blog.csdn.net/sinat_41135487/article/details/106225574)）
- 搜索引擎支撑elasticsearch：
	- jdk8+
	- [elasticsearch-rtf](https://github.com/medcl/elasticsearch-rtf)：大神开发的适用于中文的版本
	- [elasticsearch-head](https://github.com/mobz/elasticsearch-head)：可视化数据
	- [kibana](https://github.com/elastic/kibana)：运行不必要，学习ES建议安装
- 编写框架django：`pip install django`

## 运行
- [<font color=#fbd14b> 项目地址 </font>](https://github.com/AnjaVon-vv/VonSearch)
- 运行项目即可：`python manage.py runserver 8000`
	- 在localhost:8000打开页面
	- like this……
	
![首页](https://img-blog.csdnimg.cn/20200601165628376.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzQxMTM1NDg3,size_16,color_FFFFFF,t_70 =576x324)

![搜索建议](https://img-blog.csdnimg.cn/20200601165849941.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzQxMTM1NDg3,size_16,color_FFFFFF,t_70 =576x324)

![详情页](https://img-blog.csdnimg.cn/20200601165929226.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzQxMTM1NDg3,size_16,color_FFFFFF,t_70 =576x324)
## 不足
分词太细致导致搜索结果反而不太匹配搜索词，比如：

![问题](https://img-blog.csdnimg.cn/20200601170058905.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzQxMTM1NDg3,size_16,color_FFFFFF,t_70 =576x324)

- 解决方案：
    - 设置搜索模式，指定搜索使用term不对搜索词进行处理，粗略搜索延续match。
    - 爬虫存数据时选用ik_smart等划分相对粗略的分析器。
	
<br>
<table><tr><td bgcolor=#fffff3><font color=#6a60a9><b> 欢迎指正与讨论！</b></font></td></tr></table>
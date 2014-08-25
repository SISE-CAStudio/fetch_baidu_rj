# -*- coding: utf-8 -*-
import urllib2
import re

# 百度软件中心的链接
base_url = 'http://rj.baidu.com/'
list_url = base_url + 'soft/lists/%s'
detail_url = base_url + 'soft/detail/%s.html'


# 获取html
def get_html(url):
    return urllib2.urlopen(url).read()


# 获取所有分类的链接
def get_list_arr():
    list_arr = []
    for i in range(1, 19):
        list_arr.append(list_url % i)
    return list_arr


# 获取某分类下的所有详细页面链接
def get_detail_arr(list_url):
    detail_arr = []
    html = get_html(list_url)
    p = re.compile(r'<a href="/soft/detail/(\d+)\.html">')
    result = p.findall(html)
    result = set(result)  # 去重，转换为set，会打乱顺序
    # list2.sort(key=list1.index) # 重新按照旧列表顺序排序，暂时觉得没必要
    for i in result:
        detail_arr.append(detail_url % i)
    return detail_arr


# 获取详细页面的各项信息
def get_detail_info(detail_url):

    html = get_html(detail_url)

    # 各种蛋疼的正则
    _softname = re.compile(r'<p class="title">(.+?)(?:<span class="english" title="英文软件">|</span><span class="money" title="收费软件">|</span><span class="star")').findall(html)
    _classify = re.compile(r'<span class="sortTitle">(.+?)</span>').findall(html)
    _softpic = re.compile(r'<div class="soft_img">(?:.*?)<img src="" imgSrc="(http://img1sw.baidu.com/.+?)" alt="', re.S).findall(html)
    _version = re.compile(r'<span class="mInfo">版本：(.+?)</span>').findall(html)
    _size = re.compile(r'<span class="lInfo">大小：(.+?)</span>').findall(html)
    _downloadlink = re.compile(r'<a class="normal_download".+class="download" href="(.+?)"></a>').findall(html)
    _website = re.compile(r'<p>软件官网：<a href="(.+?)" target=').findall(html)
    _introduction = re.compile(r'<p class="message">(.+?)</p>', re.S).findall(html)

    try:
        print _softname[0]  # 软件名
        print _classify[0]  # 软件分类
        print _version[0]  # 版本号
        print _size[0]  # 文件大小
        print _downloadlink[0]  # 百度下载链接
        print _introduction[0]  # 功能简介
        print _introduction[1]  # 新版特征

        # 此处小坑，百度上部分软件没有官网/介绍图，所以做特殊处理！！！！！
        if _website == [] :
            print '暂无官网'
        else:
            print _website[0]
        if _softpic == [] :
            print '暂无图片'
        else:
            print _softpic[0]
        # 特殊处理完毕！！！！

        # TODO 存到数据库去

    except Exception as e:
        print '有错误：'
        print e
        return


if __name__ == '__main__':

    for i in get_list_arr():
        for j in get_detail_arr(i):
            get_detail_info(j)

    # get_detail_info(detail_url % 15094)
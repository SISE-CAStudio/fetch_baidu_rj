# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import MySQLdb
import os
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
    detail_arr = {}
    detail_arrarr = []
    html = get_html(list_url)
    p = re.compile(r'<a href="/soft/detail/(\d+)\.html">')
    pic = re.compile(r'<img src="" imgSrc="(.+?)" alt="')
    result_pic = pic.findall(html)
    result1 = p.findall(html)
    result = list(set(result1))  # 去重，转换为set，会打乱顺序
    result.sort(key=result1.index) # 重新按照旧列表顺序排序，暂时觉得没必要
    print result
    for i in result:
        detail_arrarr.append(detail_url % i)
    for index,item in enumerate(detail_arrarr):
        detail_arr[item]=result_pic[index]
        #detail_arr.append(detail_url % i)
    return detail_arr
    #return all_link


# 获取详细页面的各项信息
def get_detail_info(detail_url,pic_url):
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
            _website.append('暂无官网')
        else:
            print _website[0]
        if _softpic == [] :
            print '暂无图片'
            _softpic.append('暂无图片')
        else:
            print _softpic[0]
        
        #数据库操作
        conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="rjbaidu",charset="utf8",port=3306)
    
        cur=conn.cursor()
        sql="INSERT INTO info(softname,classify,softpic,version,size,downloadlink,website,introduction,whatisnew,picurl) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(_softname[0],_classify[0],_softpic[0],_version[0],_size[0],_downloadlink[0],_website[0],_introduction[0],_introduction[1],pic_url)
        cur.execute(sql)
        conn.commit()
        conn.close()

    except Exception as e:
        print '有错误：'
        print e
        return

def write_link_in_file():
    classify=['聊天通讯','输入法','浏览器','下载工具','影视播放','音乐播放','图像编辑','杀毒防护','压缩刻录','系统工具','驱动程序','办公学习','程序开发','影音编辑','手机管理']
    i = 0
    for row in classify:
        file_path = 'E://1/'
        conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="rjbaidu",charset="utf8",port=3306)
        cur=conn.cursor()
        sql="select * from info where classify='"+row+"'"
        cur.execute(sql)
        results=cur.fetchall()
        link=[]
        file_path = file_path + str(i) + '.txt'
        i = i + 1
        print i
        for row in results:
            link.append(row[6])
            link.append(row[10])
        fp=open(file_path,'w')
        print link
        for row in link:
            fp.write(row)
            fp.write('\n')

def download_suoluepic():
    classify=['聊天通讯','输入法','浏览器','下载工具','影视播放','音乐播放','图像编辑','杀毒防护','压缩刻录','系统工具','驱动程序','办公学习','程序开发','影音编辑','手机管理']
    i = 0
    for row in classify:
        file_path = 'E://2/'
        conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="rjbaidu",charset="utf8",port=3306)
        cur=conn.cursor()
        sql="select * from info where classify='"+row+"'"
        cur.execute(sql)
        results=cur.fetchall()
        link=[]
        file_path = file_path + str(i) + '/'
        if not os.path.isdir(file_path):
            os.makedirs(file_path)
        i = i + 1
        print i
        for row in results:
            link.append(row[3])
        for url in link:
            data = urllib.urlopen(url).read() 
            with open(file_path+str(url[-37:]),'wb') as code:
                            code.write(data)

if __name__ == '__main__':
#    for i in get_list_arr():
#        detail_fuck=get_detail_arr(i)
#        for key,value in detail_fuck.items():
#            get_detail_info(key,value)
    download_suoluepic()
#    write_link_in_file()
#     get_detail_info(detail_url % 15094)
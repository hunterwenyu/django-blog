#encoding:utf-8
__author__ = 'wuwy'
import feedparser
import datetime
import urllib2
import config
import models
import re


def convert_date(date):
    month = date.month
    month_str_array = ["", "JAN", "FEB", "MAR", "APR", "MAY", "JUNE", "JULY", "AUG", "SEPT", "OCT", "NOV", "DEC"]
    month_str = month_str_array[month]
    if date.day < 10:
        day_str = "0" + str(date.day)
    else:
        day_str = date.day
    return {"month": month_str, "day": day_str}


def rss_subscribe():
    rss = feedparser.parse(config.blog_rss)['entries']
    blogs = models.Blog.objects.all()

    locked_blogs = []
    for blog in blogs:
        if blog.locked:
            #保存锁定记录（不删除）
            locked_blogs.append(blog)
        else:
            #更新未锁定记录
            blog.delete()

    for b in rss:
        time = re.findall(r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})Z', str(b['published']))
        create_time = datetime.datetime(int(time[0][0]), int(time[0][1]), int(time[0][2]), int(time[0][3])+8, int(time[0][4]))
        html = urllib2.urlopen(b['id']).read()
        content = re.findall(r'<div id=\"cnblogs_post_body\">[\S\s]*<div id=\"MySignature\">', str(html))[0]
        blog = models.Blog()
        blog.title = b['title']
        blog.content = content
        blog.create_time = create_time
        blog.summary = b['summary_detail']['value']
        blog.subtitle = b['title']
        locked = False
        for b in locked_blogs:
            if b.title == blog.title:
                locked = True
        if not locked:
            #只保存未锁定记录
            blog.save()

if __name__ == '__main__':
    rss_subscribe()



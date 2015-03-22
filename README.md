# 基于RSS整理的小型个人博客
  通过django-crontab对系统软件制定计划任务，定期收集cnblogs本人博客文章至本博客目录。
  
## 框架

* `python2.7`      -- 编程语言
* `django`         -- web框架
* `django-crontab` -- 计划任务
* `feedparser`     -- RSS解析框架
  
  
## 如何开启计划任务
**Example**
  * 在`settings.py`中添加计划任务（时间，函数）
  
  ```
    CRONJOBS = [
        ('*/1 * * * *', 'blog.utils.rss_subscribe'),
    ]
  ```
  * 添加计划任务至系统
  `python manage.py crontab add`

  
  



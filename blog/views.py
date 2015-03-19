from django.shortcuts import render_to_response
from models import Blog
import utils
from datetime import date


def index(request, year):
    year = int(year)
    blog_array = Blog.objects.filter(create_time__year=year).order_by('-is_top', '-create_time')
    yesteryear = True if Blog.objects.filter(create_time__year=year-1) else False
    next_year = True if Blog.objects.filter(create_time__year=year+1) else False
    for blog in blog_array:
        date_map = utils.convert_date(blog.create_time)
        blog.month = date_map['month']
        blog.day = date_map['day']
    return render_to_response('index.html', {'blogs': blog_array, 'year': year,
                                             'yesteryear': yesteryear, 'next_year': next_year})


def get_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if not blog:
        index(request, date.today().year)
    return render_to_response('blog.html', {'blog': blog})



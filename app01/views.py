import datetime
import os

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def new_file(testdir):
    # 列出目录下所有的文件
    list = os.listdir(testdir)
    # 对文件修改时间进行升序排列
    list.sort(key=lambda fn: os.path.getmtime(testdir + '\\' + fn))
    # 获取最新修改时间的文件
    # filetime = datetime.datetime.fromtimestamp(os.path.getmtime(testdir + list[-1]))
    # 获取文件所在目录
    # filepath = os.path.join(testdir, list[-1])
    # print("最新修改的文件(夹)：" + list[-1])
    # print("时间：" + filetime.strftime('%Y-%m-%d %H-%M-%S'))
    return list[-1]


def index(request):
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dirs = os.path.join(path, 'templates')
    # html = render_to_string(new_file(dirs))
    return render(request, new_file(dirs))

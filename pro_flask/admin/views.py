from flask import render_template

from . import admin


@admin.route('/index.html')
def index():
    """
    显示首页
    :return:
    """
    return 'Admin.Index'



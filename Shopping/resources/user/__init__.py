# -*- coding:utf-8 -*-
# 用户模块下的蓝图，包括用户模块的所有资源

from flask import Blueprint
from flask_restful import Api
from comment.utils.output import output_json


user_bp=Blueprint('users',__name__)     # 创建蓝图
user_api=Api(user_bp)   # 创建蓝图中的资源API

#使用自定义的json格式，替代装饰器的写法
user_api.representation('application/json')(output_json)  # 给所有的蓝图加了个装饰器，减少代码复用

# 加载当前模块的资源
from Shopping.resources.user.user_resource import Shopping_User
user_api.add_resource(Shopping_User,'/user',endpoint='user')
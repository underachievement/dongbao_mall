# -*- coding:utf-8 -*-
from flask_restful import Resource
from comment.models.user import User
from flask import current_app

# 我们定义的测试的资源类
class Shopping_User(Resource):
    def get(self):
        current_app.logger.info("我的测试日志")

        # 这里的代码可能会用到User模型类
        return {"hello","测试"}

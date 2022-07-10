# -*- coding:utf-8 -*-
from flask import Flask
from settings import map_config

# 负责创建APP
def create_app(config_type):
    app=Flask(__name__)
    # 加载项目的配置
    app.config.from_object(map_config.get(config_type))

    # 加载日志处理的工具

    # 初始化SQLALCHEMY对象

    # 加载蓝图
    return app
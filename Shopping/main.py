# -*- coding:utf-8 -*-
# 咚宝商城项目入口
from Shopping import create_app

app=create_app("develop")

if __name__ == '__main__':
    app.run()
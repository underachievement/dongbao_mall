# -*- coding:utf-8 -*-
# 通过执行命令创建数据库的表
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from Shopping import create_app
from comment.models import db


# 初始化app
app=create_app('develop')
manager=Manager(app)
Migrate(app,db)
manager.add_command("shopping_db",MigrateCommand)

if __name__ == '__main__':
    manager.run()

"""
1.初始化一个环境：python db_manage.py db init   只需要第一次
2.自动检查模型，生成迁移脚本：python db_manage.py db migrate
3.将迁移脚本映射到数据库中：python db_manage.py db upgrade
4.更多命令：python db_manage.py db --help
"""
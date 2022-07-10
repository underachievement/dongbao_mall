# -*- coding:utf-8 -*-

#当前的命令调用flask要和web主程序分离，只是测试一下

from flask_script import Manager
from Shopping import create_app
from flask_sqlalchemy import SQLAlchemy

app=create_app('develop')
db=SQLAlchemy(app)
manager=Manager(app)

class User(db.Model):
    __tablename__='t_user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    uname=db.Column(db.String(50),nullable=False)
    pwd=db.Column(db.String(50),nullable=False)

# db.create_all()

@manager.command
def Hello():
    print("您的命令执行成功")

# 通过命令直接在数据库中创建一个用户
@manager.option("-u","--username",dest='uname')
@manager.option("-p","--password",dest='pwd')
def create_user(uname,pwd):
    user=User(uname=uname,pwd=pwd)
    db.session.add(user)
    db.session.commit()
    print("执行命令添加用户成功")

# 不需要右键运行
if __name__ == '__main__':
    manager.run()

# 只有管理员可以用这种方式，只是会方便一点，仅此而已
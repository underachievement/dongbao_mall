# -*- coding:utf-8 -*-
# 负责整个项目的配置信息

class Config:
    # 配置数据库和SQLAlchemy
    HOSTNAME='127.0.0.1'
    PORT='3306'
    DATABASE='dongbao'
    USERNAME='root'
    PASSWORD='root'

    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
    SQLALCHEMY_DATABASE_URI=DB_URI #数据库的连接
    SQLALCHEMY_TRACK_MODIFICATIONS=False    # 不需要追踪数据库数据的修改

    #日志的配置
    LOGGING_LEVEL="DEBUG"
    LOGGING_FILE_DIR="logs/"
    LOGGING_FILE_MAX_BYTES=1024*1024*300
    LOGGING_FILE_BACKUP=100

#开发环境下的配置信息
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO=True  #打印sql

#生产环境中的配置信息
class ProductConfig(Config):
    pass

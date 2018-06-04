#encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zlkt import app
from exts import db
from models import User, Question

manager = Manager(app)

#帮定app和db

migrate = Migrate(app, db)

#添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
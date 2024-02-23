from flask import Flask
import config

# 因MySQLDB不支持Python3，使用pymysql扩展库代替MySQLDB库pymysql.install_as_MySQLdb()

# 初始化web应用
app = Flask(__name__, instance_relative_config=True)
app.config['DEBUG'] = config.DEBUG

# 设定数据库链接app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/flask_demo'.format(config.username, config.password,config.db_address)

# 初始化DB操作对象db = SQLAlchemy(app)

# 加载控制器
from wxcloudrun import views

# 加载配置app.config.from_object('config')

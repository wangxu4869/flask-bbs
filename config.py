import os

SECRET_KEY=os.urandom(24)

DEBUG=False

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlbbs'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
CMS_USER_ID='ASDFAJKQA'
FRONT_USER_ID='AFASFDIJOIEKFK'


#发送者邮箱的服务器地址
#QQ邮箱不支持非加密方式发送邮件
#MAIL_USE_TILS端口号：587
#MAIL_USE_SSL端口号：465
MAIL_SERVER='smtp.qq.com'
MAIL_PORT=587
MAIL_USE_TLS=True
# MAIL_USE_SSL=
# MAIL_DEBUG=
MAIL_USERNAME='653590766@qq.com'
MAIL_PASSWORD='hewaszknucenbcaa'
MAIL_DEFAULT_SENDER='653590766@qq.com'

# 阿里大于相关配置
ALIDAYU_APP_KEY = '23709557'
ALIDAYU_APP_SECRET = 'd9e430e0a96e21c92adacb522a905c4b'
ALIDAYU_SIGN_NAME = '小饭桌应用'
ALIDAYU_TEMPLATE_CODE = 'SMS_68465012'

#ueditor相关配置
UEDITOR_UPLOAD_TO_QINIU = True
UEDITOR_QINIU_ACCESS_KEY = "9-7_e1Ib_BMkgbdsSgmpGoW_VIrTYMGKO-3XdxtG"
UEDITOR_QINIU_SECRET_KEY = "FzvqhdlgxRaOw5Kh2CvmrJkce8-s-e1Aq9wl7S0h"
UEDITOR_QINIU_BUCKET_NAME = "wxvideo"
UEDITOR_QINIU_DOMAIN = "http://pso0y4hys.bkt.clouddn.com/"

#flask-paginate中的相关配置
PER_PAGE=10

#celery相关配置
CELERY_RESULT_BACKEND='redis://127.0.0.1:6379/0'
CELERY_BROKER_URL='redis://127.0.0.1:6379/0'
from os import environ
from six.moves.urllib.parse import urlparse


class Config(object):

    DEBUG = False
    TESTING = False

    SECRET_KEY = 'MmPNFrWjQZ3Z9yKZ8PMFQttgHphaq8AZ'

    APP_TRANSPORT = environ.get('APP_TRANSPORT', 'http')
    APP_DOMAIN = environ.get('APP_DOMAIN', 'http://gusibi.com')
    API_DOMAIN = environ.get('API_DOMAIN', 'http://gusibi.com')
    DOMAIN = '%s://%s' % (APP_TRANSPORT, urlparse(APP_DOMAIN).netloc)

    # 微信 公众账号信息
    WEIXINMP_APPID = environ.get('WEIXINMP_APPID', 'wx1c88a488e93f3bd0')
    WEIXINMP_APP_SECRET = environ.get('WEIXINMP_APP_SECRET', '')
    WEIXINMP_TOKEN = environ.get('WEIXINMP_TOKEN', '2005726luoling')
    WEIXINMP_ENCODINGAESKEY = environ.get(
        'WEIXINMP_ENCODINGAESKEY', 'hEIB9nMZlFK1tEIYT4kNwog2395UYLGtcaK14Ywlkkt')

    QINIU_ACCESS_TOKEN = environ.get('QINIU_ACCESS_TOKEN', '')
    QINIU_SECRET_TOKEN = environ.get('QINIU_SECRET_TOKEN', '')
    QINIU_UPLOAD_URL = 'http://up.qiniu.com/'
    QINIU_DOMAIN = environ.get('QINIU_DOMAIN', 'media.gusibi.mobi')
    QINIU_DOMAINS = [QINIU_DOMAIN, 'omuo4kh1k.bkt.clouddn.com']
    QINIU_HOST = "http://%s" % QINIU_DOMAIN
    QINIU_NOTIFY_URL = '%s/qiniu/pfop/notify' % DOMAIN
    QINIU_BUCKET = environ.get('QINIU_BUCKET', 'blog')

    QINIU_AUDIOS_TIME_KEY = environ.get('QINIU_AUDIOS_TIME_KEY', '')
    QINIU_AUDIOS_HOST = environ.get('QINIU_AUDIOS_HOST',
                                    'http://omuo4kh1k.bkt.clouddn.com')

    QINIU_AUDIOS_CONFIG = {
        'access_key': QINIU_ACCESS_TOKEN,
        'secret_key': QINIU_SECRET_TOKEN,
        'time_key': QINIU_AUDIOS_TIME_KEY,
        'host': QINIU_AUDIOS_HOST
    }
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!r-q65&abt%x7zdfl463_b!v1md6)um6kv@vo)_t#s0))aa0_@'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_HOST = 'mail.smtp2go.com'

EMAIL_PORT = 587

EMAIL_HOST_USER = 'omerpucit@technodevs.com'

EMAIL_HOST_PASSWORD = 'VqsfKEZPHdNB'

DEFAULT_FROM_EMAIL = 'omerpucit@technodevs.com'


EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


try:
    from .local import *
except ImportError:
    pass

from pathlib import Path

# =========== 必要配置
# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent
# 根路由
ROOT_URLCONF = 'confs.root_urls'
# 本地媒体根目录 - 可与视图 django.views.static.serve(req, path, document_root?, show_indexes?) 一起使用
MEDIA_ROOT = BASE_DIR / 'assets' / 'media'
# debug 模式
DEBUG = True

# =========== 部署项目
# 若 DEBUG = False，则需要设置 ALLOWED_HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'liangxiongsl.github.io']
# asgi 服务器
ASGI_APPLICATION = 'confs.asgi.application'
# wsgi 服务器
# WSGI_APPLICATION = 'confs.wsgi.application'
SECRET_KEY = 'django-insecure-tvv@@j^*8t2_yd5#sn0-+fdm92ub*8d$db%z-a!)8otz=p-tfa'

# ========== 可插拔配置
# 应用
INSTALLED_APPS = [
    'daphne',
    'music.ExampleAppConfig',
    'rest_framework',
    'django_extensions',
    'graphene_django',

    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 中间件 - 请求过程中的中间处理
MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django.middleware.cache.FetchFromCacheMiddleware",
    "music.middlewares.LoginRequiredMiddleware",
]

# 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 模板
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'assets/templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'builtins' : [
            #     'django.templatetags.static',
            # ],
        },
    },
]

# ============= 本地化 / 国际化
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_TZ = True

# =========== 其他设置
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEFAULT_CHARSET = 'utf-8'


# ========== 静态资源
STATICFILES_DIRS = [
    BASE_DIR / 'assets' / 'static',
]
# 将 STATIC_URL 指定的路径暴露到 http path？
STATIC_URL = '/static/'
# python manage.py collectstatic 命令将项目所有的静态文件目录整合于 STATIC_ROOT 指定的目录
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ========== 认证
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend"
]
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# LOGIN_URL = '/account/login/'

# ============== 邮箱
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
# EMAIL_PORT = 25
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '1708494470@qq.com'
EMAIL_HOST_PASSWORD = 'gotcasiskumechjd'

EMAIL_SUBJECT_PREFIX = '[lx-dg] '
SERVER_EMAIL = '1708494470@qq.com'
ADMINS = [
    ('liangxiongsl', '1506218507@qq.com'),
    ('drk', '1708494470@qq.com'),
    # ('yuxiao', '3405400062@qq.com'),
]
MANAGERS = [
    # ('lx', '1506218507@qq.com'),
    # ('drk', '1708494470@qq.com'),
    # ('yuxiao', '3405400062@qq.com'),
]

# ============== 缓存
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
    "my_cache": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache",
        "TIMEOUT": 60,
        "OPTIONS": { "MAX_ENTRIES": 9, "CULL_FREQUENCY": 1 },
        "KEY_PREFIX": "jjj",
    },
    # "redis": {
    #     "BACKEND": "django.core.cache.backends.redis.RedisCache",
    #     "LOCATION": "redis://127.0.0.1:6379",
    # }
}
CACHE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 10
# CACHE_MIDDLEWARE_KEY_PREFIX = "cache "

# ============== 会话
SESSION_ENGINE = "django.contrib.sessions.backends.db"

# ============== 消息
MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'
MESSAGE_LEVEL = 10
# MESSAGE_TAGS =
# SESSION_COOKIE_DOMAIN =
# SESSION_COOKIE_SECURE =
# SESSION_COOKIE_HTTPONLY =


# ============== csrf
CSRF_TRUSTED_ORIGINS = ['http://localhost:5173', "https://liangxiongsl.github.io"]


# ============== django RESTFul framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticated',
    ],

    # 分页
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
}


# ============== django extensions



# =============== graphene-django
GRAPHENE = {
    "SCHEMA": "my_graphql.schema.schema"
}



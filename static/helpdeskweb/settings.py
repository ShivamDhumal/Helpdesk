"""
Django settings for helpdeskweb project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x_zh%ru%pujj^owfhze#qw0(=4860@bx*j87j+-su+wjfdhvb#'
# SECRET_KEY = 'fa09951c-d279-449f-8848-6fbfd077f79d'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['django-call-graph.azurewebsites.net','localhost']
ALLOWED_HOSTS = ['*']


# Application definition



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helpdeskapp',
    'crispy_forms',
    'crispy_bootstrap5',
    'accounts',
    'it_manager',
    'it_engineer',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'helpdeskweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'helpdeskweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db2.sqlite3',

    }
}

# DATABASES={
#    'default':{
#       'ENGINE':'django.db.backends.postgresql_psycopg2',
#       'NAME':'project_name',
#       'USER':'user_name',
#       'PASSWORD':'password',
#       'HOST':'localhost',
#       'PORT':'',
#    }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'Helpdesk',
#         'ENFORCE_SCHEMA': False,
#         'CLIENT': {
#                 'host': 'mongodb+srv://shivam:Shivam@16102000@cluster0.1bumxjr.mongodb.net/Helpdesk?retryWrites=true&w=majority'
#         }
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR, 'staticfiles'
]

# mail setup code 

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'hdts.adypu@gmail.com'
# EMAIL_HOST_PASSWORD = 'eoypbqxchlcjwdxq'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'helpdeskticketingsystem.adypu@gmail.com'
EMAIL_HOST_PASSWORD = 'kofncizlluaeogvt'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# mail setup code end

AUTH_USER_MODEL = "accounts.User"

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'helpdeskapp:index'
LOGOUT_REDIRECT_URL = 'accounts:login'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"




# from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
# import ldap

# # Baseline configuration.
# AUTH_LDAP_SERVER_URI = 'ldap://192.168.1.89'

# AUTH_LDAP_BIND_DN = "CN=LDAP,CN=Users,DC=cloudstrats,DC=local"
# AUTH_LDAP_BIND_PASSWORD = "Ctpl@123"

# AUTH_LDAP_USER_SEARCH = LDAPSearch(
#     "CN=Users,DC=cloudstrats,DC=local", ldap.SCOPE_SUBTREE, "mail=%(user)s"
# )

# # AUTH_LDAP_USER_DN_TEMPLATE = "CN=%(user)s,CN=Users,DC=cloudstrats,DC=local"


# # myfield: ldapfield

# AUTH_LDAP_USER_ATTR_MAP = {
#     "first_name": "givenName",
#     "last_name": "sn",
#     "email": "mail",
#     "phone_number" : "sAMAccountType",
#     "job_title" : "Title",
#     "department" : 'Department',
#     'city':'City',
# }



# AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
# "CN=Users,DC=cloudstrats,DC=local",
#     ldap.SCOPE_SUBTREE,
#     "(objectClass=groupOfNames)",
# )

# # AUTH_LDAP_REQUIRE_GROUP = "CN=Administrator,CN=Users,DC=cloudstrats,DC=local"

# AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="CN")

# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_active": "CN=django-users,CN=Users,DC=cloudstrats,DC=local",
#     "is_staff": "CN=django-admins,CN=Users,DC=cloudstrats,DC=local",
#     "is_superuser": "CN=django-admins,CN=Users,DC=cloudstrats,DC=local",
#     "is_it_manager": "CN=django-IT-managers,CN=Users,DC=cloudstrats,DC=local",
#     "is_it_engineer": "CN=django-IT-engineer,CN=Users,DC=cloudstrats,DC=local",
# }
# # 
# # This is the default, but I like to be explicit.
# AUTH_LDAP_ALWAYS_UPDATE_USER = True

# # Use LDAP group membership to calculate group permissions.
# AUTH_LDAP_FIND_GROUP_PERMS = True

# AUTH_LDAP_MIRROR_GROUPS = True

# AUTH_LDAP_AUTHORIZE_ALL_USERS = True

# # Cache distinguished names and group memberships for an hour to minimize
# # LDAP traffic.
# AUTH_LDAP_CACHE_TIMEOUT = 3600

# AUTHENTICATION_BACKENDS = (
#     "django_auth_ldap.backend.LDAPBackend",
#     "django.contrib.auth.backends.ModelBackend",
# )

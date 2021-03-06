#coding:utf-8
"""
                        Django settings for blog project.
=================================================================================================================
    用到的第三方库:

    SQL  Table TRANSFORM TOOL        |south               :  (http://south.aeracode.org)
    RichTextEditor                   |django-ckEditor     :  (https://github.com/shaunsephton/django-ckeditor)   
    Library for  ckEditor            |Pillow              :  (pip install Pillow)
    Django  Api Tool                 |django_tastypie     :  (http://django-tastypie.readthedocs.org/en/latest/)
              
=================================================================================================================             
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#模板路径
TEMPLATE_DIRS = os.path.join(BASE_DIR, 'templates').replace('\\','/')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kx4$5fk7+o8!20u_s%-q19kr_^8(+x(723qmj$qi(n8q=l%jm('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoblog',
    'account',
    'blog',
    'south',
    'django.contrib.staticfiles'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'blog.urls'

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoblog',
        'USER' :'root',
        'PASSWORD' : '',
        'HOST' :'',
        'PORT' :'',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR, 'statics_file')
#STATICFILES_DIRS = '/var/local/blog/blog/static'
STATICFILES_DIRS =os.path.join(BASE_DIR,'static').replace('\\','/'),
    


#media
MEDIA_URL = "/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,'media').replace('\\','/')  
CKEDITOR_UPLOAD_PATH = "article"
"""
==============================                   Ck_Editor        ====================================================
"""
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
            ['div','Source','-','Save','NewPage','Preview','-','Templates','CodeSnippet'], 
           # ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'], 
            ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'], 
            #['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'], 
            ['Textarea'],
            ['Bold','Italic','Underline','Strike','-',], 
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'], 
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'], 
            #['Link','Unlink'], 
            ['Image'],#['Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'], 
            ['Styles','Format','Font','FontSize'], 
            ['TextColor','BGColor'], 
            ['Maximize','-','ShowBlocks','-']#['About', 'pbckcode'],
            
        ),
    }
}

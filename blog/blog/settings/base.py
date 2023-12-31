from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

SITE_ID = 1

INSTALLED_APPS = [
    "account.apps.AccountConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.postgres",
    "django.forms",
    "post.apps.PostConfig",
    "ckeditor",
    "ckeditor_uploader",
    "taggit",
    "mptt",
    "easy_thumbnails",
    "comment",
    "crispy_forms",
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "blog.urls"

LOGIN_REDIRECT_URL = "account:dashboard"
LOGIN_URL = "account:login"
LOGOUT_URL = "account:logout"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "blog.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CKeditor settings
CKEDITOR_UPLOAD_PATH = "uploads/editor"
CKEDITOR_IMAGE_BACKEND = "ckeditor_uploader.backends.PillowBackend"
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

CUSTOM_TOOLBAR = [
    {
        "name": "document",
        "items": [
            "Styles",
            "Format",
            "Bold",
            "Italic",
            "Underline",
            "Strike",
            "-",
            "TextColor",
            "BGColor",
            "-",
            "JustifyLeft",
            "JustifyCenter",
            "JustifyRight",
            "JustifyBlock",
        ],
    },
    {
        "name": "widgets",
        "items": [
            "Undo",
            "Redo",
            "-",
            "NumberedList",
            "BulletedList",
            "-",
            "Outdent",
            "Indent",
            "-",
            "Link",
            "Unlink",
            "-",
            "Image",
            "CodeSnippet",
            "Table",
            "HorizontalRule",
            "Smiley",
            "SpecialChar",
            "-",
            "Blockquote",
            "-",
            "ShowBlocks",
            "Maximize",
        ],
    },
]

DEFAULT_CONFIG = {
    "skin": "moono-lisa",
    "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
    "toolbar_Full": [
        [
            "Styles",
            "Format",
            "Bold",
            "Italic",
            "Underline",
            "Strike",
            "SpellChecker",
            "Undo",
            "Redo",
        ],
        ["Link", "Unlink", "Anchor"],
        ["Image", "Flash", "Table", "HorizontalRule"],
        ["TextColor", "BGColor"],
        ["Smiley", "SpecialChar"],
        ["Source"],
    ],
    "toolbar": "Full",
    "height": 291,
    "width": "100%",
    "filebrowserWindowWidth": 940,
    "filebrowserWindowHeight": 725,
}

CKEDITOR_CONFIGS = {
    "default": DEFAULT_CONFIG,
    "my-custom-toolbar": {
        "skin": "moono-lisa",
        "toolbar": CUSTOM_TOOLBAR,
        "toolbarGroups": None,
        "extraPlugins": ",".join(
            ["uploadimage", "image2", "codesnippet", "html5video", "widget"]
        ),
        "removePlugins": ",".join(["image"]),
        "codeSnippet_theme": "xcode",
    },
}

# End Ckeditor settings

# Comments
COMMENT_FLAGS_ALLOWED = 10
COMMENT_USE_EMAIL_FIRST_PART_AS_USERNAME = True
COMMENT_USE_GRAVATAR = True
COMMENT_ALLOW_SUBSCRIPTION = False
PROFILE_APP_NAME = "account"
PROFILE_MODEL_NAME = "Profile"
ADMINS = (("Yasin Alipour", "yasinalipour@example.com"),)

# Email server config
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")

# mptt model setting
MPTT_ADMIN_LEVEL_INDENT = 20

# Crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "account.authentication.EmailAuthBackend",
]

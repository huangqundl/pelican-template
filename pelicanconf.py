#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'huangqundl'
SITENAME = u'\u7075\u9b42\u7194\u7089'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_URL = 'posts/{date:%Y}-{date:%b}-{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%b}-{slug}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

THEME = 'theme/huangqundl-bootstrap3'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_MAX_ITEMS = 100
TAGS_URL = "tags"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud"]
DISPLAY_CATEGORIES_ON_MENU = False
QUOTE = "\"Life is tough, so you must work harder.\""
BANNER = True
BANNER_ALL_PAGES = True
BANNER_SUBTITLE = "\"Life is tough, so you must work harder.\""

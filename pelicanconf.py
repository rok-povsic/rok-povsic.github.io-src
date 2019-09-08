#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rok Povšič'
SITENAME = u'Dev Log'
SITEURL = 'https://rokpovsic.com'
SITESUBTITLE = 'Tech blog by Rok Povšič'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
LOCALE = ('en_US.UTF-8',)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True
MENUITEMS = [
    ('All posts', '/archives'),
]

# Blogroll
# LINKS = ()

# Social widget
SOCIAL = (
    ('stack-overflow', 'http://stackoverflow.com/users/365837/yper'),
    ('github', 'https://github.com/rok-povsic'),
    ('linkedin', 'https://www.linkedin.com/in/rokpovsic'),
    ('rss', 'feeds/all.atom.xml'),
)
SHOW_SOCIAL_ON_INDEX_PAGE_HEADER = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/pelican-clean-blog'
LOAD_CONTENT_CACHE = False
IGNORE_FILES = ['articles-wip', ]

# PYGMENTS_STYLE = 'monokai'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary']
# PLUGINS += ['yuicompressor']

HEADER_COLOR = '#1a4971'
COLOR_SCHEME_CSS = 'monokai.css'

from datetime import date
CURRENT_YEAR = date.today().year

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

STATIC_PATHS = ['images', 'videos']

MD_EXTENSIONS = ['headerid']

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rok Povšič'
SITENAME = u'Rok Povšič blog'
SITEURL = 'https://rokpovsic.com'

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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/flex'
LOAD_CONTENT_CACHE = False
IGNORE_FILES = ['articles-wip', ]

SUMMARY_MAX_LENGTH = 50
PYGMENTS_STYLE = 'monokai'

GOOGLE_ANALYTICS = 'UA-41532619-2'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary']

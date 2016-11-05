#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rok Povšič'
SITENAME = u'Rok Povšič blog'
SITEURL = 'https://rokpovsic.com'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True
MENUITEMS = [
    ('About', '/pages/about-me'),
    ('Contact', '/pages/contact'),
]

# Blogroll
# LINKS = ()

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/rokpovsic'),
    ('github', 'https://github.com/rok-povsic'),
    ('rss', 'feeds/all.atom.xml'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/flex'
LOAD_CONTENT_CACHE = False
ARTICLE_EXCLUDES = ['articles_wip', ]

SUMMARY_MAX_LENGTH = 0
PYGMENTS_STYLE = 'monokai'

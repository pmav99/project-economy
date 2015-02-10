#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Θανάσης Αργυρίου & Παναγιώτης Μαυρογιώργος'
SITENAME = 'Economy Project'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Athens'
LOCALE = "el_GR"
DEFAULT_LANG = 'el'

#MENUITEMS = [
    #("google", "http://www.google.com"),
    #("yahoo", "http://www.google.com"),
    #("bing", "http://www.google.com"),
#]

SHOW_ARTICLE_AUTHOR = True
#SHOW_ARTICLE_CATEGORY = True
#SHOW_DATE_MODIFIED = True

#BOOTSTRAP_FLUID = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
#DISPLAY_ARTICLE_INFO_ON_INDEX = True

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

DEFAULT_PAGINATION = 4

THEME = "../themes/pelican-bootstrap3"
THEME = "./pelican-bootstrap3"
BOOTSTRAP_THEME = "superhero"

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DELETE_OUTPUT_DIRECTORY = True

PLUGIN_PATHS = ['./plugins', '../plugins']
PLUGINS = [
    "assets",
    #"liquid_tags",
    "sitemap",
    'simple_footnotes',
    'series',
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

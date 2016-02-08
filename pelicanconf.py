#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jason Hamilton-Smith'
SITENAME = u'Zchfvy'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['favicon/']
EXTRA_PATH_METADATA = {
    'favicon/favicon.ico': {'path': 'favicon.ico'},
    'favicon/favicon-196x196.png': {'path': 'favicon-196x196.png'},
    'favicon/favicon-160x160.png': {'path': 'favicon-160x160.png'},
    'favicon/favicon-96x96.png'  : {'path': 'favicon-96x96.png'}  ,
    'favicon/favicon-32x32.png'  : {'path': 'favicon-32x32.png'}  ,
    'favicon/favicon-16x16.png'  : {'path': 'favicon-16x16.png'}  ,
}

THEME = 'alchemy'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LICENSE_NAME = 'Creative Commons Attribution-ShareAlike 4.0 International License.'
LICENSE_URL = 'http://creativecommons.org/licenses/by-sa/4.0/'

EMAIL_ADDRESS = 'hs.jason@gmail.com'
TWITTER_ADDRESS = 'https://twitter.com/jason_hs'
GITHUB_ADDRESS = 'https://github.com/jason-hs'

EXTRA_FAVICON = True

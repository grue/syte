
DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.0'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = '[ENTER TUMBLR BLOG URL] ex. rigoneri.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = '[ENTER TUMBLR API KEY HERE, SEE TUMBLR SETUP INSTRUCTIONS]'


#Twitter Integration
TWITTER_INTEGRATION_ENABLED = False
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&screen_name='
TWITTER_CONSUMER_KEY = '[ENTER TWITTER CONSUMER KEY HERE, SEE TWITTER SETUP INSTRUCTIONS]'
TWITTER_CONSUMER_SECRET = '[ENTER TWITTER CONSUMER SECRET HERE, SEE TWITTER SETUP INSTRUCTIONS]'
TWITTER_USER_KEY = '[ENTER TWITTER USER KEY HERE, SEE TWITTER SETUP INSTRUCTIONS]'
TWITTER_USER_SECRET = '[ENTER TWITTER USER SECRET HERE, SEE TWITTER SETUP INSTRUCTIONS]'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_USER_API_URL = 'https://github.com/api/v2/json/user/show/grue'
GITHUB_REPOS_API_URL = 'https://github.com/api/v2/json/repos/show/grue'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = False
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'

#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = False
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '[ENTER INSTAGRAM ACCESS TOKEN HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_USER_ID = '[ENTER INSTAGRAM USER_ID HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'

INSTAGRAM_OAUTH_ENABLED = False
INSTAGRAM_CLIENT_ID = '[ENTER INSTAGRAM CLIENT_ID HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_CLIENT_SECRET = '[ENTER INSTAGRAM CLIENT_SECRET HERE, SEE INSTAGRAM SETUP INSTRUCTIONS]'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://joshua.in/'

MEDIA_URL = SITE_ROOT_URI + 'static/'

# Heroku Specific

import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

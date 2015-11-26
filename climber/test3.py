try:
    import json
except ImportError:
    import simplejson as json
import cookielib
import urllib2

cookie_jar = cookielib.MozillaCookieJar()
cookies = open('cookies.txt').read()
for cookie in json.loads(cookies):
    print cookie['name']
    cookie_jar.set_cookie(cookielib.Cookie(version=0,
                                           name=cookie['name'],
                                           value=cookie['value'],
                                           port=None,
                                           port_specified=False,
                                           domain=cookie['domain'],
                                           domain_specified=False,
                                           domain_initial_dot=False,
                                           path=cookie['path'],
                                           path_specified=True,
                                           secure=cookie['secure'],
                                           expires=None, discard=True,
                                           comment=None,
                                           comment_url=None,
                                           rest={'HttpOnly': None},
                                           rfc2109=False))

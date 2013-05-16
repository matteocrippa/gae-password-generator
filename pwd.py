#pwd - quick online password generator
#author: Matteo Crippa
#version: 1.51

import wsgiref.handlers
import md5
import time
import googleLanguage
import os
import cgi
import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
 def get(self,length):
  salt = 'pwd'
  salt2 = 'generator'
  salt1 = str(time.time())
  pwd = md5.new(salt+salt1+salt2)
  if length:
   try:
    length = int(length)
    password = pwd.hexdigest()[0:int(length)]
   except ValueError:
    password = 'Length Error'
  else:
   password = pwd.hexdigest()
   
  template_values={
   'password': password,
   'autotranslate' : googleLanguage.googleLanguage(),
  }
  path = os.path.join(os.path.dirname(__file__),'themes/index.html')
  self.response.out.write(template.render(path,template_values))
  
def main():
 urls = []
 urls.append(('/(.*)',MainPage))
 application = webapp.WSGIApplication(urls,debug=True)
 wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
 main()
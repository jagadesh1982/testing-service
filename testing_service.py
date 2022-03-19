import logging
import os
import json
import tornado.ioloop
import tornado.web
import random
import time
import socket
import random
import string
from os import environ
import time


from tornado.escape import json_encode

class Info(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/info` resource.
    """
    try:
      hostname = socket.gethostname()    
      IPAddr = socket.gethostbyname(hostname)    
      logging.info("/info serving from %s has been invoked from %s \n", hostname, IPAddr)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : VERSION,
          "host" : hostname,
          "from" : IPAddr
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)


class Fruit(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/fruit` resource.
    """
    try:
      hostname = socket.gethostname()    
      IPAddr = socket.gethostbyname(hostname)    
      logging.info("/Demo serving from %s has been invoked from %s \n", hostname, IPAddr)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : VERSION,
          "host" : hostname,
          "from" : IPAddr,
          "fruit": FRUIT
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)


class Environment(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/env` resource.
    """
    try:
      logging.info("/env serving from %s has been invoked from %s \n", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : VERSION,
          "env" : str(os.environ),
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)

class Random(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/rand` resource.
    """
    try:
      letters = string.ascii_lowercase
      file = open("file.txt", "w")
      file.write(''.join(random.choice(letters) for i in range(10)))
      file.write("\n")

      logging.info("/env serving from %s has been invoked from %s \n", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : file.read(),
          "env" : str(os.environ),
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)

class Random(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/rand` resource.
    """
    try:
      letters = string.ascii_lowercase
      logging.info("/env serving from %s has been invoked from %s \n", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "Random" : ''.join(random.choice(letters) for i in range(10))
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)

class Read(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/read` resource.
    """
    try:
      letters = string.ascii_lowercase
      fopen = open("/demo/demofile.txt", "r")
      logging.info("/env serving from %s has been invoked from %s \n", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "Contents" : fopen.read()
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)     


if __name__ == "__main__":
  app = tornado.web.Application([
        (r"/info", Info),
        (r"/env", Environment),
        (r"/fruit", Fruit),
        (r"/rand", Random),
        (r"/read", Read) 
  ])
 
 
  PORT = os.getenv('PORT0', 9876)
  VERSION = os.getenv('VERSION', "0.5.0")
  FRUIT = os.getenv('FRUIT', "apple")
  
  with open('/tmp/test.txt', 'w') as f:
    f.write('Create a new text file!')

  if environ.get('SLEEP') is not None:
    time.sleep(int(os.getenv('SLEEP')))

  os.remove("/tmp/test.txt")
  app.listen(PORT, address='0.0.0.0')
  logging.info("This is simple service in version v%s listening on port %s", VERSION, PORT)
  tornado.ioloop.IOLoop.current().start()


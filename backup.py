import logging
import os
import json
import tornado.ioloop
import tornado.web
import random
import time
import socket
from tornado.escape import json_encode


class Info(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/info` resource.
    """
    try:
      hostname = socket.gethostname()    
      IPAddr = socket.gethostbyname(hostname)    
      logging.info("/info serving from %s has been invoked from %s \n", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : VERSION,
          "host" : hostname,
          "type" : "apple",
          "from" : IPAddr
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      self.set_status(404)


class Version(tornado.web.RequestHandler):
  def get(self):
    """
    Handles `/version` resource.
    """
    try:
      hostname = socket.gethostname()
      IPAddr = socket.gethostbyname(hostname)
      logging.info("/version serving from %s has been invoked from %s \n", self.request.host, self.request.remote_ip)
      self.set_header("Content-Type", "application/json")
      self.write(json_encode(
        {
          "version" : "banana",
          "host" : hostname,
          "from" : IPAddr
        }
      ))
      self.finish()
    except Exception, e:
      logging.debug(e)
      print e
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


if __name__ == "__main__":
  app = tornado.web.Application([
        (r"/info", Info),
        (r"/version", Version),
        (r"/env", Environment)
  ])
 
 
  PORT = os.getenv('PORT0', 9876)
  VERSION = os.getenv('VERSION', "0.5.0")

  app.listen(PORT, address='0.0.0.0')
  logging.info("This is simple service in version v%s listening on port %s", VERSION, PORT)
  tornado.ioloop.IOLoop.current().start()

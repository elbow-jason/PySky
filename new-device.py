import urllib
import pycurl

def getNewID():
  curler = pycurl.Curl()
  req_type = {'type' :' example'}
  curler.setopt(curler.URL, 'http://skynet.im/devices')
  curler.setopt(curler.POST, 1)
  post = urllib.urlencode(req_type)
  curler.setopt(curler.POSTFIELDS, post)

  curler.perform()

  print "retrieved: \n", curler
  return curler

new_device = getNewID()
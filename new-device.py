import urllib
import pycurl
import StringIO

def new_device():
#set up vars
  id_holder = StringIO.StringIO()
  curler    = pycurl.Curl()
  req_type  = {'type' :' example'}
  post      = urllib.urlencode(req_type)

#set up curler
  curler.setopt(curler.URL, 'http://skynet.im/devices')
  curler.setopt(curler.POST, 1)
  curler.setopt(curler.WRITEFUNCTION, id_holder.write)
  curler.setopt(curler.POSTFIELDS, post)
  curler.perform()

  print "id_holder.getvalue() =>"
  print id_holder.getvalue()
  return id_holder.getvalue()

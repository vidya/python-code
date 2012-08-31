#
#-------------------- problem description { --------------------
#
# Problem: In the dynamic language of your choice, write
# a short program that will:
#
#   define a list of the following user ids 42346, 77290,
#   729 (you can hardcode these, but it should still work
#   with more or less ids)
#
#   retrieve an xml document related to each user at this url
#   	"http://api.etsy.com/feeds/xml_user_details.php?id="
#
#   retrieve the data contained in the city element from each xml 
#   document    
#     
#   keep a running total of how many users are found in each city
#
#   display the total count of users living in each city
#   
#   You can assume user ids are valid and that the url is
#   available. The output should look something like:
#   
#     Charlotte: 1 New York: 2
#
#-------------------- } problem description  ---------------------
#

import xml.sax

#------------- UserHandler { -------------
class UserHandler(xml.sax.handler.ContentHandler):
  def __init__(self):
    self.inCity = 0
    self.cityCount = {}
    
  def startElement(self, name, attributes):
    if name == "user":
      self.city = ""
    elif name == "city":
      self.inCity = 1
 
  def characters(self, data):
    if self.inCity:
      self.city += data.strip()
 
  def endElement(self, name):
    if name == "city":
      self.inCity = 0
      if self.cityCount.has_key(self.city):
         self.cityCount[self.city] += 1
      else:
         self.cityCount[self.city] = 1
#------------- } UserHandler  -------------

#------------- main ----------------------
USER_DETAIL_URL = "http://api.etsy.com/feeds/xml_user_details.php?id=%s"

handler = UserHandler()

parser = xml.sax.make_parser()
parser.setContentHandler(handler)

idList = [42346, 77290, 729]
for id in idList:
   parser.parse(USER_DETAIL_URL % id)

outStr = ""  
for k, v in handler.cityCount.iteritems():
  outStr += "%s: %d " % (k, v)

print outStr
   

from xml.dom import minidom
import pymongo

# Create a mongodb connection
client = pymongo.MongoClient()
db = client['xml_qburst1']
urlcollection = db.urlcollection

# Parse the xmldoc
xmldoc = minidom.parse('qburst.xml')
itemlist = xmldoc.getElementsByTagName('loc') 

# Store the data in mongodb
for s in itemlist :
    urlcollection.insert({s.localName: s.childNodes[0].data})

print "Xml stored in mongodb successfully"
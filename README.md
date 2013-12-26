python_xml_parsing
==================

This is a sample app using python to parse an xml file and store in mongo db.

This is a trial app created for parsing xml data and storing it in mongo db.

I have used minidom for Xml processing and pymongo to connect to the mongodb.

Here a mongodb connection is established initially, then the xml data is parsed using minidom and the parsed data is stored in the mongodb using the insert command.

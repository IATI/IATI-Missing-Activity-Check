import xml.sax
import json

# Set empty identifier
datastore_identifiers = []

# Class for identifing a IATI identifier from an XML
class IATIIdentifierHandler(xml.sax.ContentHandler):
    
    # Set default values
    inIdentifier = False
    identifier = ''
    i = 0

    def startElement(self, name, attrs):
        if name == "iati-identifier":
            self.i += 1
            if self.i % 1000 == 0:
                print(self.i)
            self.inIdentifier = True

    def endElement(self, name):
        if name == "iati-identifier":
            datastore_identifiers.append(self.identifier)
            self.identifier = ''
            self.inIdentifier = False 

    def characters(self, chrs):
        if self.inIdentifier:
            self.identifier += chrs

# Instantiate the parser
parser = xml.sax.make_parser()

# Attach the IATIIdentifierHandler() class and parse downloaded data
parser.setContentHandler(IATIIdentifierHandler())
parser.parse(open('temp/datastore_all_data.xml', 'r'))

# Output sample data to a JSON file in the temp directory
json.dump(datastore_identifiers, open('temp/datastore_identifiers.json', 'w'))

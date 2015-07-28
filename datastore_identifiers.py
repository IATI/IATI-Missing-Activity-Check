import xml.sax
import json

datastore_identifiers = []

class IATIIdentifierHandler(xml.sax.ContentHandler):
    inIdentifier = False
    identifier = ''
    i=0

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

parser = xml.sax.make_parser()
parser.setContentHandler(IATIIdentifierHandler())
parser.parse(open("datastore.xml","r"))

json.dump(datastore_identifiers, open('datastore_iati_identifiers.json', 'w'))

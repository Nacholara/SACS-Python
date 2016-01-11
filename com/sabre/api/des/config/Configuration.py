'''
Created on Nov 27, 2015

@author: SG0946321
'''
from pyDes import triple_des
import base64

class Configuration:
    
    def __init__(self):
        separator = "="
        comment = "#"
        self.rest = {}
        self.encKey = "pqfudkeiurodlpsk" # 16-bytes key

        with open('../config/rest.properties') as f:

            for line in f:
                if separator in line and line[0] != comment:
                    # Find the name and value by splitting the string
                    name, value = line.split(separator, 1)
                    # Assign key value pair to dict
                    # strip() removes white space from the ends of strings
                    self.rest[name.strip()] = value.strip()
       
    def getProperty(self, propertyName):
        return self.rest.get(propertyName)
    
    def getEncryptedProperty(self, propertyName):
        print(base64.b64decode(self.rest.get(propertyName)))
        return triple_des(self.encKey).decrypt(base64.b64decode(self.rest.get(propertyName)), padmode=2)
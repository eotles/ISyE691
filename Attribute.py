'''
Created on Apr 24, 2014

@author: eotles
'''

class Attribute(object):
    '''
    classdocs
    '''


    def __init__(self,collect,name):
        self.name = name
        self.collect = collect
        if(collect):
            self.vals = set()
        #self.name = name
        #self.type = type
    
    def addVal(self,val):
        #print(val + `self.vals`)
        if(self.collect):
            self.vals.add(val)
    
    def getVals(self):
        if(self.collect):
            return self.vals
    
    def toString(self):
        out = ""
        if(self.collect):
            for val in self.vals:
                out = out + val + "/"
        return out
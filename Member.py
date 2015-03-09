'''
Created on Apr 23, 2014

@author: eotles
'''
from Visit import *
from History import *
import test
import math

class Member(object):
    id = None
    sex = ""
    age = ""
    dih = ""
    claims = list()

    def __init__(self, id, sex, age):
        self.id = id
        self.sex = sex
        self.age = age
        self.claims = list()
        self.history = History()
    
    def setY2DIH(self, binary, dih):
        if(dih=="0" or dih ==""):
            self.dih = 0
        elif(binary):
            self.dih = 1
        else:
            self.dih = dih
        
    def addClaim(self, visitData):
        claim = Visit(visitData)
        self.claims.append(claim)
    
    def addVisit(self, dataModel, visit):
        self.history.addVisit(dataModel, visit)
    
    #@classmethod
    #def fromList(cls, info):
    #    #self.id = info[0]
    #    return cls(info[0], info[1], info[2])
    
    def nicePrint(self):
        print(str(self.id) + "\t" + self.sex + "\t" + self.age + "\t" + self.dih)
        #print("\t"+`self.majorityClaim()`)
        
    
    def coallate(self, dataModel, binary):
        self.coallatedHx = self.history.coallate(dataModel, binary)
        #print(self.coallatedHx)
        return self.coallatedHx
    
    def transformDT(self, dataModel, binary):
        out = list()
        out.append(self.id)
        out.append(self.dih)
        out.append(self.sex)
        out.append(self.age)
        out.append(self.history.numVisits())
        out += self.coallate(dataModel, binary)
        #out.append(self.coallate(dataModel))
        #print(out)
        return(out)
    
    def transformPR(self, dataModel, binary):
        out = list()
        out.append(self.id)
        out.append(self.dih)
        if(self.sex=="F"):
            out.append(1)
            out.append(0)
        else:
            out.append(0)
            out.append(1)
        out += self.prAge()
        out += self.prVisit()
        out += self.coallate(dataModel, binary)
        return(out)
    
    def prAge(self):
        ages = ["0-9","10-19","20-29","30-39","40-49","50-59","60-69","70-79", "80+"]
        prAge = [0 for i in ages]
        for index,age in enumerate(ages):
            if(self.age==age):
                prAge[index] = 1
        return prAge

    def prVisit(self):
        prVisit = [0 for i in xrange(40)]
        prVisit[self.history.numVisits()] = 1
        return prVisit
        

    def distance(self, Member):
        dist = 0;
        if(self.sex!=Member.sex):
            dist += 1
        if(self.age!=Member.age):
            dist += 1
        if(self.history.numVisits()!=Member.history.numVisits()):
            dist += 1
        #selfHx = self.coallatedHx
        #for index, val in enumerate(Member.coallatedHx):
        #    dist += (selfHx[index]-val)**2
        return math.sqrt(dist)
    
if __name__ == '__main__':
    test.main()

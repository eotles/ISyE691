'''
Created on Apr 24, 2014

@author: eotles
'''
import Visit
import test

class History(object):


    def __init__(self):
        self.visits = list()
    
    def addVisit(self, dataModel, visit):
        self.visits.append(Visit.Visit(dataModel, visit))
        
    def numVisits(self):
        return len(self.visits)
    
    def disp(self, prefix):
        for visit in self.visits:
            sVisit = visit.toString()
            print(str(prefix) + sVisit)
    
    def coallate(self, dataModel, binary):
        return(self.rowize(self.attrValCount(dataModel),binary))
        
    def attrValCount(self, dataModel):
        attrValCount = [dict() for i in self.visits[0].data]
        for index,attr in enumerate(dataModel):
            #print(attr)
            gotVals = attr.getVals()
            if(gotVals != None):
                for attrVal in gotVals:
                    attrValCount[index].update({attrVal : 0})
        for visit in self.visits:
            for index,attr in enumerate(dataModel):
                gotVals = attr.getVals()
                if(attr.collect):    
                    visitAttrVal = visit.data[index]
                    attrValCount[index].update({visitAttrVal : attrValCount[index].get(visitAttrVal)+1})
        return attrValCount
    
    def rowize(self, attrValCount,binary):
        out = list()
        for attr in attrValCount:
            for attrVal,count in attr.iteritems():
                if(count==0):
                    out.append(0)
                elif(binary):
                    out.append(1)
                else:
                    out.append(count)
        return(out)     
        
    def countClaimAttrVal(self):
        claimsAttrValVotes = [dict() for i in self.claims[0].data]
        for claim in self.claims:
            for i,claimAttrVal in enumerate(claim.data):
                if(claimAttrVal in claimsAttrValVotes[i]):
                    claimsAttrValVotes[i].update({claimAttrVal : claimsAttrValVotes[i].get(claimAttrVal)+1})
                else:
                    claimsAttrValVotes[i].update({claimAttrVal : 1})
        return claimsAttrValVotes
    
    def majorityClaim(self):
        majorityClaim = list()
        countClaimAttrVal = self.countClaimAttrVal()
        for i,claimAttr in enumerate(countClaimAttrVal):
            maxAttrVal = None
            maxAttrCount = 0
            for attrVal, attrValCount in claimAttr.iteritems():
                if(attrValCount >= maxAttrCount):
                    maxAttrVal = attrVal
                    maxAttrCount = attrValCount
            majorityClaim.append(maxAttrVal)
        LoS = 0
        for claim in self.claims:
            #print(claim.LoS)
            if(claim.LoS != ""):
                if("week" in claim.LoS):
                    LoS += 7*int(claim.LoS[0])
                else:
                    LoS += int(claim.LoS.split(" ")[0])
            #if(len(claim.LoS)>len(LoS)):
            #    LoS = claim.LoS
        majorityClaim[8] = LoS
        return(majorityClaim)
                
            
if __name__ == '__main__':
    test.main()  



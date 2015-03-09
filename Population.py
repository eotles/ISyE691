'''
Created on Apr 23, 2014

@author: eotles
'''
import Member
import test
from Visit import *
#import Member

class Population(object):


    def __init__(self):
        self.memberDict = dict()
    
    def loadPop(self, fileName):
        with open(fileName, "r") as f:
            next(f)
            for line in f:
                mInfo = line.strip().split(",")
                mID = int(mInfo[0])
                mTemp = Member.Member(mID, mInfo[1], mInfo[2])
                self.memberDict[mID] = mTemp
        f.close()
    
    def loadY2DIHs(self, binary, fileName):
        with open(fileName, "r") as f:
            next(f)
            for line in f:
                mInfo = line.strip().split(",")
                mID = int(mInfo[0])
                self.memberDict.get(mID).setY2DIH(binary, mInfo[1])
        f.close()
        
    def loadVisits(self, dataModel, fileName):
        with open(fileName, "r") as f:
            next(f)
            for line in f:
                mInfo = line.strip().split(",")
                mID = int(mInfo[0])
                self.memberDict.get(mID).addVisit(dataModel, mInfo[1:])
        f.close()
    
    def dispPop(self):
        for mID, mem in self.memberDict.iteritems():
            mem.nicePrint()
    
    def transformDT(self, dataModel, binary, file):
        for mID, mem in self.memberDict.iteritems():
            file.write(','.join(str(item) for item in mem.transformDT(dataModel, binary)))
            file.write('\n')

    def transformPR(self, dataModel, binary, file):
        for mID, mem in self.memberDict.iteritems():
            file.write(','.join(str(item) for item in mem.transformPR(dataModel, binary)))
            file.write('\n')
    
            
            
if __name__ == '__main__':
    test.main()
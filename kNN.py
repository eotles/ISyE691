'''
Created on Apr 26, 2014

@author: eotles
'''
import random
import sys
import Member
import numpy

class kNN(object):   

    def __init__(self, pop):
        self.pop = pop
        
    def run(self):
        self.split(42, 2)
        self.knnAlg(5, self.dataSets[0], self.dataSets[1])
        
    def split(self, seed, numDataSets):
        random.seed(seed)
        self.dataSets = [list() for i in xrange(numDataSets)]
        for mID, mem in self.pop.memberDict.iteritems():
            dataSetIndex = random.randint(0, numDataSets-1)
            self.dataSets[dataSetIndex].append(mem)
    
    def knnAlg(self, k, trainData, testData):
        hit = 0
        miss= 0
        #minDist = sys.float_info.max
        #maxDist = sys.float_info.min
        #neigbors = [Member() for i in xrange(k)]
        for test in testData:
            neigbors = [0 for i in xrange(k)]
            distances = [sys.float_info.max for i in xrange(k)]
            #minDist = sys.float_info.max
            #maxDist = sys.float_info.min
            for train in trainData:
                dist = test.distance(train)
                if(dist < max(distances)):
                    index = numpy.argmax(distances)
                    distances[index] = dist
                    neigbors[index] = train
            votes = dict()
            for n in neigbors:
                if(votes.has_key(n.dih)):
                    votes.update({n.dih: votes.get(n.dih)+1})
                else:
                    votes.update({n.dih: 1})
            maxDIH = ""
            maxVotes = 0
            for dih,v in votes.iteritems():
                #print(str(dih) + "/" + str(v))
                if(v>maxVotes):
                    maxDIH=dih
                    maxVotes=v
            #print("pred:" + str(maxDIH) + " act:" + str(test.dih))
            if(maxDIH==test.dih):
                hit+=1
            else:
                miss+=1
        print("hit: "+str(hit)+ " miss: " + str(miss) + "acc" + str(float(hit)/(hit+miss)))
                
                    
            
            
        
            
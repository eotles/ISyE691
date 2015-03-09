'''
Created on Apr 23, 2014

@author: eotles
'''
from Member import *
from Population import *
from Attribute import *
from kNN import * 

membersFile = "/Users/eotles/Desktop/Data/HHP/HHP_release1/Members_Y1.csv"
y2DIHFile = "/Users/eotles/Desktop/Data/HHP/HHP_release1/DAyInHospital_Y2.csv"
claimsFile = "/Users/eotles/Desktop/Data/HHP/HHP_release1/Claims_Y1.csv"
outFile = "/Users/eotles/Desktop/transform"
binary = True
outFile += "_bin_" + str(binary)

def main():
    f = open(claimsFile, "r")
    names = f.readline().strip().split(",")
    names = names[1:]
    f.close()
    #print(names)
    collect = [True for i in range(len(names))]
    #print(collect)
    collect[0] = collect[1] = collect[2] = collect[3] = collect[6] = collect[7] = collect[8] =False
    #print(collect)
    visitDM = [Attribute(collect[i],names[i]) for i in xrange(len(names))]
    pop = Population()
    pop.loadPop(membersFile)
    pop.loadY2DIHs(binary, y2DIHFile)
    pop.loadVisits(visitDM, claimsFile)
    #pop.dispPop()
    #for attr in visitDM:
    #    print(attr.toString())
    #print(visitDM)
    #pop.rowize(visitDM)
    makeFileDT(pop, visitDM, binary, outFile)
    #makeFilePR(pop, visitDM, binary, outFile)
    #runKNN(pop)

def makeFileDT(pop, visitDM, binary, outFile):
    fDT = open(outFile + "_DT.csv", "w+")
    dmLabDT(visitDM, fDT)
    pop.transformDT(visitDM, binary, fDT)
    fDT.close()

def makeFilePR(pop, visitDM, binary, outFile):
    fPR = open(outFile + "_PR.csv", "w+")
    pop.transformPR(visitDM, binary, fPR)
    fPR.close()
    
def runKNN(pop):
    x = kNN(pop)
    x.run()

def dmLabDT(dm, file):
    out = list()
    out.append("memberID")
    out.append("dih")
    out.append("sex")
    out.append("age")
    out.append("visit")
    for attr in dm:
        if(attr.collect):
            for attrVal in attr.vals:
                a = str(attr.name)
                a = a.replace(" ","_")
                v = attrVal
                v = v.replace(" ","_")
                name = a +":" + v
                #print(name)
                out.append(name)
    #return out
    file.write(','.join(str(item) for item in out))
    file.write('\n')

if __name__ == '__main__':
    main()
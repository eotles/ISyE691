'''
Created on Apr 26, 2014

@author: eotles
'''

from Attribute import *
import random
from random import choice
folder = "/Users/eotles/Desktop/"
transFileDT = folder +"abbr_DT"
baseFileNameDT = transFileDT + "_split"
transFileDT = transFileDT + ".csv"

transFilePR = folder + "lr_fr_PR"
baseFileNamePR = transFilePR + "_split"
transFilePR = transFilePR + ".csv"

def makeHeader(fileName):
    file = open(fileName, "r")
    firstLine = file.readline().strip().split(",")
    atts = [Attribute(True, name) for name in firstLine[1:]]
    for line in file:
        info = line.strip().split(",")
        for index,attVal in enumerate(info[1:]):
            atts[index].addVal(attVal)
    file.close()
    sOut = ""
    for index,att in enumerate(atts):
        if(index==0):
            sOut += "%%" + commaSep(att.getVals())
            sOut += "\n" + str(len(atts)-1)
        else:
            sOut += "##" + att.name + " " + commaSep(att.getVals())
        sOut += "\n"
    return sOut

def commaSep(list):
    return(','.join(str(item) for item in list))

def putInFile(data, file):
    file.write(commaSep(data))
    file.write("\n")

def makeFileDT(seed, transFile, numFiles):
    random.seed(seed)
    #rng.seed(seed)
    outFiles = [open(baseFileNameDT+"_"+str(i), "w+") for i in xrange(numFiles)]
    header = makeHeader(transFile)
    print(header)
    for file in outFiles:
        file.write(header)
    inFile = open(transFile, "r")
    next(inFile)
    for line in inFile:
        data = line.strip().split(",")
        data = data[1:]
        outFileIndex = random.randint(0,numFiles-1)
        print(data)
        print(outFileIndex)
        putInFile(data, outFiles[outFileIndex])
    inFile.close()
    for file in outFiles:
        file.close()

def makeFileDTLim(seed, transFile, lAmounts, names):
    random.seed(seed)
    numFiles = len(lAmounts)
    #rng.seed(seed)
    outFiles = [open(baseFileNameDT+"_"+names[i]+"_"+str(lAmounts[i]), "w+") for i in xrange(numFiles)]
    rndList = rndLists(transFile, 1, lAmounts)
    header = makeHeader(transFile)
    #print(header)
    for file in outFiles:
        file.write(header)
    inFile = open(transFile, "r")
    next(inFile)
    for i,line in enumerate(inFile):
        data = line.strip().split(",")
        data = data[1:]
        #outFileIndex = random.randint(0,numFiles-1)
        for outFileIndex,outFileIndexList in enumerate(rndList):
            if(outFileIndexList):
                if(i==outFileIndexList[0]):
                    outFileIndexList.remove(i)
                    #print(data)
                    #print(outFileIndex)
                    putInFile(data, outFiles[outFileIndex])
    inFile.close()
    for file in outFiles:
        file.close()

def makeFilePR(seed, transFile, numFiles):
    random.seed(seed)
    outFiles = [open(baseFileNamePR+"_"+str(i), "w+") for i in xrange(numFiles)]
    inFile = open(transFile, "r")
    for line in inFile:
        data = line.strip().split(",")
        data = data[1:]
        outFileIndex = random.randint(0,numFiles-1)
        print(data)
        print(outFileIndex)
        putInFile(data, outFiles[outFileIndex])
    inFile.close()
    for file in outFiles:
        file.close()

def makeFilePRLim(seed, transFile, lAmounts, names):
    random.seed(seed)
    numFiles = len(lAmounts)
    outFiles = [open(baseFileNamePR+"_"+names[i]+"_"+str(lAmounts[i]), "w+") for i in xrange(numFiles)]
    rndList = rndLists(transFile, 1, lAmounts)
    inFile = open(transFile, "r")
    for i,line in enumerate(inFile):
        data = line.strip().split(",")
        data = data[1:]
        for outFileIndex,outFileIndexList in enumerate(rndList):
            if(outFileIndexList):
                if(i==outFileIndexList[0]):
                    outFileIndexList.remove(i)
                    #outFileIndex = random.randint(0,numFiles-1)
                    #print(data)
                    #print(outFileIndex)
                    putInFile(data, outFiles[outFileIndex])
    inFile.close()
    for file in outFiles:
        file.close()

def rndLists(transFile,start,lAmounts):
    length = lineCount(transFile)
    indices = [i for i in xrange(start,length)]
    rnd = [list() for _ in lAmounts]
    for i,amount in enumerate(lAmounts):
        for _ in xrange(amount):
            ind = choice(indices)
            rnd[i].append(ind)
            indices.remove(ind)
        rnd[i].sort()
    print(rnd)     
    #print(indices)
    return(rnd)

def lineCount(transFile):
    with open(transFile) as f:
        for i, l in enumerate(f):
            pass
    f.close()
    return i+1

def main():
    #makeFileDT(42, transFile, 3)
    #makeFilePR(42, transFile, 2)
    makeFileDTLim(42, transFileDT, [500,10000,20000], ["train", "tune", "test"])
    #makeFilePRLim(42, transFilePR, [20000,10000,20000], ["train", "tune", "test"])

if __name__ == '__main__':
    main()
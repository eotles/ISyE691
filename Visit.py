'''
Created on Apr 23, 2014

@author: eotles
'''

from Attribute import *
import test

class Visit(object):
    
    #dataModel = [Attribute(True) for i in range(11)]
    #dataModel.append(Attribute("MemberID","ID"))   #memberID
    #dataModel.append(Attribute("ProviderID","ID"))   #providerID
    #dataModel.append(Attribute("Vendor","ID"))   #vendor
    #dataModel.append(Attribute("PCP","ID"))   #pcp
    #dataModel.append(Attribute("Year","STR"))  #Year
    #dataModel.append(Attribute("Specialty","STR"))  #Specialty
    #dataModel.append(Attribute("Places","STR"))  #Places
    #dataModel.append(Attribute("PayDelay","STR"))  #Paydelay
    #dataModel.append(Attribute("LoS","TRANGE"))  #LoS
    #dataModel.append(Attribute("dsfs","STR"))  #DSFS
    #dataModel.append(Attribute("PrimaryCondition","STR"))  #primaryCondition
   # dataModel.append(Attribute("CharlsonIndex","STR"))  #charlsonIndex  
    member = ""
    provider = ""
    vendor = ""
    pcp = ""
    year = ""
    specialty = ""
    placesvc = "" 
    paydelay = ""
    LoS = ""
    dsfs = ""
    primaryConditionGroup = ""
    charlsonsIndex = ""

    def __init__(self, dataModel, visitData):
        
        self.dataModel = dataModel
        self.data = self.fixData(visitData)
        for index,attrVal in enumerate(visitData):
            dataModel[index].addVal(attrVal)
            #print("add val: "+ attrVal)
        #self.member = visitData[0]
        self.provider = self.data[0]
        self.vendor = self.data[1]
        self.pcp = self.data[2]
        self.year = self.data[3]
        self.specialty = self.data[4]
        self.placesvc = self.data[5]
        self.paydelay = self.data[6]
        self.LoS = self.data[7]
        self.dsfs = self.data[8]
        self.primaryConditionGroup = self.data[9]
        self.charlsonsIndex = self.data[10]
    
    def toString(self):
        out = "\t" + self.provider + "\t" + self.vendor + "\t" + self.pcp + "\t" + self.year + "\t" + self.specialty + "\t" + self.placesvc + "\t" + self.paydelay + "\t" + self.LoS + "\t" + self.dsfs + "\t" + self.primaryConditionGroup + "\t" + self.charlsonsIndex
        return(out)

    def getDataModel(self):
        return self.dataModel

    def fixData(self,data):
        #print(data[6])
        paydelay = data[6].strip()
        if(len(paydelay)>0):
            data[6] = str((1+int(paydelay)/7))
        else:
            data[6] = "NA"
        return data
        
 
if __name__ == '__main__':
    test.main()       
        
        
    
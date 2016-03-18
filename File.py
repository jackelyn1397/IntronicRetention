
#import cProfile

#creates a LinkedList class
class LinkedList :
    #Initializes the linked list object
    #param name   the name of the linked list
    #param first  the first node in the linked list
    #param last   the last node in the linked list
    def __init__(self, name, first, last) :
        self.name=name
        self.first=first
        self.last=last
    
    #returns the name of the linked list
    def getName(self) :
        return self.name
    
    #sets the name of the linked list to param name, returns the new name
    def setName(self, name) :
        self.name=name
        return self.name
    
    #returns the first node of the linked list
    def getFirst(self) :
        return self.first
    
    #sets the first node of the linked list to param first, returns the new first node
    def setFirst(self, first) :
        self.first=first
        return self.first
    
    #returns the last node of the linked list
    def getLast(self) :
        return self.last
    
    #sets the last node of the linked list to param last, returns the new last node
    def setLast(self, last) :
        self.last=last
        return self.last
    
    #sets the last node of the linked list to param nextNode when there is already a last node, returns the new last node
    def addNode(self, nextNode) :
        self.last.setNext(nextNode)
        self.last=nextNode
    
    #removes the last node of the linked list
    def removeEnd(self, endNode) :
        if endNode!=self.getFirst() :
            newLast=endNode.getPrevious()
            newLast.setNext(None)
            self.setLast(newLast)
        else :                          #if there is only one node in the linked list
            self.setFirst(None)
            self.setLast(None)


class GeneNode:
    #initializes the GeneNode object
    #param value   the name of the gene or transcript
    #param list    a LinkedList object holding transcripts or exons/introns
    #param next    the next node in the LinkedList
    def __init__(self, value, list, index, upstream, downstream) :
        self.value=value
        self.list=list
        self.index=index
        self.next=next
        self.upstream=upstream
        self.downstream=downstream
    
    #returns the name of the gene/transcript
    def getValue(self) :
        return self.value
    
    #sets the name of the gene/transcript to param value, returns the new name
    def setValue(self, value) :
        self.value=value
        return self.value
    
    #returns the LinkedList containing transcripts/introns
    def getList(self) :
        return self.list
    
    #sets the list variable to a LinkedList object, returns the new list
    def setList(self, list):
        self.list=list
        return self.list
    
    def getIndex(self):
        return self.index
    
    def setIndex(self, index):
        self.index=index
        return self.index
    
    #gets the most upstream intron start point in the gene
    def getUpstream(self):
        return self.upstream
    
    #sets the most upstream intron start point in the gene to param num, returns the new upstream boundary
    def setUpstream(self,num):
        self.upstream=num
        return self.upstream
    
    #gets the most downstream intron end point in the gene
    def getDownstream(self) :
        return self.downstream
    
    #sets the most downstream intron end point in the gene to param num, returns the new downstream boundary
    def setDownstream(self,num) :
        self.downstream=num
        return self.downstream


class TransNode:
    #initializes the GeneNode object
    #param value   the name of the gene or transcript
    #param list    a LinkedList object holding transcripts or exons/introns
    #param next    the next node in the LinkedList
    def __init__(self, value, list, next) :
        self.value=value
        self.list=list
        self.next=next
        self.boundaries=[None,None]        #the upstream (boundaries[0]) and downstream (boundaries[1] intron) boundaries for genes
    
    #returns the name of the gene/transcript
    def getValue(self) :
        return self.value
    
    #sets the name of the gene/transcript to param value, returns the new name
    def setValue(self, value) :
        self.value=value
        return self.value
    
    #returns the LinkedList containing transcripts/introns
    def getList(self) :
        return self.list
    
    #sets the list variable to a LinkedList object, returns the new list
    def setList(self, list):
        self.list=list
        return self.list
    
    #returns the next node in the LinkedList
    def getNext(self) :
        return self.next
    
    #sets the next node in the LinkedList, returns the new next node
    def setNext(self, next) :
        self.next=next
        return self.next

#creates a LinkedList node object for exons and introns
class ExonNode:
    #initializes the ExonNode object
    #param start     the start point of the exon/intron
    #param end       the end point of the exon/intron
    #param previous  the previous node in the LinkedList
    #param next      the next node in the LinkedList
    def __init__(self, start, end, previous, next) :
        self.start=start
        self.end=end
        self.next=next
        self.previous=previous
    
    #returns the start point of the exon/intron
    def getStart(self) :
        return self.start
    
    #sets the start point of the exon/intron to param start, returns the new start point
    def setStart(self, start) :
        self.start=start
        return self.start
    
    #returns the end point of the exon/intron
    def getEnd(self) :
        return self.end
    
    #sets the end point of the exon/intron to param end, returns the new end point
    def setEnd(self, end) :
        self.end=end
        return self.end
    
    #gets the next node in the LinkedList
    def getNext(self) :
        return self.next
    
    #sets the next node in the LinkedList to param next, returns the new next node
    def setNext(self, next) :
        self.next=next
        return self.next
    
    #gets the previous node in the LinkedList
    def getPrevious(self) :
        return self.previous
    
    #sets the previous node in the LinkedList to param previous, returns the new previous node
    def setPrevious(self, previous) :
        self.previous=previous
        return self.previous





#prints out a 3D list in a sequential format
def printList(chrList) :
    for x in range(1,25) :                                                          #cycles through the chromosome list
        if x==23:                                                                   #prints CHRX instead of CHR23
            print "CHRX"
        elif x==24:                                                                 #prints CHRY instead of CHR24
            print "CHRY"
        else:
            print "CHR"+str(x)                                                      #prints the chromosome number
        geneList=chrList[x]                                                             #gets the first gene in the chromosome
        if geneList!=[] and geneList[0]!=None:
            for y in range(0,len(geneList)):                                                           #cycles through all the genes in the chromosome
                print("--"+geneList[y].getValue()+"\t"+str(geneList[y].getIndex()))                                             #prints the indented gene name
                transcript=geneList[y].getList().getFirst()                                    #gets the first transcript of the gene
                while transcript!=None:                                                 #cycles through all transcripts of the gene
                    print("----"+transcript.getValue())                                 #prints the indented transcript name
                    exon=transcript.getList().getFirst()                                #gets the first exon of the gene (intron can be substituted for exon)
                    while exon!=None :                                                  #cycles through all the exons in the transcript
                        print("------"+str(exon.getStart())+", "+str(exon.getEnd()))    #prints the indented start and end points of the exon
                        exon=exon.getNext()                                             #moves onto the next exon
                    transcript=transcript.getNext()                                     #moves onto the next transcript


#adds an exon node into a transcript's exon list
#param exonList  the exon list of the transcript
#param start     the start point of the exon
#param end       the end point of the exon
def addExon(exonList,start,end):
    node=exonList.getFirst()                                        #gets the first node in the exon list
    if node==None :                                                 #if there is no first node
        x=exonList.setFirst(ExonNode(start,end,None,None))          #creates a new exon node
        exonList.setLast(x)                                         #sets the last node to the new node
    else :                                                          #if there is a first node
        while node!=None :                                          #cycles through transcript's recorded exons
            prevEnd=node.getEnd()                                   #sets the current exon's end pos to "prevEnd"
            if prevEnd < start :                                    #if end of the exon is upstream of this start
                nextNode=node.getNext()                             #retrieves the next node in the exon list
                if(nextNode==None) :                                #if there is no next node
                    newNode=ExonNode(start,end,node,None)           #creates new exon node setting only previous
                    node.setNext(newNode)                           #sets current node's next to new node
                    exonList.setLast(newNode)                       #sets the last exon to the new exon
                    node=exonList.getLast()                         #stops cycling through loop
                elif nextNode.getStart() > end :                    #if next exon's start is downstream of end
                    newNode=ExonNode(start,end,node,nextNode)       #creates new exon, sets previous and next
                    node.setNext(newNode)                           #current node's next is now the new exon
                    nextNode.setPrevious(newNode)                   #next node's previous is now new exon
                    node=exonList.getLast()                         #stops cycling through loop
            node=node.getNext()                                     #moves on to next node in exon list


#attempts to add a transcript into a gene's transcript list
#param transList   the gene's transcript list
#param transcript  a string containing the name of the gene's transcript
#param start       the start of a particular exon in the transcript
#param end         the end of a particular exon in the transcript
def addTranscript(transList,transcript,start,end) :
    node=transList.getFirst()                                       #gets the first node in the transcript list
    if node==None :                                                 #if there is no first node
        exonList=LinkedList("exons",None,None)                      #creates a new exon list
        x=transList.setFirst(TransNode(transcript,exonList,None))    #creates a new transcript node with exon list
        addExon(exonList,start,end)                                 #adds exon to exon list
        transList.setLast(x)                                        #sets last node to the new node
    else:                                                           #if there is a first node
        alreadyTrans=False                                          #assumption that transcript is not in list
        while node!=None :                                          #cycles through transcript list
            if node.getValue()==transcript :                        #if transcript already in list
                alreadyTrans=True                                   #changes variable to true
                exonList=node.getList()                             #gets the exon list of the transcript node
                addExon(exonList,start,end)                         #adds the new exon to the exon list
                node=transList.getLast()                            #stops cycling through loop
            node=node.getNext()                                     #moves on to next node
        if alreadyTrans==False:                                     #if transcript not in transcript list
            exonList=LinkedList("exons",None,None)                  #creates new exon list
            newNode=TransNode(transcript,exonList,None)              #creates new transcript node with exon list
            transList.addNode(newNode)                              #adds new node to transcript list
            addExon(exonList,start,end)                             #adds exon to new exon list


def addGenes() :
    #file=None                                                                   #opens a specified file
    #if EXONS_FILE!=None:
    #file=open(EXONS_FILE)
    #else :
    file=open("/Users/admin/Desktop/sampleOutput/exons.txt")
    count=0
    chrList=["place0"]                                                          #creates a new chromosome list
    for x in range(1,25):                                                       #cycles through all possible chromosomes
        if x==23:                                                               #sets index number 23 as chrX
            chrList.append([None])
        elif x==24:                                                             #sets index number 24 as chrX
            chrList.append([None])
        else:
            chrList.append([None])            #creates a new LinkedList for the genes of each chromosome
    line=file.readline().rstrip('\n').replace('"','').replace(';','')           #reads in a line and removes any edits
    while line!="" :                                                            #while end of file has not been reached
        features=line.split("\t")                                               #split columns
        gene=features[3]                                                        #gets gene from columns
        transcript=features[4]                                                  #gets transcript from columns
        start=int(features[1])                                                  #gets start of exon
        end=int(features[2])                                                    #gets end of exon
        chr=features[0]                                                         #gets gene's chromosome
        if len(chr)<=5:                                                         #ignores all contigs
            indexNum=0                                                          #initializes a chromosome number
            if len(chr)==5 :                                                    #gets double digit chromosome numbers
                indexNum=chr[3:5]
            else:
                indexNum=chr[3:4]                                               #gets single digit chromosome numbers
            if indexNum=="X":                                                   #changes X chromosome number to list compatible 23
                indexNum=23
            elif indexNum=="Y":                                                 #changes Y chromosome number to list compatible 23
                indexNum=24
            else :
                indexNum=int(indexNum)                                          #changes indexNum to an integer
            if indexNum!=0:                                                     #if chromosome number is valid
                geneList=chrList[indexNum]                               #sets variable node as first node
                if geneList[0]==None :                                                 #if list is empty
                    transList=LinkedList("transcripts",None,None)                     #creates transcript LinkedList
                    geneList[0]=GeneNode(gene,transList,None,None,None)
                    addTranscript(transList,transcript,start,end)               #adds a transcript to the node
                else:                                                           #if list is not empty
                    alreadyGene=False                                           #initial assumption that gene is not in list
                    for x in range(0,len(geneList)):                                          #circles through all nodes in linked list
                        if geneList[x].getValue()==gene :                              #if gene already in list
                            alreadyGene=True                                    #sets variable to true
                            transList=geneList[x].getList()                            #gets the transcript LinkedList of the gene
                            addTranscript(transList,transcript,start,end)       #attempts to add a transcript to the gene
                            x=len(geneList)                    #effectively stops the while loop
                    if alreadyGene==False :                                     #if no instances of gene is found
                        transList=LinkedList("transcripts",None,None)           #creates new transcript LinkedList
                        newNode=GeneNode(gene,transList,None,None,None)                   #creates a node with gene as value
                        geneList.append(newNode)                      #adds node to list
                        addTranscript(transList,transcript,start,end)           #adds transcript to transcript list
        count+=1
        if count%1000==0:
            print "addGenes: "+str(count)+" lines processed."
        line=file.readline().rstrip('\n').replace('"','').replace(';','')       #reads in next line
    #printList(chrList)
    return chrList

#sets the most upstream and downstream intron base pair boundary for a gene
#param gene  the specified gene to set boundaries
def setBoundaries(gene):
    upstream=None                                                       #initializes the upstream boundary
    downstream=None                                                     #initializes the downstream boundary
    transcript=gene.getList().getFirst()                                #gets the first transcript of the gene
    while transcript!=None :                                            #cycles through all transcripts of the gene
        intron=transcript.getList().getFirst()                          #gets the first intron of the transcript
        while intron!=None:                                             #cycles through all introns of the transcript
            if upstream==None or intron.getStart()<upstream:            #if the start of the intron is the most upstream
                upstream=intron.getStart()                              #sets the start point to upstream variable
            if downstream==None or intron.getEnd()>downstream:          #if the end of the intron is the most downstream
                downstream=intron.getEnd()                              #sets the end point to downstream variable
            intron=intron.getNext()                                     #moves onto the next intron
        transcript=transcript.getNext()                                 #moves onto the next transcript
    gene.setUpstream(upstream)                                          #sets the upstream variable
    gene.setDownstream(downstream)                                      #sets the downstream variable



#changes all exons in a 3D linked list to introns, prints out and returns the new list
#param list  the linked list containing exons
def getIntrons(chrList) :
    for x in range(1,25):                                               #cycles through all chromosomes
        print "getIntrons: Running CHR"+str(x)
        geneList=chrList[x]                                      #gets the first gene in the chromosome list
        if geneList[0]!=None:
            for y in range(0,len(geneList)) :                                              #loops through every gene in the list
                transcript=geneList[y].getList().getFirst()                        #gets first transcript in gene's trans list
                while transcript!=None:                                     #loops through every transcript in list
                    exon=transcript.getList().getFirst()                    #gets first exon in transcript's exon list
                    while exon!=None :                                      #loops through every exon in the list
                        endPrevExon=exon.getEnd()                           #gets the end of the current exon
                        startIntron=endPrevExon+1                           #sets the start of intron to endPrevExon+1
                        if(exon.getNext()!=None) :                          #if there is a next exon
                            startNextExon=exon.getNext().getStart()         #gets the start of the next exon
                            endIntron=startNextExon-1                       #sets the end of intron to startNextExon-1
                            exon.setStart(startIntron)                      #changes the exon to intron: start
                            exon.setEnd(endIntron)                          #changes exon to intron: end
                        else :                                              #if there is no next exon
                            if exon!=transcript.getList().getFirst() :      #if there is more than one exon in transcript
                                exon=exon.getPrevious()                     #remove the last exon in the list
                                transcript.getList().removeEnd(exon.getNext())
                            else :                                          #if there is only one exon in transcript
                                transcript.getList().removeEnd(exon)        #remove that exon, since no possible introns
                        exon=exon.getNext()                                 #moves to next exon
                    transcript=transcript.getNext()                         #moves to next transcript
                setBoundaries(geneList[y])
            geneList.sort(key=lambda gene: (gene.upstream, gene.downstream))
            while geneList!=[] and geneList[0].getUpstream()==None :
                del geneList[0]
            for z in range(0,len(geneList)):
                geneList[z].setIndex(z)
    #printList(chrList)
    return chrList


def binarySearchStart(geneList, start):
    #print "read: "+str(start)+"\t"+str(end)
    #geneList.sort(key=lambda gene: (gene.downstream, gene.upstream))
    #geneNode=None
    low=0
    high=len(geneList)-1
    mid=int(round((high+low)/2))
    #print str(low)+"\t"+str(high)+"\t"+str(mid)+"\t"+geneList[mid].getValue()
    while low<=high:
        #print str(low)+"\t"+str(high)+"\t"+str(mid)+"\t"+geneList[mid].getValue()+"\t"+str(geneList[mid].getDownstream())+"\t"+str(geneList[mid+1].getDownstream())
        if geneList[mid].getDownstream()>start and (geneList[mid-1].getDownstream()<start or geneList[mid-1].getDownstream()==start):
            #geneNode=geneList[mid]
            #print "start: "+str(geneList[mid].getUpstream())+"\t"+str(geneList[mid].getDownstream())+"\t"+geneList[mid].getValue()
            return mid
        elif geneList[mid].getDownstream()<=start:
            low=mid+1
            #print "less"
        else:
            high=mid-1
            #print "greater"
        mid=int(round((high+low)/2))
        #print str(low)+"\t"+str(high)+"\t"+str(mid)+"\t"+geneList[mid].getValue()
        if mid<=0:
            mid=0
            if geneList[mid].getUpstream()<start and geneList[mid].getDownstream()>start:
                #geneNode=geneList[mid]
                return mid
            else:
                #print "not found"
                return None
    #print "Not found"
    return None



def binarySearchEnd(geneList, end):
    #print "read: "+str(start)+"\t"+str(end)
    #geneNode=None
    #geneList.sort(key=lambda gene: (gene.upstream, gene.downstream))
    low=0
    high=len(geneList)-1
    mid=int(round((high+low)/2))
    while low<=high:
        #print str(low)+"\t"+str(high)+"\t"+str(mid)+"\t"+geneList[mid].getValue()+"\t"+str(geneList[mid].getUpstream())+"\t"+str(geneList[mid+1].getUpstream())
        if geneList[mid].getUpstream()<end and (geneList[mid+1].getUpstream()>end or geneList[mid+1].getUpstream()==end):
            #geneNode=geneList[mid]
            #print "end: "+str(geneList[mid].getUpstream())+"\t"+str(geneList[mid].getDownstream())+"\t"+geneList[mid].getValue()
            return geneList[mid]
        elif geneList[mid].getUpstream()>=end:
            high=mid-1
            #print str(geneList[mid].getUpstream())+"\t"+str(end)
            #print "greater"
        else:
            low=mid+1
            #print str(geneList[mid].getUpstream())+"\t"+str(end)
            #print "less"
        mid=int(round((high+low)/2))
        #print str(low)+"\t"+str(high)+"\t"+str(mid)
        if mid>=len(geneList)-1 :
            mid=len(geneList)-1
            #if geneList[mid].getUpstream()<end and geneList[mid].getDownstream()>end:
                #geneNode=geneList[mid]
            return geneList[mid]
            #else:
                #print "not found"
                #return None
    #print "Not found"
    return None



#searches the gene for all introns the read aligns to, outputs only the instances where the read aligns to the same intron in all transcripts of the gene
#param geneNode     the gene to search
#param read         the read ID
#param chr          the chromosome of the gene/read
#param start        the start point of the read
#param end          the end point of the read
#param myFile       the output file to print out intronic reads
def searchTranscript(geneNode, read, chr, start, end, myFile):
    checkStart=start+2                                              #makes sure there is a true alignment
    checkEnd=end-2
    transcript=geneNode.getList().getFirst()                        #gets the first transcript of the gene
    transCheck=[]                                                   #creates an array to hold intron boundary verifiers
    intronCheck=False                                               #creates a boolean to indentify the alignment status of each transcript
    while transcript!=None:                                         #cycles through the transcripts in the gene
        intron=transcript.getList().getFirst()                      #gets the first intron of the transcript
        if intron!=None:                                            #if there are introns
            check=transcript.getList().getLast()                    #gets the last intron of the transcript
            if (start>intron.getStart() and start<check.getEnd()) or (end>intron.getStart() and end<check.getEnd()) :        #if the read is within transcript boundaries
                while intron!=None :                                #cycles through all introns of the transcript
                    if (checkStart>intron.getStart() and checkStart<intron.getEnd()) or (checkEnd>intron.getStart() and checkEnd<intron.getEnd()):   #if start or the end of read is well within an intron boundary
                        if transCheck==[] and intronCheck==False:   #if this is the first transcript
                            transCheck.append(intron.getStart())    #adds the aligned intron boundaries to transCheck[0] and [1]
                            transCheck.append(intron.getEnd())
                            intronCheck=True                        #changes the boolean to true
                        elif intronCheck==False:                    #if this is not the first transcript and another intron has not already been found in the transcript
                            if intron.getStart()==transCheck[0] and intron.getEnd()==transCheck[1]:         #if the intron boundaries are the same as other transcripts
                                intronCheck=True                    #changes the boolean to true
                    intron=intron.getNext()                         #moves onto the next intron
            else:                                                   #if the read is not within transcript boundaries
                transCheck=[]                                       #remove any intron boundaries in the array
        else:                                                       #if there are no introns in the transcript
            transCheck=[]                                           #remove any intron boundaries in the array
        if transCheck==[] or intronCheck==False:                    #if there are no boundaries in the array or the boolean is false (didn't find any introns aligning to read)
            transCheck=[]                                           #removes any boundaries from array
            transcript=geneNode.getList().getLast()                 #moves straight to the last transcript (ends the loop)
        transcript=transcript.getNext()                             #moves to the next transcript
        intronCheck=False                                           #changes the boolean back to false to test the next transcript
    if transCheck!=[]:                                              #if there are boundaries in the array
        myFile.write(read.rstrip("2")+"\t"+chr+"\t"+str(start)+"\t"+str(end)+"\t"+geneNode.getValue()+"\t"+str(transCheck[0])+"\t"+str(transCheck[1])+"\n")         #print features to output file



def searchTranscript2(geneNode, read, chr, start, end, myFile):
    transcript=geneNode.getList().getFirst()                                                                                #gets the first transcript of the gene
    while transcript!=None:                             #cycles through all transcripts of the gene
        intron=transcript.getList().getFirst()          #gets the first intron of the transcript
        if intron!=None:                                #if there are introns
            check=transcript.getList().getLast()        #gets the last intron of the transcript
            if (start>intron.getStart() and start<check.getEnd()) or (end>intron.getStart() and end<check.getEnd()) :        #if the read is within transcript boundaries
                while intron!=None :                    #cycles through all introns of the transcript
                    if (start>intron.getStart() and start<intron.getEnd()) or (end>intron.getStart() and end<intron.getEnd()):
                        myFile.write(read.rstrip("2")+"\t"+chr+"\t"+str(start)+"\t"+str(end)+"\t"+geneNode.getValue()+"\t"+transcript.getValue()+"\t"+str(intron.getStart())+"\t"+str(intron.getEnd())+"\n")                          #prints features
                    intron=intron.getNext()             #moves to the next intron
        transcript=transcript.getNext()                 #moves to the next transcript



#checks to see if any reads in the output file contain introns
#param list  the intron list built previously
def parseReads(chrList):
    file=open("/Users/admin/Desktop/miltest.txt")       #/Users/admin/Desktop/sampleOutput_Linda/PLoS_One_2012data_cutAdapt/orig/genome/lane1_2_genome_output.sam
    count=0
    myFile=open("/Users/admin/Desktop/2binary5.txt","a")
    #myFile=None                                                     #opens file to store output values
    #myFile=open("/Users/admin/Desktop/pleasework2.txt","a")
    line=None                                                       #creates line variable
    for x in range (0,3):                                           #skips over documentation lines
        line=file.readline().rstrip("\n")
        x+=1
    while line!="" :                                                #reads through the end of the file
        features=line.split("\t")                                   #seperates the features of each read
        read=features[0]                                            #sets the read name
        #chr=features[1]
        chr=features[2]                                             #sets the chromosome
        #start=int(features[2])                                      #sets the start point of the read
        start=int(features[3])
        #end=int(features[3])                                 #sets the end point of the read
        end=len(features[9])+start-1
        #checkStart=start+2
        #checkEnd=end-2
        #print (read+", "+chr+", "+str(start)+", "+str(end))
        if chr!="chrM":                                             #ignores all mitochondrial DNA
            indexNum=0                                              #sets a chromosome number
            if len(chr)==5 :                                        #gets two digit chromosome numbers
                indexNum=chr[3:5]
            else:
                indexNum=chr[3:4]                                   #gets single digit chromosome numbers
            if indexNum=="X":                                       #changes X chromosome number to list compatible 23
                indexNum=23
            elif indexNum=="Y":                                     #changes Y chromosome number to list compatible 24
                indexNum=24
            else :
                indexNum=int(indexNum)                              #changes indexNum to an integer
            geneList=chrList[indexNum]                            #gets the first gene in the chromosome list
            geneNode=None
            if geneList!=[] and geneList[0]!=None :                                      #cycles through all genes
                #printList(chrList)
                geneNode=binarySearchEnd(geneList, end)
                if geneNode!=None:
                    endIndex=geneNode.getIndex()
                    startIndex=endIndex
                    #print "endIndex: "+str(endIndex)
                    geneList2=geneList[0:endIndex+1]
                    geneList2.sort(key=lambda gene: (gene.downstream, gene.upstream))
                    #printList(chrList)
                    reverseIndex=binarySearchStart(geneList2, start)
                    #print "reverseIndex: "+str(reverseIndex)
                    if reverseIndex!=None:
                        startIndex=reverseIndex
                        #print "startIndex: "+str(startIndex)
                        for x in range(reverseIndex,endIndex+1):
                            if geneList2[x].getIndex()<startIndex:
                                #print x
                                startIndex=geneList2[x].getIndex()
                    #print "newstartIndex: "+str(startIndex)
                    geneList.sort(key=lambda gene: (gene.upstream, gene.downstream))
                    if startIndex<=endIndex:
                        for x in range(startIndex,endIndex+1):
                            #print x
                            searchTranscript2(geneList[x], read, chr, start, end, myFile)

        count+=1
        if count%1000==0:
            print "parseReads: "+str(count)+" lines processed."
        line=file.readline().rstrip("\n")                           #gets the next read line



#import datetime
#print datetime.datetime.now()

chrList=addGenes()
chrList=getIntrons(chrList)
#cProfile.run('parseReads(chrList)', 'read3.prof')
parseReads(chrList)
print "end"

#print datetime.datetime.now()


#file=open("/Users/admin/Desktop/intronicReads2.txt")
#file2=open("/Users/admin/Desktop/2binary3.txt")
#line=file.readline().rstrip("\n")
#line2=file2.readline().rstrip("\n")
#count=0
#while line!="" and line2!="" :
    #features=line.split("\t")
    #features2=line2.split("\t")
    #read=features[0]
    #read2=features2[0]
    #line=file.readline().rstrip("\n")
    #line2=file2.readline().rstrip("\n")
    #if count%1000==0:
        #print count
    #if read!=read2:
        #print read+"\t"+read2
        #line=""
    #count+=1





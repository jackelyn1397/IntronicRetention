
#import cProfile
#import math

PARENT_DIR=None             #var1
EXONS_FILE=None             #var2
GENOME_FILE=None            #var3
CIRCPASSED_FILE=None        #var4
import sys
#print sys.argv
if len(sys.argv)>1:
    PARENT_DIR=sys.argv[1]
if len(sys.argv)>2:
    EXONS_FILE=sys.argv[2]
if len(sys.argv)>3:
    GENOME_FILE=sys.argv[3]
if len(sys.argv)>4:
    CIRCPASSED_FILE=sys.argv[4]

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
    #param value       the name of the gene or transcript
    #param list        a LinkedList object holding transcripts or exons/introns
    #param index       the index of the node in the gene list of a chromosome (sorted by upstream)
    #param upstream    the most upstream intron start point of the gene
    #param downstream  the most downstream intron end point of the gene
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
    
    #gets the index of the GeneNode in the gene list
    def getIndex(self):
        return self.index
    
    #sets the index of the GeneNode in the gene list
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
    for x in range(1,25) :                                                              #cycles through the chromosome list
        if x==23:                                                                       #prints CHRX instead of CHR23
            print "CHRX"
        elif x==24:                                                                     #prints CHRY instead of CHR24
            print "CHRY"
        else:
            print "CHR"+str(x)                                                          #prints the chromosome number
        geneList=chrList[x]                                                             #gets the first gene in the chromosome
        if geneList!=[] and geneList[0]!=None:                                          #if there are genes in the gene list
            for y in range(0,len(geneList)):                                            #cycles through all the genes in the chromosome
                print("--"+geneList[y].getValue()+"\t"+str(geneList[y].getIndex()))     #prints the indented gene name
                transcript=geneList[y].getList().getFirst()                             #gets the first transcript of the gene
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



#adds all genes and their corresponding transcripts and exons in a file to a 3D linked list, prints out and returns the list
def addGenes() :
    file=None                                                                   #opens exon file
    if EXONS_FILE!=None:
        file=open(EXONS_FILE)
    else :
        file=open("/Users/admin/Desktop/sampleOutput/exons.txt")
    count=0
    chrList=["place0"]                                                          #creates a new chromosome list
    for x in range(1,25):                                                       #cycles through all possible chromosomes
        chrList.append([None])                                                  #creates a new index for the genes of each chromosome
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
                geneList=chrList[indexNum]                                      #gets value of the chrList at indexNum, the gene list of the specific chromosome
                if geneList[0]==None :                                          #if list is empty
                    transList=LinkedList("transcripts",None,None)               #creates transcript LinkedList
                    geneList[0]=GeneNode(gene,transList,None,None,None)         #sets the first index to a new GeneNode
                    addTranscript(transList,transcript,start,end)               #adds a transcript to the new node
                else:                                                           #if list is not empty
                    alreadyGene=False                                           #initial assumption that gene is not in list
                    for x in range(0,len(geneList)):                            #circles through all nodes in linked list
                        if geneList[x].getValue()==gene :                       #if gene already in list
                            alreadyGene=True                                    #sets variable to true
                            transList=geneList[x].getList()                     #gets the transcript LinkedList of the gene
                            addTranscript(transList,transcript,start,end)       #attempts to add a transcript to the gene
                            x=len(geneList)                                     #effectively stops the while loop
                    if alreadyGene==False :                                     #if the gene is not found in the list
                        transList=LinkedList("transcripts",None,None)           #creates new transcript LinkedList
                        newNode=GeneNode(gene,transList,None,None,None)         #creates a node with gene as value
                        geneList.append(newNode)                                #adds node to list
                        addTranscript(transList,transcript,start,end)           #adds transcript to transcript list
        count+=1                                                                #adds one to the count after processing each line of the exon file
        if count%10000==0:                                                       #if processed a thousand more lines
            print "addGenes: "+str(count)+" lines processed."                   #print out a line marker
        line=file.readline().rstrip('\n').replace('"','').replace(';','')       #reads in next line
    #printList(chrList)
    return chrList                                                              #returns the new chromosome list


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
#param chrList  the chromosome list
def getIntrons(chrList) :
    for x in range(1,25):                                                       #cycles through all chromosomes
        print "getIntrons: Running CHR"+str(x)                                  #output tracker
        geneList=chrList[x]                                                     #gets the array of genes in the chromosome
        if geneList[0]!=None:                                                   #if there are genes in the gene list
            for y in range(0,len(geneList)) :                                   #loops through every gene in the list
                transcript=geneList[y].getList().getFirst()                     #gets first transcript in gene's transcript list
                while transcript!=None:                                         #loops through every transcript in list
                    exon=transcript.getList().getFirst()                        #gets first exon in transcript's exon list
                    while exon!=None :                                          #loops through every exon in the list
                        endPrevExon=exon.getEnd()                               #gets the end of the current exon
                        startIntron=endPrevExon+1                               #sets the start of intron to endPrevExon+1
                        if(exon.getNext()!=None) :                              #if there is a next exon
                            startNextExon=exon.getNext().getStart()             #gets the start of the next exon
                            endIntron=startNextExon-1                           #sets the end of intron to startNextExon-1
                            exon.setStart(startIntron)                          #changes the exon to intron: start
                            exon.setEnd(endIntron)                              #changes exon to intron: end
                        else :                                                  #if there is no next exon
                            if exon!=transcript.getList().getFirst() :          #if there is more than one exon in transcript
                                exon=exon.getPrevious()                         #remove the last exon in the list
                                transcript.getList().removeEnd(exon.getNext())
                            else :                                              #if there is only one exon in transcript
                                transcript.getList().removeEnd(exon)            #remove that exon, since no possible introns
                        exon=exon.getNext()                                     #moves to next exon
                    transcript=transcript.getNext()                             #moves to next transcript
                setBoundaries(geneList[y])                              #sets the gene boundaries based on its introns
            geneList.sort(key=lambda gene: (gene.upstream, gene.downstream))    #sorts the gene list by upstream
            while geneList!=[] and geneList[0].getUpstream()==None :            #removes all genes without introns
                del geneList[0]
            for z in range(0,len(geneList)):                                    #sets the index of each gene according to the sorted list
                geneList[z].setIndex(z)
    #printList(chrList)
    return chrList                                                              #returns the new chromosome list


#finds the gene in the gene list that contains the read's start boundary by binary search, list sorted by downstream
#param geneList   the gene list to search
#param start      the read's start boundary
def binarySearchStart(geneList, start):
    low=0                                                   #initial low is the first element
    high=len(geneList)-1                                    #initial high is the last element
    mid=int(round((high+low)/2))                            #gets the rounded middle value of low and high
    while low<=high:                                        #while the middle value is valid
        if geneList[mid].getDownstream()>start and (geneList[mid-1].getDownstream()<start or geneList[mid-1].getDownstream()==start):
            #if the downstream of the gene at index mid is greater than start and the downstream of the gene at mid-1 is less than/equal to start (ie the read boundaries are within mid's boundaries)
            return mid                                      #return the index value
        elif geneList[mid].getDownstream()<=start:          #if mid's downstream is less than/equal to start
            low=mid+1                                       #search the higher half
        else:                                               #if mid's downstream is greater than start
            high=mid-1                                      #search the lower half
        mid=int(round((high+low)/2))                        #recalculate mid
        if mid<=0:                                          #if the first element or below is reached
            mid=0                                           #changes mid to 0
            if geneList[mid].getUpstream()<start and geneList[mid].getDownstream()>start:           #if the read aligns within the first element
                return mid                                  #return 0
            else:
                return None                                 #not found: read boundaries are more upstream than the first element in the list
    return None                                             #not found: read boundaries do not fall within any genes in the gene list


#finds the gene in the gene list that contains the read's end boundary, list sorted by upstream
#param geneList   the gene list to search
#param end        the read's end boundary
def binarySearchEnd(geneList, end):
    low=0                                                   #initial low is the first element
    high=len(geneList)-1                                    #initial high is the last element
    mid=int(round((high+low)/2))                            #gets the rounded middle value of low and high
    while low<=high:                                        #while the middle value is valid
        if geneList[mid].getUpstream()<end and (geneList[mid+1].getUpstream()>end or geneList[mid+1].getUpstream()==end):
            #if the upstream of the gene at index mid is less than end and the upstream of the gene at mid-1 is greater than/equal to end (ie the read boundaries are within mid's boundaries)
            return geneList[mid]                            #returns the gene node at that index
        elif geneList[mid].getUpstream()>=end:              #if mid's upstream is greater than/equal to end
            high=mid-1                                      #search the lower half
        else:                                               #if mid's upstream is less than end
            low=mid+1                                       #search the higher half
        mid=int(round((high+low)/2))                        #recalculate mid
        if mid>=len(geneList)-1 :                           #if the last element or above is reached
            mid=len(geneList)-1                             #changes mid to the last index
            return geneList[mid]                            #returns the last element
    return None                                             #not found: read boundaries do not fall within any genes in the gene list



#searches the gene for all introns the read aligns to, outputs all instances
#param geneNode     the gene to search
#param read         the read ID
#param chr          the chromosome of the gene/read
#param start        the start point of the read
#param end          the end point of the read
#param myFile       the output file to print out intronic reads
def searchTranscript2(geneNode, read, chr, start, end, myFile):
    transcript=geneNode.getList().getFirst()                #gets the first transcript of the gene
    while transcript!=None:                                 #cycles through all transcripts of the gene
        intron=transcript.getList().getFirst()              #gets the first intron of the transcript
        if intron!=None:                                    #if there are introns
            check=transcript.getList().getLast()            #gets the last intron of the transcript
            if (start>intron.getStart() and start<check.getEnd()) or (end>intron.getStart() and end<check.getEnd()) :        #if the read is within transcript boundaries
                while intron!=None :                        #cycles through all introns of the transcript
                    if (start>intron.getStart() and start<intron.getEnd()) or (end>intron.getStart() and end<intron.getEnd()):
                        myFile.write(read+"\t"+chr+"\t"+str(start)+"\t"+str(end)+"\t"+geneNode.getValue()+"\t"+transcript.getValue()+"\t"+str(intron.getStart())+"\t"+str(intron.getEnd())+"\n")                          #prints features
                    intron=intron.getNext()                 #moves to the next intron
        transcript=transcript.getNext()                     #moves to the next transcript


#searches the gene for all introns the read aligns to, outputs only the instances where the read aligns to the same intron in all transcripts of the gene
#param geneNode     the gene to search
#param read         the read ID
#param chr          the chromosome of the gene/read
#param start        the start point of the read
#param end          the end point of the read
#param myFile       the output file to print out intronic reads
def searchTranscript(geneNode, read, chr, start, end, myFile):
    checkStart=start+5                                              #makes sure there is a true alignment
    checkEnd=end-5
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
        distance1=None
        distance2=None
        if checkStart>transCheck[0] and checkStart<transCheck[1]:
            distance1=start-transCheck[0]-1
        if checkEnd>transCheck[0] and checkEnd<transCheck[1]:
            distance2=transCheck[1]+1-end
        distance=None
        if distance1!=None and distance2!=None:
            distance=min(distance1,distance2)
        elif distance1!=None:
            distance=distance1
        else:
            distance=distance2
        myFile.write(read+"\t"+chr+"\t"+str(start)+"\t"+str(end)+"\t"+geneNode.getValue()+"\t"+str(transCheck[0])+"\t"+str(transCheck[1])+"\t"+str(distance)+"\n")         #print features to output file



#checks to see if any reads in the output file contain introns
#param list  the intron list built previously
def parseReads(chrList):
    file=None                                                                                       #opens genome file
    if GENOME_FILE!=None:
        file=open(GENOME_FILE)
    else:
        file=open("/Users/admin/Desktop/Fetal_Heart_405_CAGATC_L007_R2_genome_output.sam")
    count=0
    myFile=None                                                                                     #opens output file
    if PARENT_DIR!=None:
        myFile=open(PARENT_DIR+"/intronicReads.txt","a")
    else:
        myFile=open("/Users/admin/Desktop/intronicReads_Fetal2.txt","a")
    line=None                                                                                       #creates line variable
    for x in range (0,3):                                                                           #skips over documentation lines
        line=file.readline().rstrip("\n")
        x+=1
    while line!="" :                                                                                #reads through the end of the file
        features=line.split("\t")                                                                   #seperates the features of each read
        read=features[0]                                                                            #sets the read name
        chr=features[2]                                                                             #sets the chromosome
        start=int(features[3])                                                                      #sets the start of the read
        end=len(features[9])+start-1                                                                #sets the end of the read
        if chr!="chrM":                                                                             #ignores all mitochondrial DNA
            indexNum=0                                                                              #sets a chromosome number
            if len(chr)==5 :                                                                        #gets two digit chromosome numbers
                indexNum=chr[3:5]
            else:
                indexNum=chr[3:4]                                                                   #gets single digit chromosome numbers
            if indexNum=="X":                                                                       #changes X chromosome number to list compatible 23
                indexNum=23
            elif indexNum=="Y":                                                                     #changes Y chromosome number to list compatible 24
                indexNum=24
            else :
                indexNum=int(indexNum)                                                              #changes indexNum to an integer
            geneList=chrList[indexNum]                                                              #gets the gene list of the chromosome
            geneNode=None                                                                           #creates a geneNode variable
            if geneList!=[] and geneList[0]!=None :                                                 #if there are genes in the chromosome
                geneNode=binarySearchEnd(geneList, end)                                             #finds the gene containing the read boundaries based on upstream sort
                if geneNode!=None:                                                                  #if read is within a gene in the upstream sorted list
                    endIndex=geneNode.getIndex()                                                    #endIndex: the index of the gene in the upstream sorted list
                    startIndex=endIndex                                                             #initially sets startIndex to endIndex
                    geneList2=geneList[0:endIndex+1]                                                #sorts only the the beginning of the list up to endIndex by downstream
                    geneList2.sort(key=lambda gene: (gene.downstream, gene.upstream))
                    reverseIndex=binarySearchStart(geneList2, start)                                #gets the index of the gene in the downstream sorted list that contains the read boundaries
                    if reverseIndex!=None:                                                          #if there is a gene in the downstream sorted list containing the read boundaries
                        startIndex=reverseIndex                                                     #startIndex is now equal to that index
                        for x in range(reverseIndex,endIndex+1):                                    #searches between the start value and the end of the sorted list to find a lower index (upstream) number
                            if geneList2[x].getIndex()<startIndex:
                                startIndex=geneList2[x].getIndex()
                    geneList.sort(key=lambda gene: (gene.upstream, gene.downstream))
                    if startIndex<=endIndex:                                                        #if the indices are valid
                        for x in range(startIndex,endIndex+1):                                      #search all genes between the indices for intron retention
                            searchTranscript(geneList[x], read, chr, start, end, myFile)
        
        count+=1
        if count%10000==0:
            print "parseReads: "+str(count)+" lines processed."
        line=file.readline().rstrip("\n")                           #gets the next read line



def binarySearch(circ, gene, array, line, file3):
    low=0
    high=len(array)-1
    while low<=high:
        mid=int(round((high+low)/2))
        features=array[mid].split("\t")
        #print circ+"\t"+features[0]+"\t"+gene+"\t"+features[4]
        if circ==features[0] and gene==features[4]:
            feat=line.split("\t")
            file3.write(feat[0]+"\t"+feat[1]+"\t"+feat[2]+"\t"+features[2]+"\t"+features[3]+"\t"+features[7]+"\n")
            #file3.write(feat[0]+"\t"+feat[1]+"\t"+feat[2]+"\t"+features[4]+"\n")
            #file3.write(feat[0]+"\t"+feat[1]+"\t"+feat[2]+"\t"+features[2]+"\t"+features[3]+"\t"+features[4]+"\t"+features[5]+"\t"+features[6]+"\t"+features[7]+"\n")
            minus=mid-1
            while minus>0:
                feat2=array[minus].split("\t")
                if circ==feat2[0]:
                    #file3.write(feat[0]+"\t"+feat[1]+"\t"+feat[2]+"\t"+feat2[4]+"\n")
                    file3.write(feat[0]+"\t"+feat[1]+"\t"+feat[2]+"\t"+feat2[2]+"\t"+feat2[3]+"\t"+feat2[7]+"\n")
                    minus=minus-1
                else:
                    minus=0
            plus=mid+1
            while plus<len(array):
                feat3=array[minus].split("\t")
                if circ==feat3[0]:
                    file3.write(feat[0]+"\t"+feat[1]+"\t"+feat[2]+"\t"+feat3[2]+"\t"+feat3[3]+"\t"+feat3[7]+"\n")
                    plus=plus+1
                else:
                    plus=len(array)
            low=1
            high=0
        elif features[0]<circ:
            low=mid+1
        else:
            high=mid-1


def findIntronicCircles():
    array=[]
    file2=None
    if PARENT_DIR!=None:                                            #opens the file listing intronic reads
        file2=open(PARENT_DIR+"/intronicReads.txt")
    else:
        file2=open("/Users/admin/Desktop/processedintronicReads_Fetal2.txt")  #/Users/admin/Desktop/processedIntronicReads.txt
    line2=file2.readline().rstrip("\n")
    while line2!="":
        array.append(line2)
        line2=file2.readline().rstrip("\n")
    file=None
    if CIRCPASSED_FILE!=None:                                           #opens edited output file
        file=open(CIRCPASSED_FILE)
    else:
        file=open("/Users/admin/Desktop/circPassed_Fetal2_nodup.txt")  #/Users/admin/Desktop/circPassed_Fetal.txt
    file3=None
    if PARENT_DIR!=None:                                                #opens a file to store the output
        file3=open(PARENT_DIR+"/intronicCircles","a")
    else:
        file3=open("/Users/admin/Desktop/intronicCircles_Fetal2_nodup.txt","a") #/Users/admin/Desktop/intronicCircles_Fetal.txt
    line=file.readline().rstrip("\n")                                   #reads in a line
    count=0
    while line!="":                                                     #parses through the file
        features=line.split("\t")                                       #splits the columns of the file
        circ=features[0] #.rstrip("1")                                                #stores the read ID
        col1=features[1].split("|")
        gene=col1[1].split(":")
        dupCheck=col1[3]
        if dupCheck!="dup":
            binarySearch(circ, gene[0], array, line, file3)
        line=file.readline().rstrip("\n")                               #moves onto the next line of Linda's output file
        count+=1
        if count%1000==0:
            print "findIntronicCircles: "+str(count)+" lines processed."




import datetime
print datetime.datetime.now()

#parses through gtf file and organizes exons by chr, gene, transcripts (3D linked list)
#chr->gene->transcript->exon
#chrList=addGenes()
#removes exons in the chr list and replaces them with intron boundaries
#chr->gene->transcript->intron
#chrList=getIntrons(chrList)
#parses through genome file, determining which reads overlap the intron boundaries in the chr list
#output (intronic read line): "read ID \t chr \t read start \t read end \t gene \t transcript \t intron start \t intron end" (all possible versions of intronic reads determined)
#cProfile.run('parseReads(chrList)', 'read4.prof')
#parseReads(chrList)
#parses through all circpassed junctions in the output file, matching their aligned reads to the intronic reads file outputted by the previous method
#output: "output line \t intronic read line" (all possible versions of intronic circles determined)
findIntronicCircles()
print "end"

print datetime.datetime.now()




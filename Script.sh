#!/bin/sh

#  Script.sh
#
#
#  Created by JackelynShen on 6/30/14.
#
PARENT_DIR=$1                #full pathway to the directory under which files can be saved (ex. /Users/admin/Desktop)
GTF_FILE=$2                  #full pathway to gtf file with exon boundaries (ex. /Users/admin/Desktop/genes.gtf)
GENOME_FILE=$3              #full pathway to bowtie2 read alignments to genome index from circularRNApipeline (ex: /Users/admin/Desktop/sampleOutput_Linda/PLoS_One_2012data_cutAdapt/orig/genome/lane1_2_genome_output.sam)
CIRC_OUTPUT_FILE=$4       #full pathway to circularRNApipeline output determining circular RNAs (ex. /Users/admin/Desktop/sampleOutput_Linda/PLoS_One_2012data_cutAdapt/circReadsNeg10/ids/lane1_1__output.txt)
REPORT_FILE=$5                  #full pathway to circularRNApipeline report file containing all aligned junctions (ex. /Users/admin/Desktop/sampleOutput_Linda/PLoS_One_2012data_cutAdapt/circReadsNeg10/reports/lane1_1_report.txt)


#edits the GTF file to include only exons
awk 'BEGIN{OFS="\t";} $3=="exon" {print $1,$4,$5,$10,$14}' $GTF_FILE > $PARENT_DIR/EXONS_FILE.txt

#edits the output.txt file to include only circPassed reads
grep 'circPassed' $CIRC_OUTPUT_FILE > $PARENT_DIR/circPassed.txt

#no parameters: tester files automatically inputted
#1st parameter: exon file from the gtf file
#2nd parameter: bowtie2 genomic alignments (Rd2)
#3rd parameter: all circPassed from the output.txt file
#4th parameter: the parent directory
#creates intronicCircles.txt - all possible versions of intronic circles
python /Users/admin/Desktop/IntronRetention/python.py $PARENT_DIR $PARENT_DIR/EXONS_FILE.txt $GENOME_FILE $PARENT_DIR/circPassed.txt

sort -u -k2,2 /Users/admin/Desktop/intronicCircles.txt > /Users/admin/Desktop/intronicCircles2.txt

#removes duplicates from intronic reads file for adding column
sort -u -k1,1 $PARENT_DIR/intronicReads2.txt > $PARENT_DIR/sortedIntronicReads.txt


#adds a column to Linda's report file indicating the number of intron retention events for each junction (creates a new file)
#takes each junction in the report file, matches it with the reads listed in the output file, and takes that list of aligned reads and counts the number of matches to the sorted intronic reads file from the python file
#only executed after read duplicates are removed from the intronic reads file outputted by the python file
addColumn2()
{
    PARENT_DIR=$1                                                               #full pathway to the directory under which files can be saved (ex. /Users/admin/Desktop)
    CIRC_OUTPUT_FILE=$2                                                         #full pathway to circularRNApipeline output determining circular RNAs
    REPORT_FILE=$3                                                              #full pathway to circularRNApipeline report file containing all aligned junctions
    count=0                                                                     #initializes a count variable to parse through the report file
    awk '{print $0}' $REPORT_FILE |
    while read line                                                             #reads the report file line by line
    do
    count=`expr $count + 1`                                                     #adds one to the count
    tmp=`echo $line | awk '{print $1}'`                                         #sets tmp variable as the junction ID
    printf "$line\t"                                                            #prints the line and a tab to account for another column
    if [ $count == 1 ];then                                                     #skips over the Global alignment score cutoff
        echo " "
    elif [ $count == 2 ]; then                                                  #adds the label "#intronRetention" to the new column
        echo "#intronRetention"
    else                                                                        #subsequent lines contain relevant junction information
        grep "$tmp" $CIRC_OUTPUT_FILE |
        awk '{print $1}' | awk '{print substr($0, 0, length($0)-1)}' > $PARENT_DIR/readtemp.txt          #gets read IDs that aligned to the junction and saves them into a file
        WCCOUNT=0                                                                     #initializes a variable to store the number of intron retention events for the junction
        STRING_COUNT=0                                                                #initializes another count variable to create the string variable to enter into egrep
        awk '{print $0}' $PARENT_DIR/readtemp.txt | {
        while read line2                                                              #parses through all the read IDs
        do
        if [ $STRING_COUNT == 0 ]; then                                               #if the read ID is the first read ID in the list
            string=$string$line2                                                      #sets the variable string to read ID
            STRING_COUNT=`expr $STRING_COUNT + 1`                                     #increases STRING_COUNT by one
        elif [ $STRING_COUNT == 500 ]; then                                           #limits the number of patterns entered into egrep to avoid argument list too long
            string=$string'|'$line2                                                   #appends a the read ID to the existing string and adds a vertical bar (egrep optimization)
            wc=$(egrep $string $PARENT_DIR/sortedIntronicReads.txt | wc -l)          #greps and counts the number of intronic reads from the reads listed in the string (max 500)
            WCCOUNT=`expr $WCCOUNT + $wc`                                             #adds wc to the intron retention count
            STRING_COUNT=0                                                            #resets the string count to 0
            string=""                                                                 #empties the string
        else                                                                          #if the read number is under 500
            string=$string'|'$line2                                                   #appends the current read ID to the existing string and adds a vertical bar (egrep optimization)
            STRING_COUNT=`expr $STRING_COUNT + 1`                                     #increases STRING_COUNT by one
        fi
        done
        if [ $string ]; then                                                          #if the string is not empty
            wc=$(egrep $string $PARENT_DIR/sortedIntronicReads.txt | wc -l)          #greps and counts the number read IDs appearing in the edited intronic reads file
            WCCOUNT=`expr $WCCOUNT + $wc`                                             #adds wc to the intron retention count
        fi
        echo $WCCOUNT; }                                                              #prints out the intron retention count
        rm $PARENT_DIR/readtemp.txt                                                   #removes the temporary read file
    fi
    done
}

#1st parameter: parent directory
#2nd parameter: circ output file
#3rd parameter: report file
addColumn2 $PARENT_DIR $CIRC_OUTPUT_FILE $REPORT_FILE



# program that reads a file and takes
# Author: Andrew Beatty

import csv

FILENAME= "students.csv"
DATADIR= "../../data/"
FULLPATH= DATADIR + FILENAME

#print(FULLPATH)

with open (FULLPATH, "rt") as fp:
    #for line in fp:
    #    print(line, end="")
    reader = csv.reader(fp, delimiter = ",")
    total = 0
    linenumber = 0
    for line in reader: # is not the header (line 0)
        if linenumber:
           #print(line)
           total += int(line[1].strip().strip('"')) # the ages have quotes so are read in as strings until we strip
        else: #is the header row
            print(line)
        linenumber += 1
    print(f"The total age is {total}")
        
    
     
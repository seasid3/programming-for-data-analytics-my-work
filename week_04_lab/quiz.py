# This is the quiz file for week 4 lab.
# Author: Andrew Beatty

import re

regex = "\[" 
filename = "./quiz.txt"

with open(filename) as quizFile:
    for line in quizFile:
        searchResult = re.search(regex, line)
        if (searchResult):
            matchingLine = line
            # I set the end to blank because each line will already have a \n
            print (matchingLine, end="")
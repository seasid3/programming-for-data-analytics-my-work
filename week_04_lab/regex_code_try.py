# This is code to try using regex. from the lab
# Author: Andrew Beatty

import re

'''
#to find date and times, andrew's examples.
regex = "\[.*\]"
filename = "smallerAccess.log.txt"

with open(filename, 'r') as input_file:
    for line in input_file:
        found_text_list = re.findall(regex, line)
        if (len (found_text_list) != 0):
            # print (found_text_list)
            found_text = found_text_list[0]
            print (found_text)
            # if I did not want the [] at the beginning and end
            print(found_text[1:-1])
            '''
'''  
#to find \text. my attempt
regex = "\/\w*+\."
filename = "smallerAccess.log.txt"

with open(filename, 'r') as input_file:
    for line in input_file:
        found_text_list = re.findall(regex, line)
        if (len (found_text_list) != 0):
            # print (found_text_list)
            found_text = found_text_list[0]
            print (found_text)
        '''
'''
regex = "\d{1,3}\.\d{1,3}"
filename = "smallerAccess.log.txt"

with open(filename, 'r') as input_file:
    for line in input_file:
        found_text_list = re.findall(regex, line)
        if (len (found_text_list) != 0):
            # print (found_text_list)
            found_text = found_text_list[0]
            print (found_text)
            # if I did not want the [] at the beginning and end
            print(found_text[1:-1])
            '''

# To anonymise the sub domains of IP addresses
regex = "(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}" # search for IP address but create a group for the first two triplets
# to keep this group
replacement_text = "\\1XXX.XXX " #note the space at the end to match above
filename = "smallerAccess.log.txt"
output_filename = "anonymisedIPs.txt"

with open(filename) as input_file:
    with open(output_filename, 'w') as output_file:
        for line in input_file:
            #for debugging
            # found text = re.search(regex, line).group()
            # print (found_text)
            new_line = re.sub (regex, replacement_text, line)
            output_file.write (new_line)
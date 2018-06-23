#credit to /The-ivyleague-sloth for development of this script
#-------------------------

from sys import argv
from itertools import islice
import time

#open all of our files we are going to create
#rename to something more fitting later
location_file = open("location.h","w+")
main_file = open("dictionary2.h","w+")
new_file = open("dictionary.h", "w+")

#write a short description in the file of what the file is for followed by a newline for clarity
location_file.write("/*this file shows the word and the start and end address from the dictionary array in dictionary.h*/") # writes them out like able[ah,bu,le]
location_file.write("\r\n") # new line character for organization
main_file.write("/*this file a giant look up table for how to pronounce certain words from PhraseALater.dic file*/") # writes them out like able[ah,bu,le]
main_file.write("\r\n") # new line character for organization

#if not defines for header files to avoid redundancy
main_file.write ("#ifndef DICTIONARY2_H__ \n#define DICTIONARY2_H__ \n\n" )
location_file.write ("#ifndef LOCATION_H__ \n#define LOCATION_H__ \n\n")

#any includes that need to be un our files
main_file.write('#include "speak.h"\n\n')

#write the beginning of the main look up table rest is from dictionary file
main_file.write ("char dic[8350] = {")

#any initial variables that need to be declared
start = 0
end = 0
temp_list = []
#tell the user files are being created
print "creating files"
time.sleep(.1)

#parse through dictinonary file
with open("PhraseALator.dic", 'r') as f:
    for line in islice(f, 0, None,):
        nupart = line.replace("\\", " ").replace ("=", " ").replace("'t","t").replace("o'","o").replace("'s","s").replace("'r","r").replace("-","") #reoplace any apostrophes or characters that cause issues
        words = [i for i in nupart.split()] #creates a list with all of our pronuniations and the word
        first = "uint32_t " + words[0] + "[2] = {" #creates our location array output = uint32_t word[2]{locatin of word in giant array}
        begin = words[0] + "[example] = {" #can be erased
        del words[0] # delete our word from our array so we only have abbreviations

        # if else statement here because of index zero
        if line[0] == 'a' and line[1] == ' ' : #if statement just for finding the first line... this is is file specific
            #find the length and calculate the start adn end range
            length = len(words)
            start = (end)
            end = start + (length) -1

        else:
            # go here if not at first word.. calculate start and end ranges
            length = len(words)
            start = (end) + 1
            end = start + (length) -1

        #put our start and end address in temporary list for reference
        temp_list.append(start)
        temp_list.append(end)
        #join our elements so we ouput what we want
        values = ','.join(str(t) for t in temp_list) + "};"
        array = ",".join(words) + "," + "\\"
        fin = ",".join(words) + "]"
        new_line = first + fin
        new_line2 = first + values

        location_file.write(new_line2) # writes them out like able[ah,bu,le]
        location_file.write("\n") # new line character for organization
        #for dictionary2.h
        main_file.write(array) #writes a giant array
        main_file.write("\n\t\t\t\t") # new line character for organization
        #for dictionary.h
        new_file.write(new_line) # writes them out like able[ah,bu,le]
        new_file.write("\n") # new line character for organization
        #delete start and end elements in list for new regions
        temp_list.pop()
        temp_list.pop()
        #print temp_list

#close our main array
main_file.write("};")
#write our #endifs to header files
main_file.write ("\n#endif\n" )
location_file.write ("\n#endif\n")
#close files and alert user we are done
time.sleep(.1)
main_file.close()
time.sleep(.1)
new_file.close()
time.sleep(.1)
location_file.close()
print "all files closed"

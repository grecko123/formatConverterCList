from sys import argv
from itertools import islice
#from itertools import product

script,filename = argv

with open(filename, 'r') as f:
    # iterate over every 3rd line, starting with the 2nd
    # this is the format of the file as provided(fixed)
    for line in islice(f, 0, None,):
		nupart = line.replace("\\", " ").replace ("=", " ")
		print nupart
		words = [i for i in nupart.split()]
		first = "#define " + words[0] + " (" 
		print first
		del words[0]
		print words
		fin = " + ".join(words) + ")"
		print first + fin

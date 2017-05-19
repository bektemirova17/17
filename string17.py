#creation
word = "Hello World"
>>> print word
Hello World
#
word = "Hello World"
letter=word[0]
>>> print letter
H
#length
word = "Hello World"
>>> len(word)
11
#finding
word = "Hello World"
>>> print word.count('l')	# count how many times l is in the string
3
>>> print word.find("H")  	# find the word H in the string
0
>>> print word.index("World") 	# find the letters World in the string
6
#count
s =  "Count, the number     of spaces"
>>> print s.count(' ')
8
#set of letter
print word[0]          #get one char of the word
print word[0:1]        #get one char of the word (same as above)
print word[0:3]        #get the first three char
print word[:3]         #get the first three char
print word[-3:]        #get the last three char
print word[3:]         #get all but the three first char
print word[:-3]        #get all but the three last character
word = "Hello World"
word[start:end]    	# items start through end-1
word[start:]            # items start through the rest of the list
word[:end]              # items from the beginning through end-1
word[:]                 # a copy of the whole list

#split
word = "Hello World"
>>> word.split(' ')  # Split on whitespace
['Hello', 'World']
#truefalse
word = "hello world"
>>> word.startswith("H")
True
>>> word.endswith("d")
True
>>> word.endswith("w")
False
#repeat
print "."* 10	# prints ten dots
>>> print "." * 10
..........
#replace
word = "Hello World"
>>> word.replace("Hello", "Goodbye")
'Goodbye World'
#upper-lower
string = "Hello World"
>>> print string.upper()
HELLO WORLD
>>> print string.lower()
hello world
>>> print string.title()
Hello World
>>> print string.capitalize()
Hello world
>>> print string.swapcase()
hELLO wORLD
#reversing
string = "Hello World"
>>> print ' '.join(reversed(string))
d l r o W   o l l e H
#strip
strip()     #removes from both ends
lstrip()    #removes leading characters (Left-strip)
rstrip()    #removes trailing characters (Right-strip)
>>> word = "    xyz    "
>>> print word
    xyz    
>>> print word.strip()
xyz
>>> print word.lstrip()
xyz    
>>> print word.rstrip()
    xyz
#+++
"Hello " + "World" # = "Hello World"
"Hello " + "World" + "!"# = "Hello World!"
#join
>>> print ":".join(word)  # #add a : between every char
H:e:l:l:o: :W:o:r:l:d
>>> print " ".join(word)  # add a whitespace between every char
H e l l o   W o r l d
#testing
word = "Hello World"
word.isalnum()         #check if all char are alphanumeric 
word.isalpha()         #check if all char in the string are alphabetic
word.isdigit()         #test if string contains digits
word.istitle()         #test if string contains title words
word.isupper()         #test if string contains upper case
word.islower()         #test if string contains lower case
word.isspace()         #test if string contains spaces
word.endswith('d')     #test if string endswith a d
word.startswith('H')   #test if string startswith H
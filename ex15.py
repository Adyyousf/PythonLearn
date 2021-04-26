# importing module
from sys import argv

# getting the arguments before running the script
script, filename = argv

# open the file inside the the variable 'txt'
txt = open(filename)

print "Here's your file %r:" % filename

# read the content inside 'txt' and print it
print txt.read()

print "Type the filename again:"

# get the file name from the user and store it inside 'file_again'
file_again = raw_input("> ")

# open the file_again inside txt_again
txt_again = open(file_again)

# read the content inside text_again and print it
print txt_again.read()

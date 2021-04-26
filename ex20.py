from sys import argv #importing module
 
script, input_file = argv # taking argument file

def print_all(f):      # Defining a function to print the whole file
    print f.read()
    
def rewind(f):         # defining a function to take the cursor back to 
    f.seek(0)          # the first line

def print_a_line(line_count, f):  # function to print a single line
    print line_count, f.readline()
    
current_file = open(input_file)    # opening the input file

print "first let's print the whole file:\n"

print_all(current_file)    # call function to print whole file

print "Now let's rewind, kind of like a tape."

rewind(current_file)      # call function rewind, passing current file
                          # as argument
print "Let's print three lines."

current_line = 1       
print_a_line(current_line, current_file) # calling function to print a line

current_line += 1          # incrementing
print_a_line(current_line, current_file) # calling print_a_line again

current_line += 1          
print_a_line(current_line, current_file)  

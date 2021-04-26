from sys import argv
from os.path import exists

script, from_file, to_file = argv
#from_file = raw_input("Enter file name to copy from \t")
#to_file = raw_input("Enter file name to copy to \t")
print "Copying from %s to %s" %(from_file, to_file)

#```````````````??``````~~~~
in_file = open(from_file).read()

print "The input file is %d bytes long" % len(in_file)

print "Does the output file exits? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

out_file = open(to_file, 'w').write(in_file)
#out_file.write(in_file)

print "Alright, all done."

#out_file.close()
#in_file.close()

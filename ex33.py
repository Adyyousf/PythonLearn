def looping(N, X) :
	numbers = []
	i = 0

	while i < N :
		print "At the top i is %d" %i
		numbers.append(i)
		
		i = i + X = y
		print "\nNumbers now :\t", numbers
		print "\nAt the bottom i is %d" % i


	print "The numbers: "

	for num in numbers :
		print "\t%d" % num

num = int(raw_input("Number of operations:> "))
incrementor = int(raw_input("Increment by:> "))

looping(num, incrementor)
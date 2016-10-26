program_loop = True
while program_loop:
	box = raw_input("what number? ")
	if box == "exit":
		program_loop = False
	else:
		try:
			box = int(box)
			for x in range(13):
				print box * x
		except Exception as e:
			print "Thats not a Number!"
f = open( "InputDay1.txt", "r" )
total = 0
numcount = 2052 #found by printing
firstnum = f.read( 1 )
lastnum = firstnum

while True:
	num = f.read( 1 )
	if not num: 
		if firstnum == lastnum:
			total = total + int(lastnum)
			print ( total )
			break
		else:
			print ( total )
			break
	else:
		if lastnum == num:
			total = total + int(num)
			lastnum = num
		else:
			lastnum = num

f.close()
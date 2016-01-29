import os
filename = open("output.txt")            
outputfile = open("final.txt","w+")

trips = []

for line in filename:

	if line.startswith("trip"):
		continue
	
        trip = line.split(',')
        trips.append(trip)
pos = 0
tripread = 0
tripfile = 0
filename = open("output.txt")
flag = None

for line in filename:
        trip = line.split(',')

	if line.startswith("trip"):
		continue

	tripread = int(trip[4])
	tripprev = tripread - 1

	tripfile = int(trips[pos-1][4])
	print "this",tripread,"prev",tripfile,line
	if tripread == tripfile + 2:
		print "^^this replaced with vv"
		line = line.replace(","+trip[4]+",",","+str(tripprev)+",")
		print line
		print "this seq",trip[4],"prev seq",trips[pos-1][4]
		flag = 1
		outputfile.write(line)
		pos += 1
		continue

	if flag:

		if tripread == tripfile+1:
			print line
			line = line.replace(","+trip[4]+",",","+str(tripfile)+",")
			print "replaced with",line
		else:
			flag = None

	outputfile.write(line)
	pos += 1
filename.close()
os.remove('output.txt')

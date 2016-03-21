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
		outputfile.write(line)
		continue

	tripread = int(trip[4])
	tripprev = tripread - 1

	tripfile = int(trips[pos-1][4])
	if tripread == tripfile + 2:
		line = line.replace(","+trip[4]+",",","+str(tripprev)+",")
		flag = 1
		outputfile.write(line)
		pos += 1
		continue

	if flag:

		if tripread == tripfile+1:
			line = line.replace(","+trip[4]+",",","+str(tripfile)+",")
		else:
			flag = None

	outputfile.write(line)
	pos += 1
filename.close()
os.remove('output.txt')
print "gtfs final.txt created"

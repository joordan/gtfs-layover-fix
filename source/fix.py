filename = raw_input("Enter file name (stop_times.txt): ")
if len(filename) < 1 : filename ="stop_times.txt"

inputfile = open(filename)                    
outputfile = open("output.txt","w+")            

trips = []

for line in inputfile:

        if line.startswith("trip"):
                continue

	trip = line.split(',')

        trips.append(trip)

inputfile = open(filename)                
pos=0
for line in inputfile:
        if line.startswith("trip"):
        	outputfile.write(line)
        	continue


	trip = line.split(',')
	id = trip[3]
	dep = trip[2]
	arr = trip[1]
	seq = int(trip[4])

	try:
		if id == trips[pos+1][3] and seq+1 == int(trips[pos+1][4]):
			line = line.replace(dep,trips[pos+1][2])
			line = line.replace(trips[pos+1][2],arr,1)

		pos += 1
	
		if id == trips[pos-2][3] and trip[0] == trips[pos-2][0]:
			continue	
	except:
		pass

	outputfile.write(line)        
print "gtfs output.txt created"

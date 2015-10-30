filename = raw_input("Enter file name (gtfs.txt): ")
if len(filename) < 1 : filename ="input.txt"

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
                continue


	trip = line.split(',')
	id = trip[3]
	dep = trip[2]
	arr = trip[1]
	seq = int(trip[4])

	if id == trips[pos+1][3] and seq+1 == int(trips[pos+1][4]):
		print "\tTIME CHANGED",id
		line = line.replace(dep,trips[pos+1][2])
		line = line.replace(trips[pos+1][2],arr,1)
		
	pos += 1
	
	print "\tseq:",seq,"\ttripseq",trips[pos][4]

	print trip[0],trips[pos][0]
	if id == trips[pos-2][3] and trip[0] == trips[pos-2][0]:
		print id,"\tthis REMOVED"," trip id:",trips[pos-2][3]
		continue	

	outputfile.write(line)	


	if pos == len(trips) - 2:
		break

filename = open("output.txt")          


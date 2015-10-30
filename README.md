# gtfs-layover-fix
Script to fix layover problem in gtfs

2 scripts 
the 1st script fixlayover.py takes the gtfs file and creates an output.txt file with the layovers corrected
the 2nd script cascade.py takes the output.txt file and cascades the stop sequences and creates a final.txt file
the 2nd is optional but I actually needed to cascade the sequences becuase of my realtime implementation

Heres a big warning though, you need to add the headers again and the very last line of the original gtfs

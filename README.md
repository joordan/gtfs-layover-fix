# gtfs-stop_times_layover-fix
Script to fix layover problem in gtfs in certain feed exports

2 scripts  
the 1st script fix.py takes the gtfs stop_times.txt file and creates an output.txt file with the layovers corrected  
the 2nd script cascade.py takes the output.txt file and cascades the stop sequences and creates a final.txt file  
the 2nd is optional but I actually needed to cascade the sequences becuase of my realtime implementation

Heres a big warning though, you need to add the headers again and copy the last few lines of the original gtfs

Note: stop_headsign,pickup_type,drop_off_type are not specified, tested on SJRTD gtfs not sure if it will work on other agencies

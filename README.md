# gtfs-stop_times_layover-fix
Script to fix layover problem in gtfs in certain feed exports

2 scripts  
the 1st script fix.py takes the gtfs stop_times.txt file and creates an output.txt file with the layovers corrected  
the 2nd script cascade.py is optional, it takes the output.txt file and cascades the stop sequences and creates a final.txt file  
Tested on SJRTD gtfs not sure if it will work on other agencies

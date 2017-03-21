# chipmunk
any .sh file may at some point be replaced with a .py file  
The goal is to create a python (or something similar) script that automates these steps, and records details about backed up items so the user can keep track of what's where and all that.  

intended order of script execution:   
+ init.sh - init config files & indexing database files.   
+ prep_directory.sh - create entry in index.json, create tarball of directory  
+ process_tarball.sh - split tarball into 2950 byte chunks, turn each chunk in to a QR code, [encode in to video file]  
+ upload.sh - upload to chosen site + record urls in database  

+ download.sh - download from site  
+ restore.sh - extract QR codes from video, scan into chinks, cat chunks together, untar back to origional directory  

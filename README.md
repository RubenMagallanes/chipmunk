# chipmunk  

This project is intended as more of a proof of concept than anything else.  
The end goal is a series of scripts that together, backup a local directory to a media hosting website.  
This is acomplished by splitting a tarball into pieces, encoding these piece to QR codes, then uploading these codes to a media hosting website, either individually or in a video container (such as mp4). Challenges include finding a hosting site whos compression doesn't ruin the QR codes, and keeping track of the urls.  

any .sh file may at some point be replaced with a .py file  
The goal is to create a python (or something similar) script that automates these steps, and records details about backed up items so the user can keep track of what's where and all that.  

intended order of script execution:   
+ init.sh - init config files & indexing database files.   
+ prep_directory.sh - create entry in index.json, create tarball of directory  
+ process_tarball.sh - split tarball into 2950 byte chunks, turn each chunk in to a QR code, [encode in to video file]  
+ upload.sh - upload to chosen site + record urls in database  
usage : python upload_video.py --file="/tmp/test_video_file.flv"
                       --title="Summer vacation in California"
                       --description="Had fun surfing in Santa Cruz"
                       --keywords="surfing,Santa Cruz"
                       --category="22"
                       --privacyStatus="private"

+ download.sh - download from site  
+ restore.sh - extract QR codes from video, scan into chinks, cat chunks together, untar back to origional directory  

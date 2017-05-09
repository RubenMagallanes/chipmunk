#!/bin/bash
#else, upload to youtube, save hash,url in index.csv

#check if client secrets file exists in ~/.chipmunk/cient_secrets
#call upload_video.py passing in required args. read args from file? 
#redirecto script output to file ${HASH}.url so can be read by download .sh

DBPATH=~/.chipmunk/
HASH=$(<${DBPATH}.current_hash)
FILEPATH=${DBPATH}${HASH}.video.mp4

#check if client secrets file exists
if [ ! -e "${DBPATH}client_secrets.json" ] 
then 
	echo "client secrets file doesn't exist, run init.sh first"
	exit -1 # indicates failure
fi

# construct array of args
opt=(--file="${FILEPATH}")
opt+=(--title="${HASH}")
opt+=(--description="chipmunk autoupload")
opt+=(--keywords="chipmunk")
opt+=(--category="28")	# science and tech category
opt+=(--privacyStatus="private")


#call upload_video.py
#TODO call python2 or python3 in script's source shebang depending
python upload_video.py "${opt[@]}"


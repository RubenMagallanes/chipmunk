#!/bin/bash

#check if directory ~/chipmunk exists, create if not
echo "chipmunk init script called"

DIRECTORY=~/.chipmunk/		#cant have spaces in dir name as that would need quotes, but quotes prevent expansion of '~' so :)
if [ ! -d "$DIRECTORY" ] 
then
	mkdir "$DIRECTORY"
	echo "${DIRECTORY} directory created"
fi

#check if ~/chipmunk/index.json exists, create if not

if [ ! -a "${DIRECTORY}index.json" ]
then
	touch "${DIRECTORY}index.json"
	> "${DIRECTORY}index.json"	
	echo "{\"entries\":[]}" > "${DIRECTORY}index.json"
	echo "${DIRECTORY}index.json created"
fi

#check if ~/chipmunk/prefs file exists, create if not & populate with text (like username and psswd for upload site, api key if necc'y)




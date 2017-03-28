#!/bin/bash
echo "chipmunk init script called"

#check if directory ~/.chipmunk exists, create if not
#cant have spaces in dir name as that would need quotes, but quotes prevent expansion of '~' so :)
DIRECTORY=~/.chipmunk/	

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

if [ ! "${DIRECTORY}prefs" ]
then
	touch "${DIRECTORY}prefs"
	>"${DIRECTORY}prefs"
	
fi

#ensure ~/.chipmunk/.current_hash exists, then clear it

if [ ! "${DIRECTORY}.current_hash" ]
then
	touch "${DIRECTORY}.current_hash"
fi

>"${DIRECTORY}.current_hash"


#ensure ~/.chipmunk/.current_dir exists, then clear it

if [ ! "${DIRECTORY}.current_dir" ] 
then
	touch "${DIRECTORY}.current_dir"
fi

>"${DIRECTORY}.current_dir"


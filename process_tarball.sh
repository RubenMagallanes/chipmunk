#ASSUMES:				#these should be from previous script
#	~/.chipmunk/.current_dir*	contains path to .archive.tar.gz, path ends in /
#	~/.chipmunk/.current_hash*	contains hash of .archive.tar.gz


DBPATH=~/.chipmunk/			#chipmunk directory 
WORKINGDIR=$(<${DBPATH}.current_dir)	#read working directory from file
HASH=$(<${DBPATH}.current_hash)		#read hash from file


#mkdir  $HASH_temp to save part files and qr codes in to 

TEMP_DIR=${WORKINGDIR}${HASH}_temp/
echo "directory tarball will be split into:"
echo $TEMP_DIR

if [ ! -d "$TEMP_DIR" ] 
then
	mkdir "$TEMP_DIR"
	echo "$TEMP_DIR created"
else
	#dont delete it for the user in case it contains important stuff
	echo "somehow theres already a directory what that name"
	echo "check it yourself, and delete it, then re run this script"
fi


#split tarball with name .archive.tar.gz into part files, save in $DIR/part


#split -b 2953 in $HASH.part_ 

#turn each file into qr code, save in $DIR/qr
#qrencode 
#	-o filename
#	-l L [error correction minimal
#	-v 40 [protocol version 40 
#	-S [structured (idk if we want this)
#	-8 [8 bit mode (also idk if we want this either)

#depending on uploading to imgur or youtube or whatever, stop here or 
#encode qr codes into video

#cleanup temp directory?


#ASSUMES:				#these should be from previous script
#	~/.chipmunk/.current_dir*	contains path to .archive.tar.gz, path ends in /
#	~/.chipmunk/.current_hash*	contains hash of .archive.tar.gz
#	W0RKINGDIR/.archive.tar.gz


DBPATH=~/.chipmunk/			#chipmunk directory 
WORKINGDIR=$(<${DBPATH}.current_dir)	#read working directory from file
HASH=$(<${DBPATH}.current_hash)		#read hash from file


#mkdir  $HASH_temp to save part files and in to 

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

#create directory for qr codes 

QR_DIR=${WORKINGDIR}${HASH}_qr/
echo "directory qr codes will be saved into:"
echo $QR_DIR

if [ ! -d "$QR_DIR" ]
then
	mkdir "$QR_DIR"
	echo "$QR_DIR created"
else
	echo "somehow directory already exists, delete it then rerun script"
fi

#split tarball with name .archive.tar.gz into part files, save in $TEMP_DIR/part
#level 40 QR code with low error correction can contain about 2953 bytes or so. Lets split into 2952 or 2920 for a nice round number
split -b 2952 ${WORKINGDIR}.archive.tar.gz ${TEMP_DIR}${HASH}.part_ 

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


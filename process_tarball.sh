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
	exit
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
	exit
fi

#split tarball with name .archive.tar.gz into part files, save in $TEMP_DIR/part
#level 40 QR code with low error correction can contain about 2953 bytes or so. Lets split into 2952 or 2920 for a nice round number
split -b 2952 ${WORKINGDIR}.archive.tar.gz ${TEMP_DIR}${HASH}.part_ 

#turn each file into qr code, save in $QR_DIR
for file in ${TEMP_DIR}*
do
	TEXT=$(<$file)
	echo "encoding ${file} into QR code"
	qrencode -l L -v 40 -o ${QR_DIR}${file}.qr $TEXT
done
#	-8 [8 bit mode -test whether we want this?

#encode qr codes into video, 60 frames using bash style * glob
#save video in .chipmunk directory
ffmpeg -framerate 60 -pattern_type glob -i '${QR_DIR}*.qr' ${DBPATH}${HASH}.video.mp4

#cleanup temp directory
rm -rf $TEMP_DIR
echo "${TEMP_DIR} removed"


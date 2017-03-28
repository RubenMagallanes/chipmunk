#ASSUMES:				#these should be from previous script
#	~/.chipmunk/.current_dir	contains path to .archive.tar.gz
#	~/.chipmunk/.current_hash	contains hash of .archive.tar.gz


DBPATH=~/.chipmunk/			#chipmunk directory 
WORKINGDIR=$(<${DBPATH}.current_dir)	#read working directory from file
HASH=$(<${DBPATH}.current_hash)		#read hash from file


#mkdir name $HASH_temp to save part files and qr codes in to 
if

#split tarball with name $HASH into part files, save in $DIR/part
#split -b 2953 $HASH_0000.part 

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


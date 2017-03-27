#!/usr/bin/env python2.7
import json
from pprint import pprint
from subprocess import call
from sys import exit

#global variables yay

directory_path = "./test/backmeup"	# eventually take this from args
db_path = "./test/chipmunk/"		#location of db, ref from config

#these are all placeholders, will overwrite in seperate_path
path = "directory path"
directory_name = "dir name"
output_filepath = "archive output filepath"

#hash tarball
hash_path = "hashoath"

#read hash
	dir_hash = "hash read from file"
	new_entry = "json object for archive"

""" 
	STEPS:
	1. seperate part to directory and directory name
	2. archive & compress dir, save as archive.tar.gz to same path
	3. hash tarball, save to file in same directory as db
	4. read hash into variable, save that and directory name to new_entry
	5. append this to the db 'entries' list
	6. create $hash .tags file, also create .tree file with tree output
"""

def seperate_path():
	"""
	1. seperate directory to backup name and path

	path 		#directory path, string
	directory_name	#directory name, string
	output_filepath	#path archive will be output to 
	"""
	#seperate directory name from rest of path
	directories_list = directory_path.split("/")
	last_item_index = len(directories_list) -1

	#get name of directory
	directory_name = directories_list[last_item_index]

	#remove last item, left with just the path 
	del directories_list[-1]

	#restore back to string
	path = ""
	for dir in directories_list :
		path = path + dir + '/' 

	output_filepath = path + '.archive.tar.gz'

	

def archive_dir():
	"""
	2. archive & compress dir, save as archive.tar.gz to same path

	"""
	print("archiving and compressing directory")

	#execute tar command
	tar_command = ['tar', '-zcvf',  output_filepath, directory_path]
	
	if call(tar_command) != 0 :
		print("tar returned nonzero exit code, something screwed up")
		print("assume archive is corrupted, ")
		print("rerun this step before moving on to next step")
		exit()
	
	
	print("tarball created successfuly")
	print("tarball path: " + output_filepath  )

	
def hash_tarball():
	"""
	3. hash tarball, save to file in same directory as db

	"""
	print("hashing tarball")
	
	#create hash path
	hash_path = path + 'hash.txt'
	
	#save md5 hash of archive to file
	hash_command = ['md5sum', output_filepath, '>', hash_path]

	if call(hash_command) != 0 :
		print("tar returned nonzero exit code, something screwed up")
		print("assume archive is corrupted, ")
		print("rerun this step before moving on to next step")
		exit()
	print("md5 hash created successfully")


def read_hash():
	"""
	4. read hash into variable, save that and directory name to new_entry

	"""
	
	#read hash from file, clearing the \n
	with open(hash_path) as hashfile:
		dir_hash = hashfile.read().replace('\n', '')
	

	#create new database entry
	new_entry = {'name':directory_name, 'hash': dir_hash}

def add_to_db():
	"""
	5. append this to the db 'entries' list

	"""
	
	# load db into $data variable
	with open(db_path + 'index.json') as data_file:
		data = json.load(data_file)

	#add new entry to database
	data["entries"].append(new_entry)

	#save back to file
	with open(db_path + 'index.json', 'w') as data_file_w : 
		json.dump(data, data_file_w)

	print("new entry added to database successfully")


def create_tags_file():
	"""
	6. create $hash .tags file, also create .tree file with tree output

	"""
	#TODO  do some kind of interactive where user enters one by one and we add to csv with each \n
	#while loop
	tags_command = ['echo', '"tags"', '>', db_path + dir_hash + '.tags.csv'] 
	if call(tags_command) != 0 :
		print("creating tags file failed for some reason")
		print("rerun this script ")
		exit()
	
	#save output of tree command to file
	tree_command = ['tree', 'directory_path', '>', db_path + dir_hash +'.tree']
	if call(tree_command) != 0 :
		print("tree command returned error")

	


#actually execute these. 
seperate_path()
archive_dir()
hash_tarball()
read_hash()
add_to_db()
create_tags_file()

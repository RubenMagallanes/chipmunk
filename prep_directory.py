#!/usr/bin/env python2.7
import json
from pprint import pprint
from subprocess import call
from sys import exit

directory_path = "./test/backmeup"	# eventually take this from args
db_path = "./index.json"		#location of db, ref from config
hash_path = "./test/hash.txt"		#we're gonna redirecto the hash here
tags_path = "./test/"			#TODO clean this mess up, use variables more

""" 
	STEPS:
	1. seperate part to directory and directory name
	2. archive & compress dir, save as archive.tar.gz to same path
	3. hash tarball, save to file in same directory as db
	4. read hash into variable, save that and directory name to new_entry
	5. append this to the db 'entries' list
	6. create $hash .tags file, also create .tree file with tree output
"""

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

"""
	2. archive & compress dir, save as archive.tar.gz to same path

"""

print("archiving and compressing directory")

#execute tar command
tar_command = ['tar', '-zcvf',  output_filepath, 'directory_path']

if call(tar_command) != 0 :
	print("tar returned nonzero exit code, something screwed up")
	print("assume archive is corrupted, ")
	print("rerun this step before moving on to next step")
	exit()

print("tarball created successfuly")
print("tarball path: " + output_filepath  )

"""
	3. hash tarball, save to file in same directory as db

"""

print("hashing tarball")

#save md5 hash of archive to file
hash_command = ['md5sum', output_filepath, '>', hash_path]

if call(hash_command) != 0 :
	print("tar returned nonzero exit code, something screwed up")
	print("assume archive is corrupted, ")
	print("rerun this step before moving on to next step")
	exit()
print("md5 hash created successfully")

"""
	4. read hash into variable, save that and directory name to new_entry

	new_entry	#json object containing name and hash of directory
"""

#read hash from file
dir_hash = open(hash_path)

#create new database entry
new_entry = {'name':directory_name, 'hash': dir_hash}

"""
	5. append this to the db 'entries' list

	data	#json database containing all entries
"""
# load db into $data variable
with open(db_path) as data_file:
	data = json.load(data_file)

#add new entry to database
data["entry"].append(new_entry)

#save back to file
with open('db_path', 'w') as data_file_w : 
	json.dump(data, data_file_w)

print("new entry added to database successfully")

"""
	6. create $hash .tags file, also create .tree file with tree output

"""
#TODO have this open up $EDITOR so user can add tags now, or do some kind of interactive where user enters one by one and we add to csv with each \n

tags_command = ['echo', '"add your tags for the backed up directory here, dont forget to delete this sentence!"', '>', tags_path + dir_hash + '.tags']

tree_command = []

#execute tree
#execute echo

#!/usr/bin/env python2.7
import json
from pprint import pprint
from subprocess import call
from sys import exit

#global variables yay

directory_path = "./test/backmeup"	# eventually take this from args
db_path = "~/.chipmunk/"		#location of db

#these are all placeholders, will overwrite in seperate_path
path = "directory path"
directory_name = "dir name"
output_filepath = "archive output filepath"

#hash tarball
hash_path = "path + hash.txt"

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

"""
1. seperate directory to backup name and path

path 		#directory path, string
directory_name	#directory name, string
output_filepath	#path archive will be output to 
"""
print("directory backup process has begun")

#seperate directory name from rest of path
directories_list = directory_path.split("/")
last_item_index = len(directories_list) -1

#get name of directory
directory_name = directories_list[last_item_index]
print("directory to be backed up: " + directory_path)

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
tar_command = ['tar', '-zcvf',  output_filepath, directory_path]
	
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

#create hash path
hash_path = path + 'hash.txt'

#touch hash file
#touch_command = ['touch', hash_path]
#if call (touch_command) != 0 :
#	print("error touching hash file")
#	exit()

#open file so we can write to it 
diskhash = open(hash_path, 'w')

#save md5 hash of archive to file
hash_command = ['md5sum', output_filepath]
if call(hash_command, stdout=diskhash) != 0 :
	print("tar returned nonzero exit code, something screwed up")
	print("assume archive is corrupted, ")
	print("rerun this step before moving on to next step")
	exit()

print("md5 hash created successfully: "+ hash_path)

# also write current hash to .current_hash.temp file to keep track of current
# hash between scrips
#TODO


"""	
4. read hash into variable, save that and directory name to new_entry

"""
	
#read hash from file, grabbing hash from md5sum's output
with open(hash_path) as hashfile:
	dir_hash = hashfile.read().split()[0]
	

#create new database entry
new_entry = {'name':directory_name, 'hash': dir_hash}


"""
5. append this to the db 'entries' list

"""

print("creating and adding new database entry")

# load db into $data variable
with open(db_path + 'index.json') as data_file:
	data = json.load(data_file)

#add new entry to database
data["entries"].append(new_entry)

#save back to file
with open(db_path + 'index.json', 'w') as data_file_w : 
	json.dump(data, data_file_w)

print("new entry added to database successfully")


"""
6. create $hash .tags file, also create .tree file with tree output
"""
#TODO  do some kind of interactive where user enters one by one and we add to csv with each \n
#while loop

#print("creating tags file")
#touch_command = ['touch', db_path + dir_hash + '.tags.csv']
#if call(touch_command) != 0 :
#	print("failed to touch tags file")
#	exit()

#open tags file for writing to
tags_file = open(db_path + dir_hash + '.tags.csv', 'w')
tags_command = ['echo', '"tags"'] 
if call(tags_command, stdout=tags_file) != 0 :
	print("creating tags file failed for some reason")
	print("rerun this script ")
	exit()
	
#print("creating tree file")
#touch_command = ['touch', db_path + dir_hash + '.tree']
#if call(touch_command) != 0 :'
#	print("failed to touch tree file")
#	exit()

#open tree file for writing to
print("tree-ing directory: " + directory_path)
tree_file = open(db_path + dir_hash + '.tree', 'w')
tree_command = ['tree', 'directory_path']
if call(tree_command, stdout=tree_file) != 0 :
	print("tree command returned error")
	print("failed to write to tree file")
	exit()
	

print("directory archived and data files created successfully ")


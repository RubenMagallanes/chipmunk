#!/usr/bin/env python2.7
import json
from pprint import pprint


filepath = "./index.json"

with open(filepath) as data_file:
	data = json.load(data_file)



#data["entries"] 
pprint(data["entries"][0])


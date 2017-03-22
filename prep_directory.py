#!/usr/bin/env python2.7
import json
from pprint import pprint


filepath = "./index.json"

with open(filepath) as data_file:
	data = json.load(data_file)

entry = {'newkey': 'newvalue'}
data.update(enrty);
with open('filepath', 'w') as f:
	json.dump(data, f);



# demonstrates how to append to json objects, 

#pprint(data["entries"])
#data["entries"].append({"hash":"19817312731298dicks", "name": "new_entry"})
#pprint(data["entries"])

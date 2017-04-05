#! /usr/bin/env python2
import os

#assume ~/.chipmunk/client-secrets.json exists
file_body = '''
{ 
	"web":{
		"client_id": "[[INSERT CLIENT ID HERE]]",
		"client_secret": "[[INSERT CLIENT SECRET HERE]]",
		"redirect_uris": [],
		"auth_uri": "https://accounts.google.com/o/oauth2/auth",
		"token_uri": "https://accounts.google.com/o/oauth2/token"
	}
}'''

filepath = os.path.expanduser('~/.chipmunk/client_secrets.json')

with open(filepath, 'w') as f:
	f.write(file_body)



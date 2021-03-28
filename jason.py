''' JavaScript Object Notation '''

import json

people_string = '''
{
	"people": [
	{
		"name":"john david",
		"phone":"09-6886-565",
		"email":["john@bob.com"],
		"has_license":false
	},
	{
		"name":"john smith",
		"phone":"09-7875-565",
		"email":["jsmith@bob.com"],
		"has_license":true
	}
	]
}
'''

# LOAD JSON

data = json.loads(people_string)
#print(data)

for person in data['people']:
    #print(person['name'])
    del person['phone']

new_string = json.dumps(data, indent=1, sort_keys=True)
#print(new_string)

#print(type(data['people']))












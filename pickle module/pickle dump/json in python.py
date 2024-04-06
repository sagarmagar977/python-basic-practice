#########################################################
import json
blog={
    'url':'www.wscubetech.com',
    'name':'wscubetech'
    }
to_json=json.dumps(blog)
# json is in string format in python  
print(type(to_json))
print(to_json)

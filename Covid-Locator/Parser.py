import pip._vendor.requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#def parseInts(obj){
    #var obj = JSON.parse('{ "name":"John", "age":30, "city":"New York"}');
#}
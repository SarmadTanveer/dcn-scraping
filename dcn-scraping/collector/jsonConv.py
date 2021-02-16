import json

def readList(name):
    data=[]
    with open(name+'.json', 'r') as read_file:
        data=json.load(read_file)
    return data

def writeList(name, data):
    with open(name+'.json', 'w') as write_file:
        json.dump(data, write_file, indent=4)
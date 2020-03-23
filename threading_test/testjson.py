import json



filename = 'username.json'

try:
    with open(filename, 'r') as obj:
        print(obj.read())
        users = json.load(obj.read())

        print(users)

except Exception as e:
    print(e)
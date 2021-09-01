import json

# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
# #converting this dict to a string in json
# person_json = json.dumps(person)
# #using optional arguments
# person_json2 = json.dumps(person, indent=4, sort_keys=True)
# print(person_json)
# print(person_json2)

# #if u want to save the result in a file
# with open('examples.json','w') as file:
#     json.dump(person,file, indent=4) #coverts person dict to json string and stores it in a file named examples.json

# #Or load data from a file and convert it to a Python object with the json.load() method.
# with open('examples.json', 'r') as file:
#     person = json.load(file)
#     print(person)

#Encoding a custom object with the default JSONEncoder will raise a TypeError. We can specify a custom encoding function that will store the class name and all object variables in a dictionary. Use this function for the default argument in the json.dump() method.
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User('nikki',19)
#custom encoding function to convert the obect to a dictionary
def custom_enc(obj):
    if isinstance(obj, User):
        return {'name':obj.name, 'age': obj.age, obj.__class__.__name__ : True}
    else:
        raise TypeError('not JSON serializable')
userJSON = json.dumps(user, default=custom_enc)
print(userJSON)
#decoding and converting to an object
def custom_dec(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct
user = json.loads(userJSON, object_hook=custom_dec)
print(user.name)
print(User.__name__)


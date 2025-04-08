import json

class Person():
    def __init__(self, name, phoneNumber, emailAddress):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress

p1 = Person("Stefan", "01234", "stefan@stefan.at")

# json.dumps(p1)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"name": obj.name, "phoneNumber": obj.phoneNumber, "emailAddress": obj.emailAddress}
            # return obj.__dict__
        return super(MyEncoder, self).default(obj)


jsonStr = json.dumps(p1, cls=MyEncoder)
print("Encoded JSON", jsonStr)

class MyPersonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.person_hook, *args, **kwargs)

    def person_hook(self, dct):
        if ("name" in dct):
            # decode Pet
            return Person(dct["name"], dct["phoneNumber"], dct["emailAddress"])


p2 = json.loads(jsonStr, cls=MyPersonDecoder)
print("Decoded Object", p2.name, p2.phoneNumber, p2.emailAddress)



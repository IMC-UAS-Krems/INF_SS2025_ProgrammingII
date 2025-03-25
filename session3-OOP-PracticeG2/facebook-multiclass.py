from datetime import datetime

class User:
    def __init__(self, name):
        self.name = name
        self.requests = RequestList()
        self.friends = FriendList()

    def addFriend(self, friend):
        request = Request(self, friend)
        friend.requests.add_request(request)

    def approve(self, request):
        request.approve()

    def reject_request(self, request):
        self.requests.remove_request(request)

class RequestList:
    def __init__(self):
        self.requests = []

    def add_request(self, request):
        self.requests.append(request)

    def remove_request(self, request):
        self.requests.remove(request)

    def __str__(self):
        strs = "".join((f"Add friend request from {r.sender.name}" for r in self.requests))
        return f"[{strs}]"

    def __getitem__(self, item):
        return self.requests[item]

class FriendList:
    def __init__(self):
        self.friends = []

    def __str__(self):
        strs = "".join((f"'{f.name}'" for f in self.friends))
        return f"[{strs}]"

    def append(self, friend):
        self.friends.append(friend)

class Request:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.request_date = datetime.now()
        self.status = "open"

    def approve(self):
        self.sender.friends.append(self.recipient)
        self.recipient.friends.append(self.sender)

    def __str__(self):
        return f"Add friend request from {self.sender.name}"


u1 = User("Joe")
u2 = User("Jill")
print (u1.name + " Friend List = " + str(u1.friends))
u1.addFriend(u2)
print (u2.name + " Friend Requests = " + str(u2.requests))
u2.approve (u2.requests[0])
print (u1.name + " Friend List = " + str(u1.friends))

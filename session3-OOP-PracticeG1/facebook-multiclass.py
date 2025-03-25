from datetime import datetime


class User:
    def __init__(self, name):
        self.name = name
        self.requests = RequestList()
        self.friends = []
        self.rejected_request = []

    def add_friend(self, friend):
        request = Request(self, friend)
        friend.requests.append(request)

    def approve_request(self, request):
        request.approve()

    def reject_request(self, friend):
        self.requests.remove(friend)

class RequestList:
    def __init__(self):
        self.requests = []
        self.cancelled_requests = []
        self.rejected_requests = []

    def add_request(self, request):
        self.requests.append(request)

    def remove_request(self, request):
        self.requests.remove(request)

class Request:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.request_date = datetime.now()
        self.status = "open"

    def approve(self):
        print(f"EventLog: {datetime.now()} {self.recipient.name} approved {self.sender.name}'s friend request")
        self.sender.friends.append(self.recipient)
        self.recipient.friends.append(self.sender)

    def __str__(self):
        return f"Add friend request from {self.sender.name}"

class FollowRequest:
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.request_date = datetime.now()

    def approve(self):
        print(f"EventLog: {datetime.now()} {self.recipient.name} approved {self.sender.name}'s friend request")
        self.sender.following.append(self.recipient)



u1 = User("Joe")
u2 = User("Jill")
print(u1.name + " Friend List = " + str(u1.friends))
u1.add_friend(u2)
print(u2.name + " Friend Requests = " + str(u2.requests))
u2.approve_request(u2.requests[0])
print(u1.name + " Friend List = " + str(u1.friends))

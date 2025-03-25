
class User(object):
    def __init__(self, name: str):
        self.name: str = name
        self.friends: list = []
        self.requests: list = []

    def addFriend(self, friend: 'User'):
        self.outgoing_requests.append(FriendRequest(self, friend))
        # friend.requests.append(self)

    def approve(self, request_index):
        requested_friend = self.requests[request_index]
        self.friends.append(requested_friend)
        print("Approving add friend request")
        requested_friend.friends.append(self)

        self.requests.pop(request_index)

class FriendRequest():
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

    def approve(self):
        print(f"This is an log entry to say that {self.sender} wants to be friends with {self.recipient}")
        self.sender.friends.append(self.recipient)
        self.recipient.friends.append(self.sender)
        self.recipient.requests.remove(self)

    def reject(self):
        pass

# * Test Code:
u1 = User ("Joe")
u2 = User ("Jill")
print (u1.name + " Friend List = " + str(u1.friends))
u1.addFriend(u2)
print(u2.name + " Friend Requests = " + str([i.name for i in u2.requests]))
u2.approve(0)
print(u1.name + " Friend List = " + str([i.name for i in u1.friends]))

u2.approve(0)
print(u1.name + " Friend List = " + str([i.name for i in u1.friends]))

#
# u1 = User("Joe")
# u2 = User("Jill")
# print(u1.name + " Friend List = " + str(u1.friends))
# u1.add_friend(u2)
# print(u2.name + " Friend Requests = " + str(u2.requests))
# u2.approve_request(u2.requests[0])
# print(u1.name + " Friend List = " + str(u1.friends))

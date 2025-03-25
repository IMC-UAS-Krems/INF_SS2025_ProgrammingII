class User:
    def __init__(self, name):
        self.name = name
        self.requests = []
        self.friends = []

    def __repr__(self):
        return self.name

    def add_friend(self, friend):
        friend.requests.append(self)

    def approve_request(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)
        self.requests.remove(friend)

    def reject_request(self, friend):
        self.requests.remove(friend)

u1 = User("Joe")
u2 = User("Jill")
print(u1.name + " Friend List = " + str(u1.friends))
u1.add_friend(u2)
print(u2.name + " Friend Requests = " + str(u2.requests))
u2.approve_request(u2.requests[0])
print(u1.name + " Friend List = " + str(u1.friends))

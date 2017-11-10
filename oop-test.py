class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def __str__(self):
        return self.first + ' ' + self.last


aFriend = Person('Jason','Taylor')

print(aFriend.first + ' ' + aFriend.last)
print(aFriend)

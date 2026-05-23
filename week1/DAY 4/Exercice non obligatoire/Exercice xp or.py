class Parrot():
    
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin():

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(bird):
    bird.fly()



def my_decorator(my_function):    # <-- (4)
    def inner_decorator():        # <-- (5)
        print("This happened before!")  # <-- (6)
        my_function()             # <-- (7)
        print("This happens after ")    # <-- (10)
        print("This happened at the end!")    # <-- (11)
    return inner_decorator
    # return None


@my_decorator       # <-- (3)
def my_decorated():    # <-- (2) <-- (8)
    print("This happened!")   # <-- (9)


my_decorated()    # <-- (1)



import datetime


def my_decorator(inner):
    def inner_decorator(num_copy):
        print(datetime.datetime.utcnow())
        inner(int(num_copy) + 1)
        print(datetime.datetime.utcnow())
    return inner_decorator


@my_decorator
def decorated(number):
    print("This happened : " + str(number))

decorated(5)


















class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = val
        MyClass.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count

object_1 = MyClass(10)
print("\nValue of object : %s" % object_1.get_val())
print(MyClass.get_count())

object_2 = MyClass(20)
print("\nValue of object : %s" % object_2.get_val())
print(MyClass.get_count())














class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        MyClass.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            print("Entered value is not an INT, value set to 0")
            return 0
        else:
            return value


a = MyClass(5)
b = MyClass(10)
c = MyClass(15)

print(a.val)
print(b.val)
print(c.val)
print(a.filterint(100))
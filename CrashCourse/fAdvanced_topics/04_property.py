#%% property
class MyClass:
    def __init__(self, my_prop = 0):
        self._my_prop = my_prop
  
    def get_my_prop(self):
        print("Getting value")
        return self._my_prop

    def set_my_prop(self, value):
        if value > 100:
            raise ValueError("value have to be under 100")
        print("Setting value")
        self._my_prop = value

    my_prop = property(get_my_prop,set_my_prop)

my_class = MyClass(19)
my_class.my_prop = 100

#%% @property
class MyFancyClass:
    def __init__(self, my_prop = 0):
        self._my_prop = my_prop

    @property #decorator
    def my_prop(self):
        print("Getting value")
        return self._my_prop

    @my_prop.setter
    def my_prop(self, value):
        if value > 100:
            raise ValueError("value have to be under 100")
        print("Setting value")
        self._my_prop = value

my_class = MyFancyClass(19)
print(my_class.my_prop)
my_class.my_prop = 10
print(my_class.my_prop)

class MyClass:
    value = 0

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


a = MyClass()
b = MyClass()

a.set_value(10)
b.set_value(100)
print('a = ', a.get_value())
print('b = ', b.get_value())
a.value = 100
print('Currently the value of a is ', a.get_value())
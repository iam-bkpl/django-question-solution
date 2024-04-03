class DescriptorDemo:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print("Value ...")
        return self._value

    @value.getter
    def value(self):
        print("Value getter")
        return self._value

    @value.setter
    def value(self,value):
        print("Value setter")
        self._value = value

    @value.deleter
    def value(self):
        print("Value deleter")
        del self._value


v1 = DescriptorDemo(4)
print(v1.value)
v1.value = 10
print(v1.value)
del v1.value

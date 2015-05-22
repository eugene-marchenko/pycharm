class MyClass:
    def __init__(self):
        self.var1 = 'say hello'

    def method(self, variable1):
        print 'hello'
        # print self.var1
        print variable1 * 2


test = MyClass()
test.method(123)
print test.var1
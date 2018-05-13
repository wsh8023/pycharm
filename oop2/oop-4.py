class Person():
    def fget(self):
        return self._name * 2
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = 'NoName'
    name = property(fget, fset, fdel,'对name进行操作')

p1 = Person()
p1.name = 'TuLing'
print(p1.name)
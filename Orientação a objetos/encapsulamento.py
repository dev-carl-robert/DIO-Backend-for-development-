<<<<<<< HEAD
class Foo:
    def __init(self, x=None):
        self._x = x
    
    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
         self._x = -1
            
foo = Foo(10)    
del (foo.x)
print(foo.x)
foo.x = 10
=======
class Foo:
    def __init(self, x=None):
        self._x = x
    
    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
         self._x = -1
            
foo = Foo(10)    
del (foo.x)
print(foo.x)
foo.x = 10
>>>>>>> 0020aee41afcea1bbeb5f4d05f5fcf334c8c9c6a
print(foo.x)
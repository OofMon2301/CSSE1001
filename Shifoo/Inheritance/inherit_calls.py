""" For each of obj1, obj2, obj3, and obj4, print the methods which are called following a call to objn.f(), where n is the number of the obj, in the format:

objn: call1, call2, call3

though there may be more or less than three calls.

Take care to insert spaces after the colon and the commas.

Study this below:

class C1():
    def f(self):
        return 2*self.g()

    def g(self):
        return 2

class C2(C1):
    def f(self):
        return 3*self.g()

class C3(C1):
    def g(self):
        return 5

class C4(C3):
    def f(self):
        return 7*self.g()

obj1 = C1()
obj2 = C2()
obj3 = C3()
obj4 = C4()

>>> objn.f()
objn: call1, call2, call3
"""
print("obj1: C1.f, C1.g")  # C1.f calls C1.g; no superclass methods are called
print("obj2: C2.f, C1.g")  # C2.f calls C1.g; no superclass methods are called
print("obj3: C3.f, C3.g")  # C3.f calls C3.g; no superclass methods are called
print("obj4: C4.f, C3.g")  # C4.f calls C3.g; no superclass methods are called

class A:
    @staticmethod
    def f(): #1
        print('static method')

    @classmethod
    def g(cls): #2
        print(cls.__name__)

if __name__ == '__main__':
    a = A()
    a.f()
    a.g()
    print(type(A.f))
    print(type(A.g))
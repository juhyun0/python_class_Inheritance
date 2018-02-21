#데코레이터: 꾸며준 것

class MyDecorator:
    def __init__(self,f):
        print("Initializing MyDecorator...")
        self.func=f

    def __call__(self):
        print("Begin :{0}".format(self.func.__name__))
        self.func()
        print("End :{0}".format((self.func.__name__)))

@MyDecorator

def print_hello():
    print("Hello.")

#print_hello=MyDecorator(print_hello)

print_hello()
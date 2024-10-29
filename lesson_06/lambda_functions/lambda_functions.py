def with_return(num):
    return num ** 2

def say_hello():
    print("Hello")


greet = lambda : print("Hello World!")

greet()

square = lambda num: num ** 2


res = square(10)
print(res)
print(square(5))

print(with_return(15))
say_hello()

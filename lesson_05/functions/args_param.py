def my_function(*args: int):
    for arg in args:
        print(arg, end=" ")
    print("\n===========")

my_function(1, 2, 3)
my_function(1, 2, 3, 4, 5)
my_function()


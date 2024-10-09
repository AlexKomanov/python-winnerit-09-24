def greet_no_args():
    print(f"Hello, Alex!")


def greet(name: str):
    # print(f"Hello, {name}!")
    print("Hello, " + name + "!")

greet_no_args()
greet("Alex")

my_string = "HelLO"
lower_string = my_string.lower()  # 'hello'
# print(lower_string)
# print(my_string)

my_string = "Hello"
upper_string = my_string.upper()  # 'HELLO'
# print(upper_string)

my_string = " \t\t\t  Hello  \t\t\t\t        "
stripped_string = my_string.strip()  # 'Hello'
# print(my_string)
# print(stripped_string)

my_string = "Hello, World!"
new_string = my_string.replace("World", "Python")  # 'Hello, Python!'
# print(my_string)
# print(new_string)

my_string = "Hello World Of Python"
# print(len(my_string)) # 21
# words = my_string.split()  # ['Hello', 'World', 'Of', 'Python']
# print(words)

words = ['Hello', 'World!']
joined_string = " ".join(words)  # 'Hello World!'
# print(joined_string)
# print(joined_string.split())

my_string = "Hello, World!"
index = my_string.find("World")  # 7
# print(index)
index = my_string.find("Worldaaaaaa")  # -1
# print(index)

my_string = "Hello, World!"
result = my_string.startswith("Hello")  # True
# print(result)
result = my_string.endswith("World!")  # True
# print(result)

# equals
# print("hello" == "hello") # True
# print("Hello" == "hello") # False
# print("hello" == "hellowww") # False
# print("Hello".lower() == "hello".lower()) # True

# contains
# print("World" in "Hello World!")
# print("world" in "Hello World!")
# print("world".lower() in "Hello WoRld!".lower())





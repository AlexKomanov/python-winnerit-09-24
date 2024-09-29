my_string = "Hello"
lower_string = my_string.lower()  # 'hello'

my_string = "Hello"
upper_string = my_string.upper()  # 'HELLO'

my_string = "   Hello   "
stripped_string = my_string.strip()  # 'Hello'

my_string = "Hello, World!"
new_string = my_string.replace("World", "Python")  # 'Hello, Python!'

my_string = "Hello, World!"
words = my_string.split(", ")  # ['Hello', 'World!']

words = ['Hello', 'World!']
joined_string = ", ".join(words)  # 'Hello, World!'

my_string = "Hello, World!"
index = my_string.find("World")  # 7
index = my_string.find("Worldaaaaaa")  # -1
print(index)

my_string = "Hello, World!"
result = my_string.startswith("Hello")  # True
result = my_string.startswith("World")  # False
print(result)

# equals
"hello" == "hello"  # True
"Hello" == "hello"  # False (בגלל ההבחנה בין רישיות לקטנות)

# contains
# print("World" in "Hello World!")
# print("world" in "Hello World!")
# print("world".lower() in "Hello WoRld!".lower())





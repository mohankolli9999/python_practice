# import math
# "JUST STARTED CODING"
# first = "Mohan"
# last = "Kolli"
# full = f" {first} {last}"
# print(full)
# course = "python programming"
3  # print(course.upper())
# print(course)
# print(math.log10(100))
# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y})
# temperature = input("temperature:")
# if int(temperature) > 30:
# elif int(temperature) < 30:
# print("wear a sweater")
# else:
# print("edokasti chesko po")
# print("program done")
# for number in range(10):
# print("Attempt", number + 1, (number + 1) * ".")

# successful = input("is the attempt successful? :")
# for number in range(1, 4):
# if bool(successful):
# print("Message sent")
# break
# else:
# print("message failed to sent after 3 attempts")

# for x in range(5):
# for y in range(3):
# print(f"{x} , {y + 1}")

# number = 10
# while int(number) > 0:
# print(number)
# number //= 2


# command = ""
# while command.lower(quit) != "quit":
# command = input(">")
# print("Echo", command)


# for x in range(1, 10):
# while int(x % 2) == 0:
# print(x)
# break

# print("we have 4 even numbers")


# count = 0
# number = int(input("number: "))
# while number > 0:
# print(number)
# number = int(number / 2)
# count += 1

# print(count)


# def greet():
# print("Hi")
# print("Ratnala cheruvu Raj")


# greet()

# def greet(full_name, batch_name):
# print(f"Hi {full_name} of {batch_name} Welcome")


# greet("Mohan", "btech")
# greet("lafoot", "ninja")


# def multiply(*numbers):
# total = 1
# for number in numbers:
# total *= number
# return total


# print(multiply(2, 3, 4, 5))


# def save_user(**user):
# print(user["name"])


# save_user(id=1, name="Mohan", work="student")
# save_user(id=2, name="kolli", work="student")

# def fizz_buzz(input):
# if input % 3 == 0 and input % 5 == 0:
# print("fizzbuzz")
# elif input % 3 == 0:
# print("fizz")
# elif input % 5 == 0:
# print("Buzz")

# else:
# print(input)


# fizz_buzz(45)

# items = [("Product0", 190),    ("Product1", 90),    ("Product2", 10),]

# items.sort(key=lambda x: x[1])
# print(items)

# x = map(lambda item: item[1], items)
# for items in x:
# print(items)


# x = 10
3  # y = 11

# z = x
# x = y
# y = z

# print(f"{x},{y}")

# point = dict(x=1, y=2, z=3)

# for x in point:
# print(x, point[x])

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
# print(fruit)

# values = range(5)
# print(*values)

sentence = "This is a common interview question"
alphabet = list(sentence)
print(alphabet)

print("Hello world")
number = input("Enter number: ")
print("Entered number " + number)

# list
colors = ["red", "blue", "yellow", "pink", "green"]
print(colors)
print(colors[0])
print(colors[-1])
print(colors[-3])
print(colors[1:])
print(colors[1:3])
print(colors[:2])
colors.append("brown")
colors.extend(["white", "black"])
print(colors)
colors.insert(1, "Purple")
print(colors)
print(colors.count("Purple"))
colors.sort()
print(colors)
copy_colors = colors.copy()
print(colors)

# tuple
# tuples are immutable in nature
coordinates = (4, 5)
print(coordinates)

# list
even_numbers = [46, 90, 86]
print(coordinates)


# Function
def say_hello(name):
    print("Hello " + name)


def cube(num):
    return num * num * num


say_hello("Mike")
print(cube(4))
print(cube(5))


# if-else
if int(number) % 2 == 0:
    print("Even number")
else:
    print("Odd number")

if int(number) % 10 == 0:
    print("Divisible by 10")
elif int(number) % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 10 and 5")

# Dictionaries
months = {
    "Jan": "January",
    "Feb": "February"
}

print(months.get("Jan"))
print(months.get("jan", "NOT_FOUND"))

# while loop
i = 1
while i < 3:
    print(i)
    i += 1



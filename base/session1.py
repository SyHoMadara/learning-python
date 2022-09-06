print("something", "another thing", sep=",", end="\n")

# Formatting strings
# we can use as f"string{Object}"
number_of_tabs = 10
print(f"number of tabs is {number_of_tabs}")
print("number of tabs is {} and we say {} to each other"
      .format(number_of_tabs, "hi"))

#---------------------------###-----------------------------#
# identifiers.
a = int("10")
b = str("10")
c = float("10")
print(a, b, c)

# casting
a = 3.141592
b = int(a)
c = str(a)
print(a, b, c)


#---------------------------###-----------------------------#
# we don't need any identifier for variables and we can change it every time that we want.
a = 10
print(a)
a = "hi hi"
print(a)

# operations
print(10+3, 10*3, 10/3, 10//3, 10 % 3, 10**3, sep='\n')
# we can assign value with these operator.
a = 10
b = 50
a = a + b
# or
a = 10
a += b


#---------------------------###-----------------------------#
# getting inputs
a = input("type your name: ")
print(f"your names is{a}")
" Exr: get number n and multiplay it by 10"


#---------------------------###-----------------------------#
# conditions
condition, condition2 = True, False
if condition:
    pass
elif condition2:
    pass
else:
    pass

a = 10
if a > 10:
    a /= 10
elif a < 10:
    a *= 10
else:
    print(a)


#---------------------------###-----------------------------#
# work with lists
l = []
l = list()
l = [1, 2, 3, 4]
l = list([1, 2, 3, 4, 5])
l.append("10")
l.append(l)
l += [12]
l += [[7, 8]]


# work with dict
d = {}
d = dict()
d["name"] = "Hosein"
d["family name"] = "Sarafrazi"
d["hight"] = 179
d["github"] = "https://github.com/SyHoMadara"


#---------------------------###-----------------------------#
# loops format
condition = True
while condition:
    # do something
    pass
"for example"
i = 0
while i < 10:
    print(i)
    i += 1

list_of_things = []
for element in list_of_things:
    # do something
    pass

for i in range(10):
    print(i)

# what is range function. We can use as follow.
print(type(range(10)), list(range(10)))
print(list(range(4, 10)))
print(list(range(10, 1, -1)))


#---------------------------###-----------------------------#
# Exercises.
# Q1: https://quera.org/problemset/3537/
# Q2: calculate "n!" with getting number n.

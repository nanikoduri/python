
# Defining If
number = 5
if number == 5:
    print("The value of number = 5")
else:
    print("The Number is NOT 5")

# Truthy and Falsy Values
number = 10
if number:
    print("The Number is Defined and Truthy")

text = "Python"
if text:
        print ("The Text is Defined and Truthy")

# Not If
number = 5
if number != 5:
    print("This Will not execute")

python_course = True
if not python_course:
    print("This will also not execute")

# MULTIPLE IF CONDITIONS
number = 5
python_course = True
if number == 5 and python_course:
    print("The Condition is True")
else:
    print("The Condition is False")

if number != 15 or python_course:
    print("The Condition is True")
else:
    print("The Condition is False")

# Ternary  IF statements
a = 1
b = 10
"Bigger" if b > a else "Smaller"

#Printing List Elements

students_name = ["Nani", "Kavya", "Leela"]
print(students_name[0])

x = 0
for index in range(10):
    x += 10
    print("The value of X is {0}" .format(x))

c = "Hi There!"
print(c[3])

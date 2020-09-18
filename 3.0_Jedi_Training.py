# Sign your name:________________
# In all the short programs below, do a good job communicating with your end user!

# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name = input ("What is your name: ")
print ("Hello" + name)

# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base= float (input ("what is the base: "))
height= float (input (" what is the height: "))
mpg= base * height / 2
print (mpg)

# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius = float (input("what is the radius of a circle: "))
mpg= 2 * 3.14 * radius
print(mpg)


# 4. Ask a user for an integer and then print the square root.
number= int (input("type an integer number: "))
mpg= 2 ** number
print(mpg)

# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass= float (input ("what is the mass: "))
speed= float (input("what is the acceleration: "))
sum= mass * speed
print(sum)
print("get it?")



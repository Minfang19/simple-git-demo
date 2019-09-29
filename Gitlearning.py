
# Making Decision e6
side_num = int(input("""Find the area
1) Square
2) Triangle
Enter a number:"""))
if side_num == 1:
    squ_side = int(input("Enter the length of side:"))
    print(squ_side**2)
else:
    tri_height = int(input("Enter the height:"))
    tri_base = int(input("Enter the base:"))
    tri_squ = tri_base*tri_height/2
    print(tri_squ)


# Making Decision e5
side1 = int(input("Enter the length of side1:"))
side2 = int(input("Enter the length of side2:"))
side3 = int(input("Enter the length of side3:"))
if side1 == side2:
    if side1 == side3:
        print("This is an equilateral triangle")
    else:
        print("This is an isosceles triangle")
elif side1 == side3:
    if side1 == side2:
        print("This is an equilateral triangle")
    else:
        print("This is an isosceles triangle")
elif side2 == side3:
    if side2 == side1:
        print("This is an equilateral triangle")
    else:
        print("This is an isosceles triangle")
else:
    print("This is a scalene triangle")


if side1 == side2 == side3:
    print("This is an equilateral triangle")
elif side1 == side2 and side1 != side3:
    print("This is an isosceles triangle")
elif side2 == side3 and side2 != side1:
    print("This is an isosceles triangle")
elif side1 == side3 and side1 != side2:
    print("This is an isosceles triangle")
elif side1 != side2 != side3:
    print("This is a scalene triangle")



# Making Decision e4
shape = int(input("Enter the number of sides:"))
if shape == 3:
    print("It is a triangle")
elif shape == 4:
    print
else:
    print("Error")

# Making Decision e3
letter = input("Enter a letter:")
low_letter = str.lower(letter)
if low_letter == "a" or low_letter == "e" or low_letter == "i" or low_letter == "o" or low_letter == "u":
    print("letter is a vowel")
elif low_letter == "y":
    print("sometimes y is a vowel, and sometimes y is a consonant")
else:
    print("the letter is a consonant")


# Making Decision e2
number = int(input("Enter a number:"))
if (number % 2)== 0:
    print("This is a even number")
else:
    print("This is a odd number")

#Making Decision e1
weather = input("Is it raining?")
if weather == "yes": # use ==
    windy = input("Is it windy?")
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
       print("Take an umbralla")
else:
    print("Enjoy your day")

#03
firname = input("Enter your first name:")
len_firname = len(firname)
if len(firname) < 5:
    surname = input("Enter your surname:")
    fullname = firname + surname
    upper_fullname = str.upper(fullname)
    print(upper_fullname.split(' '))
else:
    print(str.lower(firname))

#e2 teacher's solusion
song = input("Enter your song:")
length = len(song)
print("There are", length, "chacaters in the song.")
start = int(input("a starting number")) #try seperate int(input)
end = int(input("a ending number"))
section = song[start : end] #remember the []
print("Slices of the value assigned to the variable called word:", section) #can we directly write in song[start:end]?

# 02 Exercise: Length and Slicing (23)
fla_song = input("Enter your favourite song:")
num_song = len(fla_song)
print("Your favourite song contains", num_song, "characters")
print("The starting number is:", fla_song[0])
print("The ending number is:", fla_song[-1])
print(fla_song.split(" ")) # The programme should also ask a starting number and an ending number and then display just that section of the text？



# 01 Exercise: Day old Bread
num_old_bread = input("Enter the number of loaves of day old bread:")
float(num_old_bread)
num_new_bread = input("Enter the number of loaves of day new bread:")
float(num_new_bread)
regular_pri = 3.49
discount_pri = regular_pri * 0.40
total_pri = float(num_new_bread) * regular_pri + float(num_old_bread) * discount_pri
print("Total:", "%.2f"%total_pri, "Pounds")











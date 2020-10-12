######################################################################
# Author: Thy H. Nguyen     
# Username: nguyent2        

# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
# Citation about List: http://cs.berea.edu/courses/csc226book/lists.html
# Citation about List: http://cs.berea.edu/courses/csc226book/lists_part_b.html

######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
from time import sleep      # Import the sleep module to make the codes fancier.
print ("\nDo you want to know more about yourself? ")
thyhnguyen = input( "If yes, can you tell me when were you born? [Your year of birth needs to be between 2000 and 2011] ")
sleep(1)
# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples

#This is my third way to solve the problem
print()
thy = ["Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit"]
# Created a list containing all Chinese Zodiac animals, since the last two digits of the birth year (which is saved in thyhnguyen) will be corresponding to the order of the item in the list.
# Citation about List: http://cs.berea.edu/courses/csc226book/lists.html
# Citation about List: http://cs.berea.edu/courses/csc226book/lists_part_b.html
try: #This try and except helps check whether thyhnguyen can be successfully transferred to an integer or not
    a = int(thyhnguyen)
    thuy = int(thyhnguyen[-2:])
    if 2000 <= int(thyhnguyen) <= 2011:
        print("What a surprise! Your Chinese Zodiac animal is a",thy[thuy],".")
    else:
        print("Can you please enter the birth year between 2000 and 2011? \nRe-enter your birth year to see the surprise!")
    sleep(3)
except ValueError: #When the user inputs a float, or a string, it will go to this condition
    print("Can you please enter the birth year between 2000 and 2011? \nRe-enter your birth year to see the surprise!")

"""
This is my first way to solve the problem:

if thyhnguyen == 2000:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[0],".")
elif thyhnguyen == 2001:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[1],".")
elif thyhnguyen == 2002:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[2],".")
elif thyhnguyen == 2003:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[3],".")
elif thyhnguyen == 2004:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[4],".")
elif thyhnguyen == 2005:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[5],".")
elif thyhnguyen == 2006:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[6],".")
elif thyhnguyen == 2007:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[7],".")
elif thyhnguyen == 2008:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[8],".")
elif thyhnguyen == 2009:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[9],".")
elif thyhnguyen == 2010:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[10],".")
elif thyhnguyen == 2011:
    print ("What a surprise! Your Chinese Zodiac animal is a" , thy[11],".")
else:
    print("Can you please enter the birth year between 2000 and 2011? \nRe-enter your birth year to see the surprise!")
"""

######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year

print ("\nNow, you have known your Chinese Zodiac animal. What about your friend? \nAre you curious about your friend's Chinese Zodiac animal?")
birth_year = (input("What is your friend's year of birth? [Make sure that you remember to enter a year between 2000 and 2011] "))
print()
    # TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year

# This is my fourth way to solve this problem
try: #try and except, once again, checks to see whether birth_year can be successfully transferred to be an integer
    b = int(birth_year)
    thyy = int(birth_year[-2:])
# Citation: http://cs.berea.edu/courses/csc226book/lists.html
# Citation: http://cs.berea.edu/courses/csc226book/lists_part_b.html

    if 2000 <= int(birth_year) <= 2011:
        for i in range(12): #loop 12 times
            if i == thyy:
                print("Your friend's Chinese Zodiac animal is a", thy[i],".") #Since the last 2 digits of birth_year is corresponding to the order of the item in the list
            else: # if i != thyy - it means that if i is not equal to thyy:
                i+=1 #if the last 2 digits of birth_year is not equals to the time of looping, loop again.
    else:
        print("Did you remember to enter a birth year between 2000 and 2011? \nPlease try again!")
except ValueError:
    print("Did you remember to enter a birth year between 2000 and 2011? \nPlease try again!")

"""
This is my second way to solve this problem
if thyy == 00:
    print ("Your friend's Chinese Zodiac animal is a Dragon.")
elif thyy == 1:
    print ("Your friend's Chinese Zodiac animal is a Snake.")
elif thyy == 2:
    print("Your friend's Chinese Zodiac animal is a Horse.")
elif thyy == 3:
    print("Your friend's Chinese Zodiac animal is a Goat.")
elif thyy == 4:
    print("Your friend's Chinese Zodiac animal is a Monkey.")
elif thyy == 5:
    print("Your friend's Chinese Zodiac animal is a Rooster.")
elif thyy == 6:
    print("Your friend's Chinese Zodiac animal is a Dog.")
elif thyy == 7:
    print("Your friend's Chinese Zodiac animal is a Pig.")
elif thyy == 8:
    print("Your friend's Chinese Zodiac animal is a Rat.")
elif thyy == 9:
    print("Your friend's Chinese Zodiac animal is a Ox.")
elif thyy == 10:
    print("Your friend's Chinese Zodiac animal is a Tiger.")
elif thyy == 11:
    print("Your friend's Chinese Zodiac animal is a Rabbit.")
else:
    print("Did you remember to enter a birth year between 2000 and 2011? \nPlease try again!")

"""

######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.


# TODO print if you are a strong match, no match, or in between

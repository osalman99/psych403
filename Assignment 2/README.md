# This is assignment 2: Level ): "A new language"

# Operation exercises

print(5/2)
print(5.0/2.0)
# 1. Both produced a float because the answer the answer to both the division statments is a float 2.5 (i.e, there is no rounding using the / operator).

 
print(10 % 2)
print(10 % 5)
print(10 % 3)
print(10 % 4)
# 2. The modulo operator % gives use the remainder of x/y

 
print(2**3)
print(1**3)
print(3**2)
# 3. ** Allows you to use exponents.

print("new")
print(2//3)
print(2//2)
print(2//1)
print(-2//3)
# The / operator divides the x by the y (in x/y) to give us a float, while the // operator gives an integer rounding down in with positive quotient and rounds away from zero with negative quotients.
 
print(3/2*(2-3)**2+1)
print(2 + 8 + 2 * 2 / 2)
# 4. Yes, python does follow order of operations.

# Variable exercises

# 1. 
letter1 = 'O'
letter2 = 'M'
letter3 = 'A' 
letter4 = 'R'

# 2. Yes, the variables letter1 through letter4 show up in variable editor.


letterX = 'O'
print(letter1 and letterX)
print(letter1, letterX)
print (letter1)
print(letterX)
# 3. You can print both variables in with a varity of print statements without having any issues (i.e., different variables having the same value is not a problem and will run in the console).


letterX = 'S'
print(letter1 and letterX)
print(letter1, letterX)
print (letter1)
print(letterX)
# 5. No, redefining letterX did not change the previouse value (python runs without having any issues).
 
letterX = letter1
print(letter1 and letterX)
print(letter1, letterX)
print (letter1)
print(letterX)

letter1 = 'Z'
print(letter1 and letterX)
print(letter1, letterX)
print (letter1)
print(letterX)
# 6. letterX stayed the same even after letter1 was changed. This tells you that python variable assignment is prioratized from top to bottom (i.e., program is read from top to bottom) and when run changes to variables will only occur in lines that post redefining that variable.

# Boolean exercises
 
print("1")
print("1.0")

# 1. No because the quotations indicates a string. We can test this by using ==
print("1" == "1.0")

print(1 == 1.0)
# However, if there was no quotations, then it would be equivalent. The only difference would be that one is an integer and the other a float, and could also be tested using ==

print(5 == (3+2))
# 2. Yes this is equivalent (i.e., True).

# 3. 
print(1 == 1.0 or "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 and not "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 and not "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 and not "1" == "1.0" or not 5 == (3+2))

# List excerses 

oddlist = [1, 3, 5, 7, 9] 
# 1. Yes, this is variable. 

print(oddlist) 
# 2. Printing oddlist runs smooth.

print(len(oddlist)) 
# 3. It says it is 5 items long. 

print(type(oddlist)) 
# 4. Python says the oddlist is a <class 'list'>.

intlist = range(101) # 5. 
print(list(intlist)) # 5. 
# 6. Yes, all numbers 0 through 100 are listed. Because Python starts counting from 0, this means that intlist contains 101 numbers. I could have also just have specified the range with (0, 101).

# Dictionary exercise

# 1.
about_me = {0 : 'Omar Salman', 1 : 22.0, 2 : 4, 3 : 'Pizza' } 
 
print(type(about_me)) 
# 2. Yes, the file type is dict. 

print(len(about_me)) 
# 3. Yes, Python can determine the length of the dictionary about_me is 4 items. 

# Array exercises
import numpy as np

mixnums = np.array ([1, 2, 3, 4.0, 5.0, 6.0])
print(mixnums) 
# 1. The array output is [1. 2. 3. 4. 5. 6.], where all the numbers have a decimal without a didget following that decimal (became an array of floats).

mixtypes = np.array([1, 2, 3.0, 4.0, 'A', 'B'])
print(mixtypes) 
# 2. The array output is ['1' '2' '3.0' '4.0' 'A' 'B'], where all the values have quotations (became an array of strings).

# 3.
oddarray = np.arange(1, 101, 2)  
print(oddarray) 

# 4.
logarray = np.logspace(1, 5, 16) 
print(logarray)

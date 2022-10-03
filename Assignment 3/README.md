# Python Tutorial: Level 1 Exercises

# Variable operations exercises

# 1. 
sub_code = 'sub' 
subnr_int = 2
sub_str = '2'

print(sub_code + subnr_int) 
# You can only add two of the same type variables (i.e., a string cannot be concatenated with an integer, rather you can only concatenate a str to str).
print(sub_code + sub_str)

# 2.
print(sub_code + " " + sub_str)
print(sub_code + " " + sub_str*3)
print((sub_code + sub_str)*3)
print(sub_code*3 + sub_str*3)

# List operations exercises 

# 1.
numlist = [1,2,3]
print (numlist*2)

# 2.
import numpy as np
numarr = np.array([1,2,3])
print(numarr*2) 
# Comparing multiplying arrays and lists: multplying arrays causes each value in the array being multipled by the specific multiplier ; where multiplying a list yeilds replicating the list in its entirety proportonal to the multiplier. 

# 3. 
strlist = ['do', 're', 'mi', 'fa']
print([strlist[0]*2] + [strlist[1]*2] + [strlist[2]*2] + [strlist[3]*2])

strlist = ['do', 're', 'mi', 'fa']
print(strlist*2) 

strlist = ['do', 're', 'mi', 'fa']
print(strlist[0:1]*2 + strlist[1:2]*2 + strlist[2:3]*2 + strlist[3:4]*2)

strlist = ['do', 're', 'mi', 'fa'] 
print([strlist[0:1]*2, strlist[1:2]*2, strlist[2:3]*2, strlist[3:4]*2])

# Zipping exercises  

import numpy as np 

first_list = []

second_list = []

imgs_house = ['house1.png']*5 + ['house2.png']*5 + ['house3.png']*5 + ['house4.png']*5 + ['house.png']*5                                                                       
imgs_face = ['face1.png']*5 + ['face2.png']*5 + ['face3.png']*5 + ['face4.png']*5 + ['face5.png']*5

cues = ['cue1']*50 + ['cue2']*50 

first_list.extend(imgs_face)

first_list.extend(imgs_house)

first_list.extend(imgs_face) 

first_list.extend(imgs_house) 

img_fs = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png']*5                                                                 

img_hs = ['house1.png', 'house2.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png']*5 

second_list.extend(img_hs)

second_list.extend(img_fs) 

second_list.extend(img_hs)

second_list.extend(img_fs) 

catimgs = list(zip(first_list, second_list, cues))

np.random.shuffle(catimgs)
print(catimgs)

# Indexing exercises

# 1. 
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# 2.
print(colors[-1])

# 3.
print(colors[-3:-5:-1])

# 4. 
colors.remove('purple')
colors.append('indigo')
colors.append('violet')
print(colors)

# Slicing exercises

# 1. 
list100 = list(range(101))

# 2.
print(list100[0:10])

# 3.
print(list100[99::-2])

# 4. 
print(list100[:96:-1])

# 5.
thtoth = list100[40:44]
print(thtoth)
int_3943 = list(range(39,43))
print(int_3943)
print(thtoth == int_3943) 
# Statment is false, this is because the first number in the "list100" is indexed at 0 making the 40th number 40 thus, the sequence is 40, 41, 42, 43 which is not equal to 39, 40, 41, 42, 43.

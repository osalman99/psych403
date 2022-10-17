# Python Tutorial: Level 2 Exercises
 
# Conditional exercises 

# 1. 

response = ['1', '2', 'NaN']

if response == "1" or response == "2":
  
  print("OK")
  
elif response == 'Nan':
  
  print("subject did not respond")
  
else:
  
  print("subject pressed the wrong key")

    
# 2. 

response = '1'

if response == "1" or response == "2":
  
    if response == '1':
      
      print('Correct!')
  
    elif response == '2':
      
      print('Incorrect!')

elif response == 'NaN':
    
    print('subject did not respond')

else:
    
    print("subject pressed the wrong key")

# 3. Yes,  the scripted went the scritp as I expected it to and outputs the what is asked in the previous parts. 


# For loop exercises

# 1. 

name = 'Omar'
for nm in name:
    print(nm)
    
# 2. 
count = -1 
for nm in name: 
    count = count + 1
    
    name_count = nm + " %i" % count
    print(name_count)
    
# 3. 

name_list = ['Amy', 'Rory', 'River']

for lr in name_list:

    for i in lr:
      print(i)
    
# 4. 

for lr in name_list:
    count = -1 

    for i in lr:
        count+=1
        print(i,count)
       
# While loop exercises
 
# 1. 
i = 0

while i < 20:
    i = i + 1
    
    if i < 11 :
        print('image1.png')
        
    else:
        print('image2.png')

# 2. 
import random
valid_response = False 

while not valid_response: 
    print('image.png')

    user_response = random.randint(0,5)
    if user_response == 1 or user_response == 2:
        valid_response = True

# 3. 

import random
valid_response = False 
failsafe = 0 
iterations = 0 

while not valid_response:
    iterations+=1
    print('Showing an image for %i iterations' %iterations)
    print('image.png')
    
    user_response = random.randint(0,5)
    
    if user_response == 1 or user_response == 2:
        valid_response = True
        break 
    
    failsafe = failsafe + 1
    if failsafe == 5:
        print('There was 5 invalid responses... terminating...')
        break 

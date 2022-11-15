# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:43:35 2022

@author: ghani
"""

#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event, monitors

#-import file save functions
import json

#-(import other functions as necessary: os...)
import os, time

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_dir = os.getcwd()

#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')

#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')

#-check that these directories exist
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(data_dir):
    raise Exception("Could not find the path!")
if not os.path.isdir(image_dir):
    raise Exception('Could not find the path!')

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = {'session':'1', 'subject_nr':0, 'age':0, 'handedness':('right','left','ambi'), 'gender':'male'}
print(exp_info)

my_dlg = gui.DlgFromDict(dictionary = exp_info, title = "subject info", fixed = ['session'], order = ['session', 'subject_nr', 'age', 'gender', 'handedness'], show = False)
print("All variables have been created! Now ready to show the dialog box!")

my_dlg.show()
#get date and time
from datetime import datetime

date = datetime.now() #what time is it right now?
print(date)
exp_info['date'] = str(date.day) + '/' + str(date.month) + '/' + str(date.year)
print(exp_info['date'])

#-create a unique filename for the date\
cDatetime = str(exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'
print(cDatetime)

#create a subject info directory to save subject info
import os #cant we remove this and line 63
main_dir = os.getcwd() #define the main directory where experiment info is stored
sub_dir = os.path.join(main_dir,'sub_info',cDatetime) #create a subject info directory to save subject info
print(sub_dir)

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
ntrials = range(10)
nblocks = range(2)

#-stimulus names (and stimulus extensions, if images) *
stim_n = ['stim1', 'stim2', 'stim3', 'stim4', 'stim5', 'stim6', 'stim7', 'stim8', 'stim9', 'stim10']
if stim_n == ['stim1', 'stim2', 'stim3', 'stim4', 'stim5', 'stim6', 'stim7', 'stim8', 'stim9', 'stim10']:
    # image = stim_n + '.png'
    pass
#-stimulus properties like size, orientation, location, duration *
stim_size = [200,200]
stim_orien = [10]
stim_dur = 1

#-start message text *
strM = 'This is a Psychology experiment. If you are ready to start hit the ENTER key.'
#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
images = []
for num in range(1,10):
    image_file_str = "image_" + str(num) + ".jpeg"
    images.append(image_file_str)

for image in os.listdir(image_dir):
    if image not in os.listdir(image_dir):
        raise Exception("At least one image is missing from the directory")
    else:
        print(image, "was found")

#-create counterbalanced list of all conditions *
stims = ['stim']*10
imgs = ['img1.png', 'img2.png', 'img3.png', 'img4.png', 'img5.png',
'img6.png', 'img7.png', 'img8.png', 'img9.png', 'img10.png']

zippedlist = list(zip(stim_n,imgs))
print(zippedlist)

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
cor_resp = []
#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
par_resp = []
#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
accur_res = []
#-create an empty list for response time collection *
RT = []
#-create an empty list for recording the order of stimulus identities *
Ostim_ident = []
#-create an empty list for recording the order of stimulus properties *
Ostim_prop = []

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor')# should I add width= and distance=60
#mon.setSizePix(1920,1080) # should I add this
#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, color=['Black'], size=(1000,800), units= None, colorSpace='rgb255', fullscr=True)

my_image = visual.ImageStim(win, image = image_dir + '\car.jpg', size= (.25,.25), pos=(0,0))
my_image.draw()
win.flip()
event.waitKeys() #wait for keypress
win.close()

#-define experiment start text unsing psychopy functions
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor')# should I add width= and distance=60
#mon.setSizePix(1920,1080) # should I add this
#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, color=['Black'], size=(1000,800), units= "norm", colorSpace='rgb255', fullscr=True)

#Monitor and window exercises
#1. We can specify the units of the stimulus that is drawn on the window (the valuse include cm, pix, non, etc.). The size of the wiindow is in the form (x, y) and in pixels.
#2. colorSpace can use hex values or strings (ie., can be defined by name) and should be done before setting the color. It is a fixed range of defining a color.
#Stimulus exercises
#1. It stretches the image. Yes, it is kept by changing both the x and y by the same factor.

my_image = visual.ImageStim(win, image = image_dir + '\car.jpg', units="norm", size= (.25,.25), pos=(-1,1))
my_image.draw()
win.flip()
event.waitKeys(3)

#-define block (start)/end text using psychopy functions
start_msg = "Welcome to my experiment!"
start_text = visual.TextStim(win, text=start_msg)

end_msg = "This is the end of the experiment!"
end_text = visual.TextStim(win, text=end_msg)

#-define stimuli using psychopy functions
my_image = visual.ImageStim(win)

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text.draw()
win.flip()
#-allow participant to begin experiment with button press
event.waitKeys()

#Stimulus exercises
stims = os.listdir(image_dir) #create a list if images to show
my_image = visual.ImageStim(win)

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for nblock in nblocks:
    #-present block start message
    block_msg = "Press any key to continue to the next block."
    block_text = visual.TextStim(win, text=block_msg)
    block_text.draw()
    win.flip()
    event.waitKeys()
    #-randomize order of trials here *
    np.random.shuffle(zippedlist)

    #=====================
    #TRIAL SEQUENCE
    #=====================
    #-for loop for nTrials *
    for trial in ntrials:

        #-set stimuli and stimulus properties for the current trial
        my_image.image= os.path.join(image_dir, stims[trial])

        #=====================
        #START TRIAL
        #=====================
        # -draw fixation
        fixcross= '+'
        fixationtext=visual.TextStim(win,text=fixcross)
        fixationtext.draw()
        # -flip window
        win.flip()
        # -wait time (stimulus duration)
        event.waitKeys(3)

        # -draw image
        my_image.draw()
        # -flip window
        win.flip()
        # -wait time (stimulus duration)
        event.waitKeys(3)

        # -draw end trial text
        endText= 'End trail.'
        end_trial= visual.TextStim(win, text=endText)
        end_trial.draw()
        # -flip window
        win.flip()
        # -wait time (stimulus duration)
        event.waitKeys(3)
#======================
# END OF EXPERIMENT
#======================
#-close window
win.close()

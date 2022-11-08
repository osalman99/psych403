#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np

#-import psychopy functions
from psychopy import core, gui, visual, event 

#-import file save functions
import json 

#-(import other functions as necessary: os...)
import os, random

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
main_direc = os.getcwd()

#-define the directory where you will save your data
data_direc = os.path.join(main_direc,'data')

#-if you will be presenting images, define the image directory
image_direc = os.path.join(main_direc,'images')

#-check that these directories exist
if not os.path.isdir(image_direc):
    raise Exception("Could not find the path!")
if not os.path.isdir(data_direc):
    raise Exception("Could not find the path!")

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
ntrials = 10
nblocks = 2

#-stimulus names (and stimulus extensions, if images) *
stim_n = ['stim1', 'stim2', 'stim3', 'stim4', 'stim5', 'stim6', 'stim7', 'stim8', 'stim9', 'stim10'] 
if stim_n == ['stim1', 'stim2', 'stim3', 'stim4', 'stim5', 'stim6', 'stim7', 'stim8', 'stim9', 'stim10']:
	image = stim_n + '.png'

#-stimulus properties like size, orientation, location, duration *
stim_size = [200,200]
stim_orien = [10]
stim_dur = 1

#-start message text *
strM = 'This is a Psychology experiment. If you are ready to start hit the ENTER key.'
print(strM)
#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
images = []
for num in range(1,10):
    image_file_str = "image_" + str(num) + ".jpeg"
    images.append(image_file_str)

for image in os.listdir(image_direc):
    if image not in os.listdir(image_direc):
        raise Exception("At least one image is missing from the directory")
    else:
        print(image, "was found")

#-create counterbalanced list of all conditions *
stims = ['stim']*10
imgs = ['img1.png', 'img2.png', 'img3.png', 'img4.png', 'img5.png', 'img6.png', 'img7.png', 'img8.png', 'img9.png', 'img10.png']

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
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for nblock in nblocks:
    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(zippedlist) 
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for trial in range(ntrials):
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment

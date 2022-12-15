# Blindspotexperiment.py
"""This is a blind-spot experiment, which is a monocular vision test that finds and visualizes your blind spot. The blind-spot is a result of the anatomical
structure of the eye.The whole retina has photoreceptor cells (i.e., rods and cones). However, where the optic nerve and the retina meet, there is a small
area that lacks these photoreceptor cells, and is called the optic disk. Thus, the lack of photoreceptors at the optic disk is responsible for this monocular
phenomena. For a variety of reasons including the fact that humans have binocular vision, the blind-spot is not noticed in normal circumstances. This experiment
is a fun way to experience the blind spot. It highlights how our brain influences our visual experience, and that vision is a perceptual process
(i.e., the brain interprets incoming sensory information).
"""
# Omar Salman
# =====================
# IMPORT MODULE
# =====================
# import psychopy functions
from psychopy import visual, monitors, event, core, gui
# import other necessary functions.
from datetime import datetime
import pandas as pd
import os, random, math

# =====================
# PATH SETTINGS
# =====================
# define the main directory where you will keep all of your experiment files.
directory = os.getcwd()
# define the directory where you will save your data.
data_path = os.path.join(directory, 'data')
# check if directory exists, if not create directory.
if not os.path.exists(data_path):
    os.makedirs(data_path)

# =====================
# COLLECT PARTICIPANT INFO
# =====================
# dialogue box that will collect current participant number, age, gender, handedness, as well as the choice of test size.
parInfo = {'gender':('male','female','other','prefer not to say'),'subject_nr': 0, 'age':0, 'handedness':('right','left','ambi'), 'test_size': (60, 80, 100)}

mon = monitors.Monitor('myMonitor')
win = visual.Window(
    fullscr=False,
    monitor=mon,
    size=(800, 800),
    color='black',
    units='pix')

# Hide the mouse pointer when it is over the window.
win.mouseVisible = False

# define parameters for text and string that will be displayed in dialogue window.
parInfo_instr= visual.TextStim(win=win, wrapWidth=750)
parInfo_instr.text = """
Read the following instructions, so you can fill out next step of this experiment. \n
This is a blind spot experiment. \n
Please sit at a normal viewing distance from your computer monitor (i.e., arms length or approximately 60cm). \n
When prompted, please fill your personal information, which include: age, gender, handedness. \n
You can adjust the number of times a stimulus is presented to you, by change the 'test_size' parameter. Keep in mind each stimulus will last 2 seconds. \n
\n
Press Enter to proceed.
"""
# displays parInfo_instr.text in window.
parInfo_instr.draw()
win.flip()
event.waitKeys(keyList=['return'])
win.close()
# dialogue box that will collect participant info.
myDlg = gui.DlgFromDict(dictionary=parInfo, title='Fill personal info and select test_size:')
# get date and time
parInfo['date'] = datetime.now()
# naming data file
filename = (str(parInfo['subject_nr']) + '_blind_spot_data.csv')

# =====================
# STIMULUS AND TRIAL SETTINGS
# =====================
# number of trials and blocks
nTrials = int(parInfo['test_size'])
nBlocks = 2
totalTrials = nTrials * nBlocks
# Dot stimulus properties like size and of duration stimulus, as well as the possible location that the stimulus can be in, which is restricted by window parameters (i.e., display_x and display_y).
display_x = 1900
display_y = 800
stim_size = 10
stim_duration_time = 2

# =====================
# PREPARE CONDITION LISTS
# =====================
trial_coord = [] # list for coordinates.
pixels_per_inch = 142 # to convert inches to pixels. 1 inch is approximately 142 pixels.
box_near_side = math.floor(pixels_per_inch*5.75) # this is distance in pixels on the x-axis from the fixation.
box_far_side = math.floor(pixels_per_inch*6.75) # this is distance in pixels on the x-axis from the fixation.
y_ax_down = math.floor(pixels_per_inch*1.5) # this is distance in pixels on the y-axis from the fixation horizon.
y_ax_up = math.floor(pixels_per_inch*0.25) # this is distance in pixels on the y-axis from the fixation horizon.
# floor rounds down to give the nearest integer, this is done because you cant have a part of a pixel.

# randomly present 0.40 of dot stimulus along the window.
for i in range(int(totalTrials*.40)): trial_coord.append((random.randint(-(display_x / 2) + stim_size,
                                      (display_x / 2) - stim_size),
                      random.randint(-(display_y / 2) + stim_size,
                                      (display_y / 2) - stim_size)))
# randomly present 0.30 of the dot stimulus in the left blind spot 'box'.
for i in range(int(totalTrials*.30)): trial_coord.append((random.randint((-box_far_side) + stim_size,
                                       (-box_near_side) - stim_size),
                       random.randint((-y_ax_down) + stim_size,
                                       (y_ax_up) - stim_size)))
# randomly present 0.30 of the dot stimulus in the right blind spot 'box'.
for i in range(int(totalTrials*.30)): trial_coord.append((random.randint((box_near_side) + stim_size,
                                       (box_far_side) - stim_size),
                       random.randint((-y_ax_down) + stim_size,
                                       (y_ax_up) - stim_size)))
# to randomly present the dot stimuli, with specific weighting for the specified ranges.
random.shuffle(trial_coord)

# =====================
# PREPARE DATA COLLECTION LISTS
# =====================
# create necessary empty lists.
dotsPlotted = [0] * totalTrials # stimuli presented.
trialNumbers = [0] * totalTrials
blockNumbers = [0] * totalTrials
saw_dot = [0] * totalTrials # participant response hits.

# =====================
# CREATION OF WINDOW AND STIMULI
# =====================
# define the monitor settings
mon = monitors.Monitor('myMonitor')
# define the window (size, color, units, fullscreen mode)
win = visual.Window(
    fullscr=False,
    monitor=mon,
    size=(display_x, display_y),
    color='black',
    units='pix')

# define experiment start text
strt_txt = visual.TextStim(win=win, wrapWidth=750)
# define stimuli
fixation = visual.TextStim(win, text='+', color='white', height= 36)
stim = visual.Circle(win, size=(10, 10))
# Hide the mouse pointer when it is over the window
win.mouseVisible = False

# =====================
# START EXPERIMENT
# =====================
# present start message text
strt_txt.text = """
Hello and welcome to my experiment. \n
In this experiment, a dot stimulus will be presented multiple times and at the end of this experiment you will receive a 'map' of your blind spot. \n
\n
Press the ENTER key to proceed.
"""
strt_txt.draw()
win.flip()
event.waitKeys(keyList=['return'])

instruction_txt = visual.TextStim(win=win, wrapWidth=750)
instruction_txt.text = """
This is a monocular vision test, so you will have to close one eye to find its blind spot and the do the same for the other eye. \n
It is important for you to get into a comfortable position so the test is as accurate as possible. \n
You will align your open eye with the fixation cross (i.e., +) that will be at the center of your screen. \n
A blinking dot stimulus will be presented for about 2 secondes, click the spacebar when you see a dot, wait and repeat when the dot moves. \n
\n
Press the ENTER key to proceed.
"""
instruction_txt.draw()
win.flip()
event.waitKeys(keyList=['return'])

final_instr_txt = visual.TextStim(win=win, wrapWidth=750)
final_instr_txt.text = """
Remember to get and stay in a comfortable position and at a normal viewing distance from the monitor, so results are as accurrate as possible. \n
Stay focused on the fixation cross. \n 
NOTE: there will be a short delay before the first stimulus so you can focus on the fixation cross. \n
\n
Press ENTER to START the experiment.
"""
# allowing participant to begin experiment with button press (i.e., enter key).
final_instr_txt.draw()
win.flip()
event.waitKeys(keyList=['return'])

# =====================
# BLOCK SEQUENCE
# =====================
# block counter
b_counter = 0
# reset response time clock here
trial_timer = core.Clock()
# for loop for nBlocks
for block in range(nBlocks):
    b_counter = b_counter + 1
    if b_counter > 1:
        # present this message to prompt eye change at the start of block 2.
        instruction_txt.text = """
        Now switch to your other eye, press enter when your ready. \n 
        NOTE: there will be a short delay before the first stimulus so you can focus on the fixation cross."""

        instruction_txt.draw()
        win.flip()
        event.waitKeys(keyList=['return'])

    if b_counter == 1 or b_counter == 2:
        # 1.5 seconds after instructions for first and second block to give a chance to focus on fixation before presenting first dot stimulus for each eye.
        fixation.draw()
        win.flip()
        core.wait(1.5)

    # =====================
    # TRIAL SEQUENCE
    # =====================
    # for loop for nTrials
    for trial in range(nTrials):
        overallTrial = block * nTrials + trial
        blockNumbers[overallTrial] = block + 1
        trialNumbers[overallTrial] = trial + 1
        # =====================
        # START TRIAL
        # =====================
        # setting the location and size
        coord = trial_coord[overallTrial]
        stim.pos = coord
        stim.size = (stim_size, stim_size)
        dotsPlotted[overallTrial] = coord

        trial_timer.reset()
        event.clearEvents(eventType='keyboard')
        # while loop to draw stimulus, flip window, draw stimulus
        # while statement dictates stimulus duration
        while trial_timer.getTime() < stim_duration_time:
            fixation.draw()
            stim.draw()
            win.flip()
            fixation.draw()
            win.flip()
            core.wait(.5) # dictates rate of dot flicker.

        # Get information on which key was pressed.
        keys = event.getKeys(keyList=['space'])

        # collect subject response for that trial (i.e., accuracy is visualized at the end they either see it or miss).
        if keys:
            saw_dot[overallTrial] = True
        else:
            saw_dot[overallTrial] = False

        print(
            'Block:',
            block + 1,
            ', Trial:',
            trial + 1,
            ', coord of stim:',
            coord,
            ',', 'saw' if saw_dot[overallTrial] else 'did not see', 'stimulus',
        )
# ======================
# END OF EXPERIMENT
# ======================
# Show data before ending experiment, present text string to tell participant how to interpret experiment findings.
instruction_txt.text = """
The green dots are the dots you did not miss. \n
The red dots are the dots you missed.\n
The red dot cluster to the left of the fixation cross, represent the dots that fell in the blind-spot of your left eye. \n
The red dot cluster to the right of the fixation cross, represent the dots that fell in the blind-spot of your right eye. \n
\n
To view your results press ENTER \n
After viewing your results, press ENTER to close the window and end the experiment.\n
"""
instruction_txt.draw()
win.flip()
event.waitKeys(keyList=['return'])

# for loop to visualize missed and seen stimuli, by presenting them as red and green respectively.
for i in range(totalTrials):
    if saw_dot[i]:
        stim.color = 'green'
    else:
        stim.color = 'red'
    stim.pos = dotsPlotted[i]
    stim.draw()

# present visualised blind spot data.
win.flip()

# close window is controlled by waitKeys, so participant can look at results and then hit enter to close window.
event.waitKeys(keyList=['return'])
win.close()

# write data to a csv file.
df = pd.DataFrame(data={
    "Block Number": blockNumbers,
    "Trial Number": trialNumbers,
    "coord of stimulus": dotsPlotted,
    "Saw stimulus": saw_dot
})
df.to_csv(os.path.join(data_path, filename), sep=',', index=False)


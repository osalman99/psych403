
from psychopy import visual, monitors, event, core
import os, time

main_dir = os.getcwd()
images_dir = os.path.join(main_dir,'images')

mon = monitors.Monitor('myMonitor')
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon)

fixcross= '+'
fixationtext=visual.TextStim(win,text=fixcross)

end_msg = "This is the end of the experiment!"
end_text = visual.TextStim(win, text=end_msg)

# Wait exercises ===================================================
fixationtext.draw()
win.flip()
core.wait(2)
car_image = os.path.join(images_dir, "car0.png")
my_image = visual.ImageStim(win, image=car_image)
my_image.draw()
win.flip()
core.wait(2)

endText = 'End trial'
end_trial = visual.TextStim(win, text=endText)

end_trial.draw()
win.flip()
core.wait(2)

# Clock exercises ===================================================
# 1. core.wait is consistantly precise to the seconded decimal place.
# 2. Using the clock + while loop, is more precise than using core.wait; with accuracy to the third decimal place.
# 3. CountdonTimer + while loop, is as precise as clock + while loop; with accuracy to the tird decimal place.

"""Question. 1"""
nTrials = 3

# TRIAL SEQUENCE
trial_timer = core.Clock()
for trial in range(nTrials):
    my_image = visual.ImageStim(win)
    car_image = os.path.join(images_dir, "car" + str(trial) +".png")
    my_image.image = car_image

    fixationtext.draw()
    win.flip()
    core.wait(0.5)

    trial_timer.reset()

    my_image.draw()
    win.flip()
    core.wait(2)

    print('Trial '+str(trial)+': time =', trial_timer.getTime())

    end_text.draw()
    win.flip()
    core.wait(0.5)

win.close()

"""Question. 2"""
nTrials = 3

# TRIAL SEQUENCE
clock_wait_timer = core.Clock()
for trial in range(nTrials):
    my_image = visual.ImageStim(win)
    car_image = os.path.join(images_dir, "car" + str(trial) +".png")
    my_image.image = car_image

    fixationtext.draw()
    win.flip()
    core.wait(0.5)

    clock_wait_timer.reset()
    while clock_wait_timer.getTime() <= 2:
        my_image.draw()
        win.flip()
    print('Trial '+str(trial)+': time =', clock_wait_timer.getTime())

    end_text.draw()
    win.flip()
    core.wait(0.5)

win.close()

"""Question. 3"""
nTrials = 3

#TRIAL SEQUENCE
countdown_timer = core.CountdownTimer()
for trial in range(nTrials):
    my_image = visual.ImageStim(win)
    car_image = os.path.join(images_dir, "car" + str(trial) +".png")
    my_image.image = car_image

    fixationtext.draw()
    win.flip()
    core.wait(0.5)

    countdown_timer.reset()
    countdown_timer.add(2)
    start_time = time.time()
    while countdown_timer.getTime() > 0:
        my_image.draw()
        win.flip()
    end_time = time.time()
    print('Trial '+str(trial)+': time =', end_time - start_time)

    end_text.draw()
    win.flip()
    core.wait(0.5)

win.close()

"""Question. 4"""
nBlocks = 2
nTrials = 3

TRIAL SEQUENCE
block_timer = core.Clock()
for block in range(nBlocks):
    block_timer.reset()

    trial_timer = core.Clock()
    for trial in range(nTrials):

        my_image = visual.ImageStim(win)
        car_image = os.path.join(images_dir, "car" + str(trial) +".png")
        my_image.image = car_image

        fixationtext.draw()
        win.flip()
        core.wait(0.5)

        trial_timer.reset()
        my_image.draw()
        win.flip()
        core.wait(2)

        print('Trial '+str(trial)+': time =', trial_timer.getTime())

        end_text.draw()
        win.flip()
        core.wait(0.5)

    print('Block ' + str(block) + ': time =', block_timer.getTime())

win.close()

# Frame-based timing exercises ===================================================

# add information to record dropped frames
win.recordFrameIntervals = True # record frames
# give the monitor refresh rate plus a few ms tolerance (usually 4ms)
win.refreshThreshold = 1.0/60.0 + 0.004
# set durations
image_dur = 2.0 # 100 ms
refresh = 1/60

# set frame counts
image_frames = int(image_dur / refresh)  # whole number

nBlocks = 2
nTrials = 3
my_image = visual.ImageStim(win)
countdown_timer = core.CountdownTimer()
exceed_dropped_frame_threshold = False
for block in range(nBlocks):
    # =====================
    # TRIAL SEQUENCE
    # =====================
    dropped_frames = 0
    for trial in range(nTrials):
        # -set stimuli and stimulus properties for the current trial

        # =====================
        # START TRIAL
        # =====================
        fixationtext.draw()
        win.flip()
        core.wait(0.5)

        car_image = os.path.join(images_dir, "car" + str(trial) +".png")
        my_image.image = car_image

        st = time.time()
        if not exceed_dropped_frame_threshold:
            for frameN in range(image_frames):  # for the whole trial...
                my_image.draw()  # draw
                win.flip()  # show
            dropped_frames =+ win.nDroppedFrames
            print("number of dropped frames:", dropped_frames)
            if dropped_frames > 20:
                exceed_dropped_frame_threshold = True
                print("Over 20 frames were dropped so far in this experiment, using countdown timer")
        else:
            countdown_timer.reset()
            countdown_timer.add(image_dur)
            while countdown_timer.getTime() > 0:
                my_image.draw()
                win.flip()
        et = time.time()
        print("Time:", et - st)

        end_text.draw()
        win.flip()
        core.wait(0.5)

win.close()

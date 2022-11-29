from psychopy import core, event, visual, monitors
import csv, os
import numpy as np
import json as json
import panda

# Directory stuff
main_dir = os.getcwd()  # define the main directory where experiment info is stored
# point to a data directory to save the output
data_dir = os.path.join(main_dir, 'data')

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400, 400), color=[-1, -1, -1])

'''PsychoPy keypress exercises'''

# # 1.
# nTrials = 10
# my_text = visual.TextStim(win)

# rt_clock = core.Clock()
# cd_timer = core.CountdownTimer()

# for trial in range(nTrials):
#     rt_clock.reset()
#     cd_timer.add(2)

#     event.clearEvents(eventType='keyboard')

#     count = -1

#     while cd_timer.getTime() > 0:

#         my_text.text = "trial %i" % trial
#         my_text.draw()
#         win.flip()

#         keys = event.getKeys(keyList=['1', '2'])

#         if keys:
#             count = count + 1

#             if count == 0:
#                 resp_time = rt_clock.getTime()
#                 sub_resp = keys[0]

#     print("response that was counted was", sub_resp)

# win.close()

# 2. Statement placement is important because:
# When collecting responses and refreshing keypresses...
# Putting event.ClearEvents within the loop ensures that after the trial is finished, the keys variable is clear so that we could record the new subject response for the next trial
# Unindenting the 'if keys:' line would mean would lead to us fail to count the response time of the key press, rather it count the full 2 seconds.abs(x)

'''Recording data excerises'''
from psychopy import core, event, visual, monitors
import numpy as np

# monitor specs
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400, 400), color=[-1, -1, -1])

# blocks, trials, stims, and clocks
nBlocks = 2
nTrials = 4
my_text = visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer()  # add countdown timer

# prefill lists for responses
sub_resp = {}
sub_acc = {}
prob = {}
corr_resp = {}
resp_time = {}

# create problems and solutions to show
math_problems = ['1+3=', '1+1=', '3-2=', '4-1=']  # write a list of simple arithmetic
solutions = [4, 2, 1, 3]  # write solutions
prob_sol = list(zip(math_problems, solutions))

for block in range(nBlocks):
    prob[block] = {}
    corr_resp[block] = {}
    resp_time[block] = {}
    sub_resp[block] = {}
    sub_acc[block] = {}
    for trial in range(nTrials):

        # what problem will be shown and what is the correct response?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial]

        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3)  # add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial

        count = -1  # for counting keys
        while cd_timer.getTime() > 0:  # for 3 seconds

            my_text.text = prob[block][trial][0]  # present the problem for that trial
            my_text.draw()
            win.flip()

            # collect keypresses after first flip
            keys = event.getKeys(keyList=['1', '2', '3', '4', 'escape'])

            if keys:
                count = count + 1  # count up the number of times a key is pressed

                if count == 0:  # if this is the first time a key is pressed
                    # get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    # get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0]  # remove from list

        # record subject accuracy
        # correct- remembers keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1  # arbitrary number for accurate response
        # incorrect- remember keys are saved as strings
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2  # arbitrary number for inaccurate response
            # (should be something other than 0 to distinguish
            # from non-responses)

        # print results
        print('problem=', prob[block][trial], 'correct response=',
              corr_resp[block][trial], 'subject response=', sub_resp[block][trial],
              'subject accuracy=', sub_acc[block][trial])

win.close()

'''Save csv exercises'''
for block in range(nBlocks):
    # 'compressed' experiment...

    filename = 'savecsv_example.csv'
    main_dir = os.getcwd()  # the main directory where experiment info is stored
    exp_csv_file_path = os.path.join(data_dir, 'dict.csv')  # Output is saved in data directory

    data_as_dict = []
    for a, b, c, d in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block]):
        # the names listed here do not need to be the samr as the variable names
        data_as_dict.append({'problem': a, 'corr_resp': b, 'sub_resp': c, 'sub_acc': d})

        with open(exp_csv_file_path, mode='w') as sub_data:
            data_writer = csv.writer(sub_data, delimiter=',')
            data_writer.writerow(data_as_dict)  # write

'''Save JSON exercises'''
for block in range(nBlocks):
    # run experiment
    # JSON files can be saved with txt or JSON extension, I like to use .txt
    filename = 'savejson_example'
    exp_json_file_path = os.path.join(data_dir, filename)

    data_as_dict = []
    for a, b, c, d in zip(prob[block], corr_resp[block], sub_resp[block], sub_acc[block]):
        # the names listed here do not need to be the samr as the variable names
        data_as_dict.append({'problem': a, 'corr_resp': b, 'sub_resp': c, 'sub_acc': d})

    with open(exp_json_file_path + '_block%i.txt' % block, 'w') as outfile:
        json.dump(data_as_dict, outfile)

'''Read JSON exercises'''
# importing the module
import json

# Opening JSON file
with open('savejson_example_block0.txt') as json_file:
    data = json.load(json_file)

    # Print the type of data variable
    print("Type:", type(data))
    print(data)

    # 1
    mean = 0
    for i in data:
        mean += (i["sub_resp"])
    print("Mean value for sub_resp: ", mean / len(data))

    # 2
    analysis_list = []
    for i in data:
        if i["corr_resp"] == i["sub_resp"]:
            analysis_list.append(i)
        else:
            pass
    print(analysis_list)
    
    #3. 
    for i in data:
        if i["sub_resp"] == 0:
            pass
        else:
            analysis_list.append(i)
    print(analysis_list)

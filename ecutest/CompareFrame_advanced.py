# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:13:12 2023
Modify on Fri Aug 18 10:53:2023
@author: OAM81HC
@modify by: PNM3HC
"""

def compare_frame_output(frame_data_output,frame_data_output_expect):
    frame_data_output = str(frame_data_output)
    if '~' in frame_data_output:
        frame_data_output = ''
    frame_data_output = frame_data_output.replace(" ","")
    
    frame_data_output_expect = str(frame_data_output_expect)
    frame_data_output_expect = frame_data_output_expect.replace(" ","")
    
    num_byte_frame_data_output = int(len(frame_data_output)/2)
    num_byte_frame_data_output_expect = int(len(frame_data_output_expect)/2)
    
    frame_data_output_arr = []
    for i in range(0,num_byte_frame_data_output):
        frame_data_output_arr.append(frame_data_output[i*2:i*2+2])
        
    frame_data_output_expect_arr = []
    for i in range(0,num_byte_frame_data_output_expect):
        frame_data_output_expect_arr.append(frame_data_output_expect[i*2:i*2+2])

    if num_byte_frame_data_output < num_byte_frame_data_output_expect:
        num_byte_fill = num_byte_frame_data_output_expect - num_byte_frame_data_output
        for i in range(0,num_byte_fill):
            frame_data_output_arr.append("  ")
        num_byte_max = num_byte_frame_data_output_expect
    elif num_byte_frame_data_output > num_byte_frame_data_output_expect:
        num_byte_fill = num_byte_frame_data_output - num_byte_frame_data_output_expect
        for i in range(0,num_byte_fill):
            frame_data_output_expect_arr.append("   ")
        num_byte_max = num_byte_frame_data_output
    else:
        num_byte_max = num_byte_frame_data_output
        
    is_frame_different = False
    frame_data_output_ecutest = ''
    frame_data_output_expect_ecutest = ''
    for i in range(0,num_byte_max):
        print(frame_data_output_arr[i])
        print(frame_data_output_expect_arr[i])
        if (frame_data_output_arr[i] == frame_data_output_expect_arr[i]) or (frame_data_output_expect_arr[i] == 'XX'):
            frame_data_output_ecutest += frame_data_output_arr[i] + " "
            frame_data_output_expect_ecutest += frame_data_output_expect_arr[i] + " "
        else:
            frame_data_output_ecutest += "[" + frame_data_output_arr[i] + "] "
            frame_data_output_expect_ecutest += "[" + frame_data_output_expect_arr[i] + "] "
            is_frame_different = True
    
    print(frame_data_output_ecutest)
    print(frame_data_output_expect_ecutest)
    return frame_data_output_ecutest, frame_data_output_expect_ecutest,is_frame_different
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 01:42:47 2023

@author: OAM81HC
"""

# -> 10 22 27 02 01 02 03 04
# <- 30 0x 00
# -> 21 01 02 03 04 01 02 03
# frame_data_input = "270201020304 01"
# frame_data_input = "270201020304 01020304010203 0401020304 0102030401020304 01020304010203"

def send_single_frame(frame_data_input):
    frame_data_input = str(frame_data_input).replace(" ","")
    total_byte = int(len(frame_data_input)/2)

    frame_type = "0"
    data_length = int(hex(total_byte)[2:])
    frame_data = frame_data_input[0 : data_length*2]
    
    single_frame = frame_type + str(data_length) + frame_data
    
    if data_length < 7:
        for i in range(0,7 - data_length):
            single_frame += "00"

    single_frame_ecutest = ''
    for i in range(0,8):
        single_frame_ecutest += single_frame[i*2:i*2+2] + ":"
    single_frame_ecutest = single_frame_ecutest[:-1]
    
    frame_ecutest_return = single_frame_ecutest
    print(frame_ecutest_return)
    return frame_ecutest_return

def store_order_byte_last_sent_first_frame():
    order_byte_last_sent = 6
    
    return order_byte_last_sent

def num_consecutive_frame_to_send(frame_data_input):
    frame_data_input = str(frame_data_input).replace(" ","")
    total_byte = int(len(frame_data_input)/2)
    
    num_consecutive_frame = (total_byte - 6)/7
    
    if num_consecutive_frame > int(num_consecutive_frame):
        num_consecutive_frame = int(num_consecutive_frame) + 1
    else:
        num_consecutive_frame = int(num_consecutive_frame)
    
    return num_consecutive_frame

def is_single_frame(frame_data_input):
    frame_data_input = str(frame_data_input).replace(" ","")
    
    total_byte = int(len(frame_data_input)/2)
    
    if total_byte <= 7:
        return True # single frame
    else:
        return False # first frame
    
def send_first_frame(frame_data_input,order_byte_last_sent):
    # frame_data_input = "270201020304 01020304 0102030401020304 0102030401020304 0102030401020304"
    frame_data_input = str(frame_data_input).replace(" ","")
    total_byte = int(len(frame_data_input)/2)

    frame_type = "1"
    data_length = str(hex(total_byte)[2:].zfill(3))
    frame_data = frame_data_input[0 : order_byte_last_sent*2]
    
    first_frame = frame_type + data_length + frame_data

    first_frame_ecutest = ''
    for i in range(0,8):
        first_frame_ecutest += first_frame[i*2:i*2+2] + ":"
    first_frame_ecutest = first_frame_ecutest[:-1]

    frame_ecutest_return = first_frame_ecutest
    print(frame_ecutest_return)
    return frame_ecutest_return

def store_order_byte_last_sent_consecutive_frame(frame_data_input,order_byte_last_sent_old):
    frame_data_input = str(frame_data_input).replace(" ","")
    total_byte = int(len(frame_data_input)/2)

    remain_byte = total_byte - order_byte_last_sent_old

    if remain_byte <= 7:
        order_byte_last_sent = order_byte_last_sent_old + remain_byte
    else:
        order_byte_last_sent = order_byte_last_sent_old + 7
    print(order_byte_last_sent_old,order_byte_last_sent,remain_byte)
    return order_byte_last_sent

def send_consecutive_frame(frame_data_input,order_byte_last_sent,order_byte_last_sent_old,sequence_number):
    frame_data_input = str(frame_data_input).replace(" ","")
    total_byte = int(len(frame_data_input)/2)
    
    frame_type = "2"
    
    sequence_number = str(sequence_number)
    
    remain_byte = total_byte - order_byte_last_sent_old
    frame_data = frame_data_input[order_byte_last_sent_old*2 : order_byte_last_sent*2]
    
    consecutive_frame = frame_type + sequence_number + frame_data
    
    if remain_byte < 7:
        for i in range(0,7 - remain_byte):
            consecutive_frame += "00"
    
    consecutive_frame_ecutest = ''
    for i in range(0,8):
        consecutive_frame_ecutest += consecutive_frame[i*2:i*2+2] + ":"
    consecutive_frame_ecutest = consecutive_frame_ecutest[:-1]
    
    frame_ecutest_return = consecutive_frame_ecutest
    print(frame_ecutest_return)
    return frame_ecutest_return
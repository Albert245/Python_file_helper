# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:26:01 2023

@author: OAM81HC
"""

def is_nrc78_pending(frame_data_read_first_time):
    frame_data_read_first_time = str(frame_data_read_first_time)
    frame_data_read_first_time = frame_data_read_first_time.replace(":","")
    
    negative_response_sid = frame_data_read_first_time[2:4]
    negative_response_code = frame_data_read_first_time[6:8]
    
    if negative_response_sid == "7F" and negative_response_code == "78":
        return True
    else:
        return False

def is_single_frame(frame_data_read_first_time):
    frame_data_read_first_time = str(frame_data_read_first_time)
    frame_data_read_first_time = frame_data_read_first_time.replace(":","")
    
    frame_type = frame_data_read_first_time[0:1]
    
    if frame_type == "0":
        return True # single frame
    else:
        return False # first frame

def read_single_frame(frame_data_read_first_time):
    frame_data_read_first_time = str(frame_data_read_first_time)
    frame_data_read_first_time = frame_data_read_first_time.replace(":","")

    total_byte = int(frame_data_read_first_time[1:2])
    frame_data = frame_data_read_first_time[2 : 2+total_byte*2]
    print(frame_data)
    return frame_data

def num_consecutive_frame_to_read(frame_data_read_first_time):
    print(frame_data_read_first_time)
    frame_data_read_first_time = str(frame_data_read_first_time)
    frame_data_read_first_time = frame_data_read_first_time.replace(":","")
    total_byte = int("0x" + frame_data_read_first_time[1:4],16)
    
    num_consecutive_frame = (total_byte - 6)/7
    
    if num_consecutive_frame > int(num_consecutive_frame):
        num_consecutive_frame = int(num_consecutive_frame) + 1
    else:
        num_consecutive_frame = int(num_consecutive_frame)
    print(num_consecutive_frame)
    return num_consecutive_frame

def store_order_byte_last_read_first_frame():
    order_byte_last_read = 6
    
    return order_byte_last_read

def store_order_byte_last_sent_consecutive_frame(bytestream,order_byte_last_read_old):
    string = str(bytestream)
    string = string.replace(":","")
    total_byte = int("0x" + string[1:4],16)

    remain_byte = total_byte - order_byte_last_read_old

    if remain_byte <= 7:
        order_byte_last_read = remain_byte
    else:
        order_byte_last_read = 7

    return order_byte_last_read

def read_consecutive_frame(frame_data_read_remain_time,order_byte_last_read):
    frame_data_read_remain_time = str(frame_data_read_remain_time)
    frame_data_read_remain_time = frame_data_read_remain_time.replace(":","")

    frame_data = frame_data_read_remain_time[2 : 2+order_byte_last_read*2]
    print(frame_data)
    return frame_data
    
def put_space_to_frame_data_output(frame_data_output):
    frame_data_output = ' '.join(frame_data_output[i:i+2] for i in range(0, len(frame_data_output), 2))
    return frame_data_output
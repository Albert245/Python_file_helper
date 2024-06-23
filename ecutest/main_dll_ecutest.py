# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:06:07 2022

@author: OAM81HC
"""
import ctypes
from ctypes import *
import ctypes

def main(seed_response):
    lib = cdll.LoadLibrary(r'C:\User\DTU3HC\Task_Nrc78\workspace_ecutest_base_KBT_flashingSID_P2Star_change\UserPyModules\DLL_ECUTEST_KBT.dll')
    seed_response = str(seed_response)# convert ByteStream to String
    seed_subfunction_str = seed_response[6:8]
    print(seed_subfunction_str)
    seed_subfunction_int = int(str(seed_subfunction_str),16)
    print(seed_subfunction_int)
    
    seed_val_str = seed_response[9:].split(':')
    print(seed_val_str)
    seed_val_int = [0] * 4
    for i in range(0,len(seed_val_int)):
        seed_val_int[i] = int(seed_val_str[i],16)
    # seed_val_int.pop(-1)
    print(seed_val_int)

    seed_val_arr = (ctypes.c_ubyte * len(seed_val_int))(*seed_val_int)

    keyout_int = [0] * 4
    keyout_arr = (ctypes.c_ubyte * len(keyout_int))(*keyout_int)
    keyout_final = []

    if 1 == seed_subfunction_int:
        lib.seca_level_1(byref(seed_val_arr),byref(keyout_arr))
    elif 5 == seed_subfunction_int:
        koemdata_int = [0]
        koemdata_arr = (ctypes.c_ubyte * len(koemdata_int))(*koemdata_int)
        lib.seca_level_3(byref(seed_val_arr),byref(keyout_arr),byref(koemdata_arr))

    
    for i in range(0,len(keyout_int)):
        keyout_final.append(hex(keyout_arr[i])[2:].zfill(2).upper())
    
    print(keyout_final)
    
    key_subfunction = seed_subfunction_int + 1
    key_subfunction = hex(key_subfunction)[2:].zfill(2).upper()
    key_request = "06:27:{0}:{1}:{2}:{3}:{4}:AA".format(key_subfunction,
                                                        keyout_final[0],
                                                        keyout_final[1],
                                                        keyout_final[2],
                                                        keyout_final[3],)
    
    print(key_request)
    return key_request
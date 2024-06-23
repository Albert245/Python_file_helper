# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:06:07 2022

@author: OAM81HC
"""
import ctypes
from ctypes import *
import ctypes

def ECB_encryption(seed_response):
    lib = cdll.LoadLibrary(r'D:\oam81hc\workspace_ecutest_isz_ev_v9\UserPyModules\ISZ_EV_27_03.dll')
    
    seed_response = str(seed_response) # convert ByteStream to String
    
    seed_subfunction_str = seed_response[6:8]
    seed_subfunction_int = int(str(seed_subfunction_str),16)
    # print(seed_subfunction_int)
    
    seed_val_str = seed_response[9:].split(':')
    seed_val_int = []
    for seed in seed_val_str:
        seed_val_int.append(int(str(seed),16))
    # print(seed_val_int)

    seed_val_arr = (ctypes.c_ubyte * len(seed_val_int))(*seed_val_int)
    keyout = [0,0,0,0,0]
    keyout_arr = (ctypes.c_ubyte * len(keyout))(*keyout)
    keyout_final = []
    
    lib.ECB_encryption(byref(seed_val_arr),byref(keyout_arr))

    for i in range(0,len(keyout)):
        keyout_final.append(hex(keyout_arr[i])[2:].zfill(2).upper())
    # print(keyout_final)
    
    key_subfunction = seed_subfunction_int + 1
    key_subfunction = hex(key_subfunction)[2:].zfill(2).upper()
    key_request = "07:27:{0}:{1}:{2}:{3}:{4}:{5}".format(key_subfunction,
                                                        keyout_final[0],
                                                        keyout_final[1],
                                                        keyout_final[2],
                                                        keyout_final[3],
                                                        keyout_final[4],)
    
    # print(key_request)
    return key_request
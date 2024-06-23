# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:06:07 2022

@author: OAM81HC
"""
import ctypes
from ctypes import *

import subprocess

def main(python37_32bit_path,run_dll_seca_py_path,dll_path,seed_response):
    seed_response = str(seed_response)
    seed_response = seed_response.replace(" ","")
    
    try:
        lib = cdll.LoadLibrary(dll_path)
    except Exception as e:
        # DLL 32 bit
        command = [python37_32bit_path,run_dll_seca_py_path,'--dll_path',dll_path,'--seed_response',seed_response]
        subprocess_ret = subprocess.check_output(command, stderr=subprocess.STDOUT)
 
    key_str = str(subprocess_ret)
    key_str = key_str[3:-6]
    key_str = key_str.replace("'", "")
    key_str = key_str.replace(",", "")
    key_str = key_str.replace(" ", "")
    
    key_str_with_space = ' '.join(key_str[i:i+2] for i in range(0, len(key_str), 2))
    
    sub_function_seed = seed_response[2:4]
    
    sub_function_key = str(int(sub_function_seed) + 1).zfill(2)
    
    key_request = "27 " + sub_function_key + " " + key_str_with_space
    
    return key_request
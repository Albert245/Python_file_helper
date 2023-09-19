"""
Created on Fri Aug 18 10:00:2023

@author: PNM3HC

"""

DID_test = ['3B04', 2, [1, 0], [['ACCtl_flgElecAirCdngModReq2', [0.0, 1.0], ['00', '01']]],
             True, [['GlbDa_nrHvBattThermCirc', [1, 2]], ['0F', 'XX']]]

# handle DID info total sheet

def Get_DID_info_row(DID_info_total,DID_idx = 1):
    return DID_info_total[DID_idx-1]

# handle DID info row

def Get_DID(DID_row):
    return DID_row[0]

def Get_byte_num(DID_row):
    return DID_row[1]

def Get_addr_sp(DID_row,addr = 'phys'):
    addr = addr.upper()
    if 'PHY' in addr:
        pos = 0
    else:
        pos = 1
    if DID_row[2][pos] == 1:
        return True
    else:
        return False
    
def Count_ramcell(DID_row):
    return len(DID_row[3])

def Count_ramcell_change(DID_row, idx):
    if len(DID_row[3][idx-1][1]) == len(DID_row[3][idx-1][2]):
        return len(DID_row[3][idx-1][1])
    else:
        return 0

def Get_ramcell_name(DID_row,ramcell_idx = 1,calib_tail = '.source'):
    return '{0}{1}'.format(DID_row[3][ramcell_idx-1][0],calib_tail)

def Get_ramcell_phys(DID_row,ramcell_idx = 1,loop_idx = 1):
    return DID_row[3][ramcell_idx-1][1][loop_idx-1]

def Get_ramcell_hex(DID_row,ramcell_idx,loop_idx):
    return DID_row[3][ramcell_idx-1][2][loop_idx-1]

def Check_condition(DID_row):
    return DID_row[4]

def Count_Condition(DID_row):
    return (len(DID_row[5]) - 1)

def Get_Condition_name(DID_row,Condition_idx,tail='.source'):
    if '_C' not in DID_row[5][Condition_idx-1][0][-3:]:
        return '{0}{1}'.format(DID_row[5][Condition_idx-1][0],tail)
    else:
        return DID_row[5][Condition_idx-1][0]

def Get_Condition_value(DID_row, Condition_idx = 1,loop_idx = 1):
    return DID_row[5][Condition_idx-1][1][loop_idx-1]

def Get_Condition_hex(DID_row, loop_idx = 1):
    if Check_condition(DID_row):
        return DID_row[5][-1][loop_idx-1]
    else:
        return 'XX'

def Respond_RBDI_22(DID_row,addr_sp,ramcell_idx,ramcell_val_idx,val_by_calib = 'XX'):
    if addr_sp:
        DID = DID_row[0]
        byte_num = Get_byte_num(DID_row) + 2
        if val_by_calib == 'XX':
            check_value = DID_row[3][ramcell_idx-1][2][ramcell_val_idx-1]
        else:
            check_value = val_by_calib
        fill_data = 'XX'*(byte_num - 3)
        request_RDBI_22 = '62' + str(DID) + str(fill_data) + str(check_value)
        return request_RDBI_22
    else:
        return ''
    
def Request_RDBI_22(DID_row):
    return '22{}'.format(str(DID_row[0]))
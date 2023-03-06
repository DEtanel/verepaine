array = list()
##########################################################################
########## read from date.txt and write to array #########################
with open("date.txt", 'r') as date:
    for line in date:
        array.insert(0,line.strip())
date.close
########## write from array to date_1.txt ################################
date_1 = open('date_1.txt','w')
for i in range (0, len(array)):
    date_1.write(array[i]+'\n')

date_1.close
array.clear()
##########################################################################
##########################################################################
#////////////////////////////////////////////////////////////////////////#
##########################################################################
########## read from sys.txt and write to array ##########################
with open("sys.txt", 'r') as sys:
    for line in sys:
        array.insert(0,line.strip())
sys.close
########## write from array to sys_1.txt #################################
sys_1 = open('sys_1.txt','w')
for i in range (0, len(array)):
    sys_1.write(array[i]+'\n')

sys_1.close
array.clear()
##########################################################################
##########################################################################
#////////////////////////////////////////////////////////////////////////#
##########################################################################
########## read from dia.txt and write to array ##########################
with open("dia.txt", 'r') as dia:
    for line in dia:
        array.insert(0,line.strip())
dia.close
########## write from array to sys_1.txt #################################
dia_1 = open('dia_1.txt','w')
for i in range (0, len(array)):
    dia_1.write(array[i]+'\n')

dia_1.close
array.clear()
##########################################################################
##########################################################################
#////////////////////////////////////////////////////////////////////////#
##########################################################################
########## read from pulse.txt and write to array ########################
with open("pulse.txt", 'r') as pulse:
    for line in pulse:
        array.insert(0,line.strip())
pulse.close
########## write from array to pulse_1.txt ###############################
pulse_1 = open('pulse_1.txt','w')
for i in range (0, len(array)):
    pulse_1.write(array[i]+'\n')

pulse_1.close
array.clear()
##########################################################################


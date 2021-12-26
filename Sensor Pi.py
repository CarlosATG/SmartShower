#Python 3 program for YS S201 flow meter using interrupts
#Writes to screen & file at user selected intervals
#
import RPi.GPIO as GPIO
import time, sys
f = open ('FlowMeterOutPut.txt', 'a')

GPIO.setmode(GPIO.BCM)
inpt= 13
GPIO.setup(inpt, GPIO.IN)
minutes = 0
constant = 0.006
time_new =0.0
rpt_int=10

global rate_cnt, tot_cnt
rate_cnt = 0
tot_cnt = 0

def Pulse_cnt (int_pin):
     global rate_cnt, tot_cnt
     rate_cnt +=1
     tot_cnt += 1

#MAIN
print('Water Flow - Aproximate',
           str(time.asctime(time.localtime(time.time()))))
rpt_int = int(input('Input desired report interval in seconds'))
print('Reports every', rpt_int,' seconds')
print('Control C to exit')
f.write('\nWater Flow - Approximate - Reports Every ' +
        str(rpt_int)+' Seconds' + str(time.asctime(time.localtime(time.time()))))

while True:
    time_new=time.time()+rpt_int
    rate_cnt = 0
    while time.time()<= time_new:
        try:
            None
            print(GPIO.input(inpt), end = '')
        except KeyboardInterrupt:
            print('\nCTRL C - Exiting nicely')
            GPIO.cleanup()
            f.close()
            print('Done')
            sys.exit()
    minutes +=1
    
    LperM = round (((rate_cnt*constant)/(rpt_int/60)),2)
    TotLit = round(tot_cnt*constant, 1)
    print('\nLiters / min', LperM, '(', rpt_int, 'second sample)')
    print('Total Liters', TotLit)
    print('Time(min & clock) ', minutes, '\t', time.asctime(time.localtime(time.time())), '\n')
    f.write('\nLiters / min ' + str(LperM))
    f.write('  Total Liters ' + str(TotLit))
    f.write('  Time (min & clock) ' + str(minutes) + '\t' + str(time.asctime(time.localtime(time.time()))))
    f.flush()
GPIO.cleanup()
f.close()
print('Done :D')
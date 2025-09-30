'''psuedocode
initialize the time stampwhen user sets the timer.
using a while loop create a varible which updates it time stamp with each iteration 
create another variable within the loop to check the difference between the initial time stamp and the last time stamp.
if the difference is equal to the users specified time, turn while loop false and let the user know that the time has elapses.
'''
import time 

def timer():
    timeInSeconds = int(input('enter timer(in seconds)\n'))

    time.sleep(timeInSeconds)

    print('time up')


    # start = int(time.time())
    # #print(start)

    # running = True
    # while running:
    #     stop = int(time.time())
    #     difference = stop - start
        
    #     if difference >= timeInSeconds:
    #         print('times up')
    #         running = False


if __name__ == '__main__':
    timer()

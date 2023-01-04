''''
NAME: main.py
AUTHOR: ALEX
DATE: 2023-01-01

DESCRIPTION: This is a current work in progress setting up multiproccessing for control input
            but it is not working as intended. I am trying to read input from the keyboard for now but this may be the wrong approch.
            For multiproccessing you have to get input from the main function and then pass it to the child process.
'''

#setup for mutiprocessing and reading input from a function

from multiprocessing import Process, Manager
from ctypes import c_char_p
import os, sys

def controller(name, m):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    #try catch with a while loop
    while True:
        try:
            print("Current command: ", m.value)
            #read input from keyboard
            m.value = sys.stdin
            #if input is 'exit' then break the loop
            if m.value == 'exit':
                break
            #else print the input
            else:
                print(m.value)
        #if keyboard interrupt then break the loop
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            break
        except Exception as e:
            print("Error thrown: ", e)
            break



if __name__=='__main__':
    with Manager() as manager:
        command = manager.Value(c_char_p, "Hello")
        print('Parent process %s.' % os.getpid())
        pController = Process(target=controller, args=("controller",command,))
        print('Child process will start.')
        pController.start()

        pController.join()

        print('Child process end.')

# Path: src/main.py

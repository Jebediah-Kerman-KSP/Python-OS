#initilising OS
print('Operating System ON')
print('importing Libraries')
import time as t
import os 
from os import system
print('#-----------')
t.sleep(1)
system('cls')
print('Loading Functions')
#creating main functions and main()
        

def logo():
    system('cls')
    print('+------------+--------+')
    print('| Surface OS | v1.0.0 |')
    print('+------------+--------+')

def main():
    #main loop for OS

    mi = input('S:\Python>')
    if mi == 'test':
        print('RAN COMMAND TEST')

    elif mi == 'exit':
        print ('exiting')

        system('cls')
        print('exiting')
        t.sleep(2)
        print('nah mate')

    elif mi == 'help':
        print('''
#######################################
              
        SURFACE OS COMMANDS:
               
            test        Runs a test command
            help        shows a list of commands
            new         creates a new file
BROKEN      ap          Appends a file
WIP         cd          edits a file
WIP         del         deletes a file
              
        For a tutorial on how to use the commands type "help" then the command
              

              ''')

    elif mi == 'new':
        cf = input('createfile>')
        f = open(cf, "x")
        print('file ['+cf+'] has succesfully been created')

    elif mi == 'ap':
        print('WIP [for now just use "cd"]')
        #fa = input('appendFile>')
        #with open(fa, "a") as f:
        #    faw = input('>')
        #    f.write(faw)

    elif mi == 'cd':
        cd = input('cdFile>')
        with open(cd, "w") as f:
            fcd = input('>')
            f.write(fcd)
    
    elif mi == 'del':
        print('WIP')

    elif mi == 'dir':
        print('broken. pls fix for me')
        # Get the list of all files and directories
        #path = "YOUR DIR HERE"
        #dir_list = os.listdir(path)
        #print("Files and directories in '", path, "' :")
        # prints all files
        #print(dir_list)

    elif mi == 'cls':
        os.system('cls')
        logo()
        main()

    else:
       print('Command: ['+mi+'] not recognised as a command! for commands type "help"')

    main()

def bootMenu():
        #boot menu
        system('cls')
        print('''
#######################
# Boot Menu           #
#                     #
# 1. change console   #
# colour              #
# 2. boot             #
#######################
              ''')
        BMI = input('OS/BootMenu>')
        if BMI == '1':
            CC = input('OS/Console/Colour>')
            system('color '+CC)
            bootMenu()

        elif BMI == '2':
            print('loading')
            t.sleep(5)

        else:
            bootMenu()
system('cls')
bootMenu()
logo()
main()

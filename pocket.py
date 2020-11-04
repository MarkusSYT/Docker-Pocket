import os

def color(c, text):
    if(str(c) == "green"):
        return '\033[92m' + str(text) + '\033[0m'
    elif(str(c) == "red"):
        return '\033[91m' + str(text) + '\033[0m'
    elif(str(c) == "blue"):
        return '\033[1;34;40m' + str(text) + '\033[0m'
    elif(str(c) == "yellow"):
        return '\033[1;33;40m' + str(text) + '\033[0m'
    elif(str(c) == "lightgreen"):
        return '\033[1;32;40m' + str(text) + '\033[0m'

def menu():
    print(color('blue',' _____             _            ')+color('red',' _____           _        _  '))
    print(color('blue','|  __ \           | |           ')+color('red','|  __ \         | |      | |  '))
    print(color('blue','| |  | | ___   ___| | _____ _ __')+color('red','| |__) |__   ___| | _____| |_ '))
    print(color('blue','| |  | |/ _ \ / __| |/ / _ \ \'__')+color('red','|  ___/ _ \ / __| |/ / _ \ __|'))
    print(color('blue','| |__| | (_) | (__|   <  __/ |  ')+color('red','| |  | (_) | (__|   <  __/ |_ '))
    print(color('blue','|_____/ \___/ \___|_|\_\___|_|  ')+color('red','|_|   \___/ \___|_|\_\___|\__|'))
    print('')
    print('     by MarkusS (https://github.com/MarkusSYT)')
    print('                (https://gitlab.com/MarkusSYT)')
    print('')
    print('1.   list local images')
    print('')
    print('2.   list local containers')
    print('')
    print('3.   list running containers')
    print('')
    print('4.   download image')
    print('')
    print('99.   exit')
    print('')

def select():
    select = int(input('>'))
    if(select == 1):
        os.system('docker images')
    elif(select == 2):
        os.system('docker ps -a')
    elif(select == 3):
        os.system('docker ps')
    elif(select == 4):
        img = str(input('imagename: '))
        os.system('docker pull ' + img)
    elif(select == 99):
        exit()

if __name__ == "__main__":
    menu()
    select()
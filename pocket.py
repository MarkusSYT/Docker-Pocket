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

def create_cont():
    img = str(input('imagename: '))
    cont = str(input('containername: '))
    cont_cmd = ''
    if(cont!=''):
        cont_cmd = f'--name {cont}'
    print('how to expose port: HOSTPORT_1:CONTAINERPORT_1;HOSTPORT_2:CONTAINERPORT_2')
    port = str(input('ports: '))
    ports = port.split(';')
    port_str = ''
    if(len(ports) != 0):
        for item in ports:
            port_str = port_str+' '+'-p'+item
    return f'docker run -d {port_str} {cont_cmd} {img}'

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
    print('1.   list local images           7. container shell')
    print('')
    print('2.   list local containers       8. create container')
    print('')
    print('3.   list running containers     9. start container')
    print('')
    print('4.   download image              10. stop container')
    print('')
    print('5.   remove image')
    print('')
    print('6.   remove conainer')
    print('')
    print('99.  exit')
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
    elif(select == 5):
        img = str(input('imagename: '))
        os.system('docker rmi ' + img)
    elif(select == 6):
        cont = str(input('containername: '))
        os.system('docker rm ' + cont)
    elif(select == 7):
        cont = str(input('containername: '))
        os.system('docker exec -it '+ cont + ' /bin/bash')
    elif(select == 8):
        os.system(create_cont())
    elif(select == 9):
        cont = str(input('containername: '))
        os.system('docker start ' + cont)
    elif(select == 10):
        cont = str(input('containername: '))
        os.system('docker stop ' + cont)
    elif(select == 99):
        exit()
    input("\npress any key to continue")
    main()

def main():
    menu()
    select()

if __name__ == "__main__":
    main()
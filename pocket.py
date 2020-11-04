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


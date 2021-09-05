from sys import stdout
import msvcrt as m
import keyboard  
import sys
import os

def MOTEUR(TEXTS):
    A=5
    for char in TEXTS:
        if A<5:
            stdout.write(char)
            stdout.flush()
            A=A+1
        else:    
            KEY = m.getch()
            while KEY == "":
                pass 
            else:
                stdout.write(char)
                stdout.flush()
                A=0

if __name__ == "__main__":
    if sys.platform == 'win32' : os.system('color 0F')
    FICHIER = open("text.txt",'r')
    TEXTS = FICHIER.read()
    MOTEUR(TEXTS)

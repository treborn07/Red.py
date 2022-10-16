#!/usr/bin/python3

import os

import time

import logging

import subprocess

from sys import platform

print('\033[0;30;41mPor Favor\033[m') #sublinhado e marcado vermelho

idade = input("Qual é a sua idade?: ")

print('\033[0;49;96ma sua idade é:\033[m', idade) #texto ciano

if idade < "18" :

    print ("\033[0;49;96mhoje não.\033[m \n")

    exit()

    

elif idade >= "18" : 

    print ("\033[5;49;92mOk, acesso liberado.\033[m \n")           

    time.sleep(5)

    os.system("clear")

else:

     print ("")

print ("®***************************************©")

print ("####                                    #")

print ("#. # \033[5;49;92m@ruanrobert89 \033[m  #")

print ("#  #                                    #")

print ("#  ####################                 #")

print ("# \033[4;49;91mRGrayHAT-SCRIPT \033[m     |##########")

print ("#  \033[4;49;91mANON-FMLBR\033[m               ###          #")

print ("# (.  )`````````````(   )##             #")

print()

print("\033[4;49;91mBem vindo\033[m")

print("\033[4;49;91mAtualizando seu termux\033[m")

time.sleep(5)

os.system("apt update -y && apt upgrade -y")

os.system("apt install git -y")

os.system("cd $HOME")

os.system("git clone https://github.com/mishakorzik/UserFinder")

os.system("git clone https://github.com/machine1337/iplocation")

os.system("clear")

time.sleep(3)

print("▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒")

print("▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒")

print("▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒")

print("▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒")

print("▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌")

print("▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

print("\033[7;49;91m©***************************************©\033[m")

print("\033[7;49;91mTheRedHatGov\033[m")

print("\033[7;49;91mHACK THE PLANET\033[m")

print("\033[7;49;91m                   \033[m")

print("\033[7;49;91m                   \033[m")

print("\033[7;49;91m                   \033[m")

print("\033[7;49;91m                   \033[m")

print("\033[7;49;91m                   \033[m")

print("\033[7;49;91m                   \033[m")

print("1: LAZYMUX")

print("2: ZPHISHER")

print("3: NGROK")

print("4: IP-TRACER")

print("#$Extras$#")

print("5: Procurar PERFIL")

print("6: MeuIp")

print("7: Localizar IP")

print("8: ") 

escolha = False

while escolha == False:

    nivel = int(input('Escolha uma opção: '))

    if(nivel == 1):

        os.system("git clone https://github.com/Gameye98/Lazymux")

        escolha = True

    elif(nivel == 2):

        os.system("git clone https://github.com/htr-tech/zphisher")

        escolha = True

    elif(nivel == 3):

        os.system("git clone https://github.com/Marcel0Sousa/termux-ngrok")

        escolha = True

    elif(nivel == 4):

        os.system("git clone https://github.com/rajkumardusad/IP-Tracer")

        escolha = True

    elif(nivel == 5):

        os.system("bash /data/data/com.termux/files/home/UserFinder/UserFinder.sh")

    elif(nivel == 6):

        os.system("curl ifconfig.me")

    elif(nivel == 7):

        os.system("bash /data/data/com.termux/files/home/iplocation/run.sh")

    else:

        print("Opção inválida. Escolha novamente.")

   

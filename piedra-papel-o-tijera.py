# programa para jugar piedra papel o tijera en python

#libreria
import random
import math

# imput
print("-----------------------------")
print("----piedra papel o tijera----")
print("-----------------------------")
print("--1 = piedra 2 = papel 3 = tijera--")
print("-----------------------------")

computer_number = random.randint(1,3)

usar_number = int(input("escoja piedra, papel o tijera: "))

#------------
#processing
#------------

if computer_number == 1:
    computer_choice = "piedra"
elif computer_number == 2:          
    computer_choice = "papel"
else:
    computer_choice = "tijera"  

#---------
#output
#---------

print("-----------------------------")
print("la computadora escogio: " +str(computer_choice))
print("-----------------------------")
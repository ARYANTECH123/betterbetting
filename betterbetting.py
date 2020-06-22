import random

#The betterbetting Python module for better luck based value results in Python
#Wirten by the Serial PWNER for Aman Sanju
#Version 1.0.2
#Build 21062020

#betterbetting uses a class called player to store data about each player
class player:
    #Initializing all the variables for the class
    def __init__(self, name, amt):
        self.name = name
        self.purse = amt
        self.luck = .5
        self.history = [0.5,0.5,0.5]

    def add(self, x):
        self.purse += x

    #This is the heart of betterbetting, the History Based Random Outcome Generator
    #or the HBROG function.(see end of code for more)
    #It uses the player's luck history to compute a luck value which is
    #self regulating, and performs a weighted desision.
    def GenerateOutcome(self):
        mode = 0

        if(p1.luck < 0.5):
            mode = 0.01
        if(p1.luck > 0.5):
            mode = -0.01
        
        inc = random.triangular(-0.02, 0.02,mode)

        avg = sum(p1.history)/len(p1.history)

        p1.luck  = avg + inc

        p1.history.insert(0, p1.luck)

        del(p1.history[3])

        if(random.random() <= p1.luck):
            return True
        else:
            return False

#Plays DOuble or Nothing with the player
#The string returned are so that the function can be called
#within a print statemnt, a console log ot any oher output

def dblOrNtg(p1):
    amount = p1.purse
    if(p1.GenerateOutcome()):
        p1.purse += p1.purse
        return "You won " + str(amount) + ". Your balance is " + str(p1.purse)
    else:
        p1.purse = 0
        return "You lost" + str(amount) + ". Your balance is " + str(p1.purse)

def simpleBet(p1, amount):
    
    if(p1.GenerateOutcome()):
        p1.purse += amount
        return "You won " + str(amount) + ". Your balance is " + str(p1.purse)
    else:
        p1.purse-= amount
        return "You lost" + str(amount) + ". Your balance is " + str(p1.purse)
    
        
'''
Here beging a short explanation of the HBROG algorithm.

HBROG is short for History Based Random Outcome Generator.
It is a algorithm by meas of which betterbetting generates binary decisions.

Every player has 2 'directive attributes' - Luck nad history

Luck is the probability of the player winning, History is the players
luck over the past 3 games.

The algorithm uses a triangular meaan to compute the increment by which
the average of the hsitory is changed. It is a negetive feecback loop.
luck the the avg(history) + increemnt

This system creates a weighted negetive feedback loop that controlles luck\
and thorws off patterns, as any pattern longer than 3 moves cannot be established
due to the history updation.
'''
